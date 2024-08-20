
from pynwsdata.configuration import Configuration
from pynwsdata.api_client import ApiClient
from pynwsdata.api.geo_api import GeoApi
from pynwsdata.exceptions import ApiException
from typing import Union

configuration = Configuration(
    # host = "https://api.weather.gov"
)

ApiClient.set_verbose_logging()

def latest_observations(loc: Union[str, tuple[int, int]]):
    global configuration
    with ApiClient(configuration) as client:
        api_instance = GeoApi(client)
        # FIXME cache all point => (WFO, X, Y)
        if isinstance(loc, str):
            point = api_instance.geocode_point(loc)
        else:
            point = api_instance.point(loc)
        props = point.properties
        gid =  props.grid_id
        grid_x = props.grid_x
        grid_y = props.grid_y
        print("-- using grid location: %s/%s,%s" % (gid, grid_x, grid_y))
        stations =  api_instance.gridpoint_stations(wfo = gid, x=grid_x, y=grid_y, limit=1)
        observations = dict()
        for station in stations.features:
            id = station.properties.station_identifier
            try:
                obsv = api_instance.station_observation_latest(station_id=id)
            except ApiException as exc:
                if exc.status == 404:
                    try:
                        nf = observations["not_found"]
                    except KeyError:
                        observations["not_found"] = [id]
                    else:
                        nf.append(id)
                else:
                    try:
                        err = observations["errors"]
                    except KeyError:
                        observations["errors"] = [exc]
                    else:
                        err.append(exc)
            else:
                observations[id] = obsv
        return observations

if __name__ == "__main__":
    obsv = latest_observations("Muskogee, OK")
