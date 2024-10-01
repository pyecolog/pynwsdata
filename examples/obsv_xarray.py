
from functools import partial
import concurrent.futures as cf
from datetime import datetime, UTC
import os
import pandas as pd
import sys
from threading import RLock
import time
from typing import Any, Optional, Union
import xarray as xr
from pint_xarray import unit_registry
import numpy as np
import numpy.typing as npt
import shapely

from ecolog.util.const import StrConst
from ecolog.util.nputil import is_nan_all
from pynwsdata.configuration import Configuration
from pynwsdata.api_client import ApiClient
from pynwsdata.api_object import ApiField, ApiObject
from pynwsdata.api.geo_api import GeoApi
from pynwsdata.exceptions import ApiException
from pynwsdata.models.observation import Observation
from pynwsdata.models.observation_geo_json import ObservationGeoJson
from pynwsdata.models.quantitative_value import QuantitativeValue

from pynwsdata.units.registry import WmoUnit, parse_unit

WmoUnit.initialize()

# fields for each ObservationGeoJson.properties value

OBSV_INDEX_FIELDS: frozenset[str] = frozenset({"timestamp"})
OBSV_PROPERTY_FIELDS: dict[str, ApiField] = dict(Observation.fields)


ApiClient.set_verbose_logging()

EMPTY_MAP = dict()
EMPTY_STR = ""

class Const(StrConst):
    # known limitation:
    #
    # if the resulting observation dataset is stored to netcdf,
    # this enum class must be available when the dataset
    # is restored from file
    #
    NOT_FOUND = "not_found"
    ERRORS = "errors"
    CANCELLED = "cancelled"
    LOCATION_REQUESTED = "location_requested"
    LOCATION_MATCH = "location_match"
    LOCATION_COORDS = "location_coords"
    STATION_ID = "station_id"
    STATION_NAMES = "station_names"
    STATION_DATA = "station_data"
    STATION_NAME = "station_name"

    TIMESTAMP = "timestamp"
    LAT = "lat"
    LON = "lon"
    RELATIVE_DISTANCE = "relative_distance"
    RELATIVE_TO = "relative_to"
    METRIC = "metric"
    INDEX = "index"
    POINT = "point"
    POINT_DATA = "point_data"
    WFO = "wfo"
    GRID_X = "grid_x"
    GRID_Y = "grid_y"
    SOURCE_UNITS = "source_units"
    UNITS = "units"
    TZ = "tz"


def observation_callback(station: str, offset: int, units: dict[str, Any],
                         lock: RLock, data: dict[str, dict[str, object]],
                         future: cf.Future[ObservationGeoJson]):
    # callback for threaded dispatch when requesting the latest observation data

    with lock:
        # hold the data lock and update data for observation/error tracking
        if future.cancelled():
            # record the cancelled state
            try:
                can: list[str] = data[Const.CANCELLED]
            except KeyError:
                data[Const.CANCELLED] = [station]
            else:
                can.apppend(station)
            return
        exc: Optional[ApiException] = future.exception(None)
        if exc:
            # record the exception for this observation request
            if exc.status == 404:
                try:
                    nf: list[str] = data[Const.NOT_FOUND]
                except KeyError:
                    data[Const.NOT_FOUND] = [station]
                else:
                    nf.append(station)
            else:
                try:
                    err = data[Const.ERRORS]
                except KeyError:
                    data[Const.ERRORS] = {station: exc}
                else:
                    err[id] = exc
            return
        obsv = future.result(0)
        props = obsv.properties
        pcls = props.__class__
        for name, field in OBSV_PROPERTY_FIELDS.items():
            try:
                series = data[name]
            except KeyError:
                # assumption: field is being skipped for netcdf_compat
                continue
            value = field.__get__(props, pcls)
            if isinstance(value, QuantitativeValue):
                xv = value.value
                if xv is None:
                    xv = np.nan
                # ensure the unit is recorded for this field
                try:
                    uu = units[name]
                except KeyError:
                    uu = value.unit_code
                    if uu:
                        units[name] = parse_unit(uu)
            elif value:
                xv = value
            elif field.interface.interface_class is str:
                xv = EMPTY_STR
            else:
                xv = np.nan

            if name == Const.TIMESTAMP and xv:
                try:
                    data[Const.TZ]
                except KeyError:
                    data[Const.TZ] = str(xv.tzinfo)

            series[offset] = xv

def latest_observations(loc: Union[str, tuple[float, float]], *,
                        config: Optional[Configuration] = None,
                        netcdf_compat: bool = False):
    # primary callback
    #
    # loc: either a tuple in DD format, encoding (latitude, longitude)
    # or a string denoting a collloquial place name. If provided as a
    # place name, the coordinates for the location will be determined
    # via a geocode query with Nominatim.
    #
    # This function will retrieve point / weather grid information for
    # the denoted lattitude and longitude, then collecting observation
    # data for each station in the respective grid section. Each
    # observation request will run within a thread of the thread pool
    # executor for the contained api_instance.
    #
    # After the observation requests have all completed in each request
    # thread, along with any data updates for the observations at each
    # respective station set, this function will construct an xarray
    # DataSet. The DataSet will present the measured values as reported
    # in the observation  responses, as well as measurement unit information
    # for each observation series (when available).
    #
    # Each measurement series in the dataset will be presented in relation
    # to the coordinates of a multi-index. The multi-index will be comprised
    # of the following index levels:
    #
    # - id (station ID) : np.ndarray, dtype "U5"
    # - timestamp : pd.DatetimeIndex
    # - lat: np.ndarray, np.float64
    # - lon: np.ndarray, np.float64
    #
    # Measurement units will be included via pint-xarray. Internally,
    # this uses an enum class providing pint-compatible measurement units
    # for each wmoUnit in the observation series.
    #

    global unit_registry

    with GeoApi.client_scope(config or Configuration()) as api_instance:
        attrs: dict = {Const.LOCATION_REQUESTED: loc}

        thx = api_instance.executor
        if isinstance(loc, str):
            match_loc = api_instance.geocode_location(loc)
            match_coords = match_loc.latitude, match_loc.longitude
            attrs[Const.LOCATION_MATCH] = match_loc.address
            attrs[Const.LOCATION_COORDS] = match_coords
            point_response = api_instance.point(match_coords)
        else:
            match_coords = loc
            attrs[Const.LOCATION_COORDS] = loc
            point_response = api_instance.point(loc)


        props = point_response.properties
        gid = props.grid_id
        grid_x = props.grid_x
        grid_y = props.grid_y
        print("-- using grid location: %s/%s,%s" % (gid, grid_x, grid_y))
        stations_response = api_instance.gridpoint_stations(
            wfo=gid, x=grid_x, y=grid_y)

        stations_id = tuple(map(lambda s: sys.intern(s.properties.station_identifier), stations_response.features))
        stations_id_tuple = stations_id
        station_offsets = {cc: offset for offset, cc in enumerate(stations_id)}
        stations_id = np.array(stations_id, "U5")
        n_stations = stations_id.size

        string_fields = set()
        timestamps = np.full(n_stations, "NaT", "datetime64[s]")
        data = {Const.TIMESTAMP: timestamps}

        for k, v in OBSV_PROPERTY_FIELDS.items():
            if k in OBSV_INDEX_FIELDS:
                continue
            tc = v.interface.interface_class
            if tc is QuantitativeValue:
                data[k] = np.full(n_stations, np.nan, np.float64)
            elif tc is str:
                data[k] = np.full(n_stations, EMPTY_STR, np.object_)
                string_fields.add(k)
            elif isinstance(tc, type) and (issubclass(tc, ApiObject) or issubclass(tc, list)) and netcdf_compat:
                continue
            else:
                data[k] = np.full(n_stations, np.nan, np.object_)

        futures: dict[str, cf.Future[ObservationGeoJson]] = dict()

        # dipsatching the observation requests within separate threads
        lock = RLock()
        unit_map = dict()
        station_names = [EMPTY_STR] * n_stations
        station_lat = np.full(n_stations, np.nan, np.float64)
        station_lon = np.full(n_stations, np.nan, np.float64)
        for station in stations_response.features:
            sid = sys.intern(station.properties.station_identifier)
            soffset = station_offsets[sid]
            station_names[soffset] = station.properties.name
            lon, lat = station.geometry.coordinates
            station_lat[soffset] = lat
            station_lon[soffset] = lon
            future = thx.submit(api_instance.station_observation_latest, station_id=sid)
            cb = partial(observation_callback, sid, soffset, unit_map, lock, data)
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

        # construct an Xarray Dataset from the observation series

        tz = data.pop(Const.TZ, UTC)
        data.pop(Const.TIMESTAMP)

        if not netcdf_compat:
            index = pd.MultiIndex.from_arrays(
                (stations_id, timestamps, station_lat, station_lon),
                names=(Const.STATION_ID, Const.TIMESTAMP, Const.LAT, Const.LON)
                )


        # calculate the relative_distance series
        #
        # - application: relational sorting for the observation series,
        #   in relation to the coordinates denoted to the function
        #
        # - known limitation: no units for distance
        point_vals = np.fromiter(map(shapely.Point, zip(station_lat, station_lon)), "O", n_stations)
        distance = np.fromiter(map(partial(shapely.distance, shapely.Point(match_coords)), point_vals),
                               np.float64, n_stations)

        vars = {
            Const.RELATIVE_DISTANCE: (
                [Const.INDEX], distance, {
                    Const.RELATIVE_TO: match_coords,
                    Const.METRIC: (str(Const.LAT), str(Const.LON))
                    })
        }


        if netcdf_compat:
            # index all data on station ID
            coords = {
                Const.INDEX: ([Const.INDEX], stations_id),
                Const.TIMESTAMP: ([Const.INDEX], timestamps, {Const.TZ: str(tz)}),
                Const.LAT: ([Const.INDEX], station_lat),
                Const.LON: ([Const.INDEX], station_lon)
            }
        else:
            # create coordinates for the multi-index
            coords = xr.Coordinates.from_pandas_multiindex(index, Const.INDEX)
            coords[Const.TIMESTAMP].attrs[Const.TZ]=str(tz)

        # supplemental coordinate data
        coords.update({
            Const.STATION_NAME: ([Const.INDEX], np.array(station_names)),
        })
        if not netcdf_compat:
            # include the series of Point objects in coords
            coords[Const.POINT] = ([Const.INDEX], point_vals)

        # initialize the attribute map for the resulting dataset
        attrs.update({
            Const.TZ: str(tz),
            Const.WFO: gid,
            Const.GRID_X: grid_x,
            Const.GRID_Y: grid_y,
        })

        if not netcdf_compat:
            attrs.update({
                Const.SOURCE_UNITS: unit_map,
                Const.STATION_NAMES: dict(zip(stations_id_tuple, station_names)),
                Const.POINT_DATA: point_response,
                Const.STATION_DATA: {sys.intern(stn.properties.station_identifier): stn for stn in stations_response.features},
            })

        coord_names = [Const.INDEX]

        other = data.pop(Const.NOT_FOUND, None)
        if other:
            attrs[Const.NOT_FOUND] = tuple(other)
        other = data.pop(Const.ERRORS, None)
        if other:
            attrs[Const.ERRORS] = other

        for name, values in data.items():
            if is_nan_all(values) or not any(values):
                continue
            try:
                name = sys.intern(name)
            except TypeError:
                name = sys.intern(str(name))
            unit = unit_map.get(name, None)
            if unit:
                mattrs = {Const.UNITS: unit}
            else:
                mattrs = EMPTY_MAP
            if name in string_fields:
                # convert the dtype from np.object_ to a minimum "U" type
                dt = np.min_scalar_type(tuple(values))
                values = values.astype(dt)
            vars[name] = (coord_names, values, mattrs)

        return xr.Dataset(vars, coords, attrs).sortby(Const.RELATIVE_DISTANCE).pint.quantify()


if __name__ == "__main__":
    obsv = latest_observations("Fargo, ND")

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
