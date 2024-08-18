
from geopy.geocoders import Nominatim
from typing import Optional
from geopy.adapters import (
    BaseAdapter
)
from pynwsdata.api_client import USER_AGENT
from pynwsdata.configuration import Configuration
from pynwsdata.geo.geopy_httpcore import HTTPCoreAdapter


def get_geocoder(configuration: Optional[Configuration] = None, adapter_factory: type[BaseAdapter] = HTTPCoreAdapter,
                 **kw) -> Nominatim:
    config = configuration or Configuration()
    try:
        ssl_context = kw['ssl_context']
    except KeyError:
        ssl_context = config.get_ssl_context()
    return Nominatim(user_agent=USER_AGENT, ssl_context=ssl_context, adapter_factory=adapter_factory, **kw)


if __name__ == "__main__":
    #
    # ad hoc tests
    #

    import asyncio as aio
    from geopy import Location
    from pynwsdata.geo.geopy_httpcore import AsyncHTTPCoreAdapter


    def get_test_loc_sync(loc: str, **kw) -> Optional[Location]:
        with get_geocoder() as gco:
            return gco.geocode(loc, **kw)


    async def get_test_loc_async(loc: str, **kw) -> Optional[Location]:
        async with get_geocoder(adapter_factory=AsyncHTTPCoreAdapter) as gco:
            return await gco.geocode(loc, **kw)


    # test for city with domain 1, feature, city without domain 1, domain 1, continent
    positive_tests: tuple[str, ...] = "Yuma, AZ", "Monterey Bay, CA", "Seoul", "Fiji", "Antarctica"

    # test for fictional location, empty location, punctuation in geocode query
    negative_tests: tuple[str, ...] = "Shiretonville, Northumbershire", "", "..."


    def run_tests_sync():
        for name in positive_tests:
            loc = get_test_loc_sync(name)
            assert isinstance(loc, Location)

        for name in negative_tests:
            loc = get_test_loc_sync(name)
            assert loc is None

    async def run_tests_async():
        for name in positive_tests:
            loc = await get_test_loc_async(name)
            assert isinstance(loc, Location)

        for name in negative_tests:
            loc = await get_test_loc_async(name)
            assert loc is None


    run_tests_sync()

    aio.run(run_tests_async())
