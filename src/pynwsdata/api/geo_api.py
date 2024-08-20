"""Utility methods for DefaultApi"""

from geopy import Location
from typing import Optional

from pynwsdata.api.default_api import DefaultApi, format_coord
from pynwsdata.geo.geo_nom import Nominatim, get_geocoder
from pynwsdata.geo.geopy_httpcore import HTTPCoreAdapter
from pynwsdata.models.point_geo_json import PointGeoJson


class GeoApi(DefaultApi):
    def geocode_coords(self, name: str, coder: Optional[Nominatim] = None) -> tuple[float, float]:
        # return latitude, longitude for a geocoded station
        #
        # known limitations:
        #
        # - This function will return the coordinates for the first matching location,
        #   using the Nominatim Web API. This does not test whether the location is
        #   within any coverage area for the NWS Web API.
        #
        if coder is None:
            config = self.api_client.configuration
            coder = get_geocoder(config, HTTPCoreAdapter)
        loc: Optional[Location] = coder.geocode(name)
        if loc is None:
            raise ValueError("Location not found", name)
        # print("-- DEBUG %s => (%s, %s)" % (name, format_coord(loc.latitude), format_coord(loc.longitude)))
        return loc.latitude, loc.longitude

    def geocode_point(self, name: str, coder: Optional[Nominatim] = None) -> PointGeoJson:
        return self.point(self.geocode_coords(name))

    def geocode_observations_latest(
        self, name: str, coder: Optional[Nominatim] = None): ...

    def geocode_observations_duration(
        self, name: str, start, end, limit, coder: Optional[Nominatim] = None): ...

    def geocode_forecast(
        self, name: str, coder: Optional[Nominatim] = None): ...


if __name__ == "__main__":
    #
    # ad hoc tests
    #
    from pynwsdata.api_client import ApiClient
    from pynwsdata.configuration import Configuration
    from pynwsdata.models.point_geo_json import PointGeoJson

    import logging
    import sys

    ApiClient.set_verbose_logging()


    def test_redir(config: Optional[Configuration] = None):
        # test redirect handling, using coordinates with trailing zeros
        #
        # after the initial request, the server can be expected
        # to respond with a redirect for repeating the request,
        # with trailing zeros removed from the provided coordinate
        # values
        #
        test_coords = "35.0110,-118.1903"
        with ApiClient(config) as api_client:
            api_client.logger.setLevel(logging.INFO)
            api_instance = GeoApi(api_client)
            point = api_instance.point(test_coords)
            assert isinstance(point, PointGeoJson)
            # GeoJSON uses the unconventional longitude, latitude order for coordinates
            geom = point.geometry
            assert repr(geom) == "<GeoJSONPoint (35.011, -118.1903)>"

    def test_point(loc: str, config: Optional[Configuration] = None):
        with ApiClient(config) as api_client:
            api_instance = GeoApi(api_client)
            limit = 10
            return api_instance.geocode_point(loc)

    test_redir()

    test_point("Mojave, CA")
