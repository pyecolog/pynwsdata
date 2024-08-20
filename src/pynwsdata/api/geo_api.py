"""Utility methods for DefaultApi"""

from contextlib import contextmanager
import concurrent.futures as cf
from geopy import Location
from geopy.geocoders import GeocoderNotFound
from collections.abc import Iterator
import logging
from typing import TYPE_CHECKING, Optional, Self

from pynwsdata.configuration import Configuration
from pynwsdata.api_client import ApiClient
from pynwsdata.api.default_api import DefaultApi, format_coord
from pynwsdata.geo.geo_nom import Nominatim, get_geocoder
from pynwsdata.geo.geopy_httpcore import HTTPCoreAdapter
from pynwsdata.models.point_geo_json import PointGeoJson


class GeoApi(DefaultApi):

    if TYPE_CHECKING:
        executor: cf.ThreadPoolExecutor

    @property
    def logger(self) -> logging.Logger:
        return self.api_client.configuration.logger

    def __init__(self, api_client: Optional[ApiClient]=None, *,
                 executor: cf.ThreadPoolExecutor) -> None:
        super().__init__(api_client)
        self.executor = executor

    @classmethod
    @contextmanager
    def client_scope(cls, config: Optional[Configuration] = None) -> Iterator[Self]:
        with ApiClient(config) as api_client:
            config = api_client.configuration
            with cf.ThreadPoolExecutor(max_workers=config.max_thread_workers,
                                       thread_name_prefix="api_") as xth:
                yield cls(api_client, executor = xth)

    def geocode_location(self, name: str,  coder: Optional[Nominatim] = None) -> Location:
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
        return loc

    def geocode_coords(self, name: str, coder: Optional[Nominatim] = None) -> tuple[float, float]:
        loc = self.geocode_location(name, coder)
        return loc.latitude, loc.longitude

    def geocode_point(self, name: str, coder: Optional[Nominatim] = None) -> PointGeoJson:
        return self.point(self.geocode_coords(name))

    def geocode_observations_latest(self, name: str, coder: Optional[Nominatim] = None):
        raise NotImplementedError

    def geocode_observations_duration(self, name: str, start, end, limit, coder: Optional[Nominatim] = None):
        raise NotImplementedError

    def geocode_forecast(self, name: str, coder: Optional[Nominatim] = None):
        raise NotImplementedError


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
        with GeoApi.client_scope() as api_instance:
            api_instance.logger.setLevel(logging.INFO)
            point = api_instance.point(test_coords)
            assert isinstance(point, PointGeoJson)
            # GeoJSON uses the unconventional longitude, latitude order for coordinates
            geom = point.geometry
            assert repr(geom) == "<GeoJSONPoint (35.011, -118.1903)>"

    def test_point(loc: str, config: Optional[Configuration] = None):
        # with ApiClient(config) as api_client:
        #     api_instance = GeoApi(api_client)

        with GeoApi.client_scope() as api_instance:
            return api_instance.geocode_point(loc)

    test_redir()

    test_point("Mojave, CA")
