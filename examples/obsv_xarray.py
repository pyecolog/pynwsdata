
from functools import partial
import concurrent.futures as cf
from itertools import chain
import os
from pynwsdata.configuration import Configuration
from pynwsdata.api_client import ApiClient
from pynwsdata.api_object import ApiField
from pynwsdata.api.geo_api import GeoApi
from pynwsdata.exceptions import ApiException
from pynwsdata.models.observation import Observation
from pynwsdata.models.observation_geo_json import ObservationGeoJson
from pynwsdata.models.quantitative_value import QuantitativeValue
import sys
from threading import RLock
import time
from typing import Optional, Union
import xarray as xr
import pint_xarray
import numpy as np

from pynwsdata.units.registry import UnitRegistry, WmoUnit

reg = UnitRegistry()
WmoUnit.initialize()

# fields for each ObservationGeoJson.properties value
OBSV_FIELDS: dict[str, ApiField] = Observation.fields

ApiClient.set_verbose_logging()

EMPTY_MAP = dict()

# callback for threaded dispatch when requesting the latest observation data
def observation_callback(station: str,
                         lock: RLock, data: dict[str, dict[str, object]],
                         future: cf.Future[ObservationGeoJson]):
    with lock:
        # hold the data lock and update data for observation/error tracking
        if future.cancelled():
            data['cancelled'][station] = True
            return
        exc: Optional[ApiException] = future.exception(None)
        if exc:
            if exc.status == 404:
                try:
                    nf = data["not_found"]
                except KeyError:
                    data["not_found"] = [station]
                else:
                    nf.append(station)
            else:
                try:
                    err = data["errors"]
                except KeyError:
                    data["errors"] = {station: exc}
                else:
                    err[id] = exc
            return
        obsv = future.result()
        ocls = obsv.__class__
        for name, field in OBSV_FIELDS.items():
            value = field.__get__(obsv.properties, ocls)
            # filter out any direct None/empty value or QuantativeValue with a None value,
            # else storing the value for this station under the observation field name
            if value and not (isinstance(value, QuantitativeValue) and value.value is None):
                data[name][station] = value


def latest_observations(loc: Union[str, tuple[float, float]], config: Optional[Configuration] = None):
    # primary callback
    #
    # requires DD format encoding for latitude, longitude
    # for a location in NWS weather map coverage
    #
    # this will retrieve station location information for the weather
    # grid at the provided lattitude and longitude, then collectintg
    # observation data for each station
    #
    # after the observation requests have all completed, this function
    # will construct an xarray DataSet. The DataSet will contain all
    # measured values as reported in the observation responses. For
    # each measurement, a coordinates series will be included in
    # the dataset, indicating which station was reporting each
    # measurement value.
    #
    # known limitations
    # - no pagination support for the stations list
    #
    with ApiClient(config or Configuration()) as client:
        api_instance = GeoApi(client)
        if isinstance(loc, str):
            point_response = api_instance.geocode_point(loc)
        else:        
            point_response = api_instance.point(loc)
        props = point_response.properties
        gid = props.grid_id
        grid_x = props.grid_x
        grid_y = props.grid_y
        print("-- using grid location: %s/%s,%s" % (gid, grid_x, grid_y))
        stations_response = api_instance.gridpoint_stations(
            wfo=gid, x=grid_x, y=grid_y)


        data: dict[str, dict[str, object]] = {
            k: {} for k in OBSV_FIELDS.keys()
        }
        futures: dict[str, cf.Future[ObservationGeoJson]] = dict()

        with cf.ThreadPoolExecutor(thread_name_prefix="observation_") as xt:
            # dipsatching the observation requests to separate threads
            lock = RLock()
            for station in stations_response.features:
                sid = station.properties.station_identifier
                sid = sys.intern(sid)
                future = xt.submit(
                    api_instance.station_observation_latest, station_id=sid)
                cb = partial(observation_callback, sid, lock, data)
                future.add_done_callback(cb)
                futures[sid] = future

        #
        # block in the main thread until all observation requests have completed
        #
        # individual requests may complete with error
        #

        poll = sys.getswitchinterval()
        while next((True for f in futures.values() if not f.done()), None):
            time.sleep(poll)


        vars = dict()
        coords = dict()
        units = dict()
        # initialize the attribute map for the resulting dataset
        attrs = {
            "wfo": gid,
            "grid_x": grid_x,
            "grid_y": grid_y,
            "point": point_response,
            "source_units": units,
            "stations": {sys.intern(os.path.basename(stn.id)): stn for stn in stations_response.features}
        }

        extra_names = frozenset(("not_found", "errors"))


        for name, values in data.items():
            name = sys.intern(name)
            if name in extra_names:
                attrs[name] = tuple(values)
            elif values:
                coords_name = "_".join((name, "station"))
                # store the station series under dataset coords
                cc = np.array(tuple(values.keys()))
                coords[coords_name] = ([coords_name], cc)
                #
                # format and store the value series under dataset vars
                #
                # the storage will vary, here, depending on the type
                # of the first (assuming: all) values in the series
                #
                tv = tuple(values.values())
                first = tv[0]
                unit = None
                if isinstance(first, QuantitativeValue):
                    # store the value series,
                    # also storing the value unit
                    unit = first.unit_code
                    if unit.startswith("wmo"):
                        # FIXME this parse is not sufficient for wind_direction
                        # => "degree (angle)"
                        unit = unit.split(":", 1)[-1] # .replace("_", " ")
                    # try to parse the unit name to a pint unit name
                    try:
                        unit = WmoUnit[unit]
                    except KeyError:
                        pass
                    else:
                        unit = str(reg.Unit(unit))
                    units[name] = unit
                    cv = np.array(tuple(qv.value for qv in tv))
                elif isinstance(first, list):
                    # store the object series as an array of tuples,
                    # where each tuple represents a series of values
                    # as reported for each corresponding station
                    # 
                    # e.g fields: cloud_layers, present_weather
                    # 
                    # The corresponding station series will be available
                    # in the field's <name>_station coordinate within
                    # the resulting dataset, e.g cloud_layers_station
                    #
                    # Examples: accessing individual values
                    # from the series for a single weather station
                    #
                    #  obsv.cloud_layers[0].data[()][0].base
                    #  obsv.cloud_layers[0].data[()][0].amount
                    #  obsv.cloud_layers_station[0]
                    #   
                    #  obsv.present_weather[0].data[()][0].raw_string
                    #  obsv.present_weather[0].data[()][0].weather
                    #  ...
                    #  obsv.present_weather_station[0]
                    #
                    cv = np.fromiter(map(tuple, tv), "O", count=len(tv))
                else:
                    # store the series of individual values for all
                    # reporting stations
                    cv = np.array(tv)
                if unit:
                    mattrs = {"units": unit}
                else:
                    mattrs = EMPTY_MAP
                vars[name] = ([coords_name], cv, mattrs)

        return xr.Dataset(vars, coords, attrs)

if __name__ == "__main__":
    obsv = latest_observations("Fargo, ND").pint.quantify()

    # >>> obsv.temperature.pint.to("degF")
    # ...
    # >>> obsv.visibility.pint.to("mi")
    # ...
    #
    # remove units:
    # >>> obsv_direct = obsv.pint.dequantify()
    #
    # list variables (including coordinate variables)
    # >>> obsv._variables.keys()
    #

    # see also
    # https://xarray.dev/blog/introducing-pint-xarray