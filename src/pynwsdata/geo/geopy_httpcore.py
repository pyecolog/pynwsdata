"""GeoPy Geocoder Adapters for HTTPCore"""

from abc import abstractmethod
import os
import ujson
from collections.abc import Mapping
import ssl
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Generic, Optional, TypeVar, Union
from httpcore import (
    ConnectionPool,  HTTPProxy,
    AsyncConnectionPool, AsyncHTTPProxy,
    Response
)
from geopy.adapters import (
    AdapterHTTPError, BaseAdapter,
    BaseAsyncAdapter, BaseSyncAdapter
)


Tp = TypeVar("Tp", bound=Union[ConnectionPool, AsyncConnectionPool])

PROXY_MAP_PRECEDENCE: tuple[str, ...] = (
    "socks", "https", "http"
)
PROXY_ENV_PRECEDENCE: tuple[str, ...] = (
    "SOCKS_PROXY", "HTTPS_PROXY", "HTTP_PROXY"
)
EMPTY_ARGS: Mapping[str, Any] = MappingProxyType(dict())


class HTTPCoreBaseAdapter(BaseAdapter, Generic[Tp]):
    if TYPE_CHECKING:
        connection_pool: Tp

    def get_primary_proxy(self, proxies: Optional[Mapping[str, str]]) -> Optional[str]:
        #
        # HTTPCore supports exactly one proxy URL in the proxy connection pool
        #
        # In effect, this will use any SOCKS proxy, then any HTTPS proxy, then any
        # HTTP proxy else returning None.
        #
        # The test for proxy URLs will begin with the provided `proxies` value,
        # then testing for variables in os.environ
        #
        # Caveats:
        #
        # - Each test for a `proxies' map will assume case sensitive keys
        #   in lower case, e.g "socks", "https", "http"
        #
        # - Each test for an environment variable in os.environ will be performed
        #   without case sensitivity, using the value of the first matching variable
        #   in "SOCKS_PROXY","HTTPS_PROXY", "HTTP_PROXY"
        #
        # - The `proxies` map may contain None values, in effect specifying "No proxy,"
        #   thus overriding any values defined in os.environ
        #
        # - Any SOCKS proxy URL should generally be prefixed with a corresponding SOCKS
        #   URL scheme,  e.g "socks5://...", "socks4://..."
        #
        # - SOCKS support entails an additional dependency: httpcore[socks]
        #
        # Known Limitations:
        #
        #  FIXME Proxy support has not been tested (SOCKS proxy, HTTPS proxy, HTTP proxy)
        #
        proxy = None
        if proxies:
            for k in PROXY_MAP_PRECEDENCE:
                try:
                    proxy = proxies[k]
                except KeyError:
                    pass
                else:
                    return proxy
        for k in PROXY_ENV_PRECEDENCE:
            try:
                proxy = next(ve for ke, ve in os.environ.items()
                             if ke.upper() == k)
            except StopIteration:
                pass
            else:
                return proxy
        return None

    def get_timeout_args(self, timeout: Union[int, float, None]) -> Mapping[str, Mapping[str, Mapping[str, Union[int, float]]]]:
        if timeout:
            # return {karg: kvalue} for specifying a connection timeout
            # to an HTTPCore Request
            return {"extensions": {"timeout": {"pool": timeout}}}
        else:
            return EMPTY_ARGS

    @abstractmethod
    def create_connection_pool(self, proxies: Optional[dict[str, str]], ssl_context: ssl.SSLContext) -> Tp:
        raise NotImplementedError(self.create_connection_pool)


class HTTPCoreAdapter(HTTPCoreBaseAdapter[ConnectionPool], BaseSyncAdapter):
    # synchronous adapter for HTTPCore support in GeoPy
    if TYPE_CHECKING:
        connection_pool: ConnectionPool

    def __init__(self, *, proxies: Optional[dict[str, str]], ssl_context: ssl.SSLContext):
        super().__init__(proxies=proxies, ssl_context=ssl_context)
        self.connection_pool = self.create_connection_pool(
            proxies, ssl_context)

    def create_connection_pool(self, proxies: Optional[dict[str, str]], ssl_context: ssl.SSLContext) -> ConnectionPool:
        proxy = self.get_primary_proxy(proxies)
        if proxy:
            return HTTPProxy(proxy, ssl_context=ssl_context, http2=True)
        else:
            return ConnectionPool(ssl_context=ssl_context, http2=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection_pool.close()
        return super().__exit__(exc_type, exc_val, exc_tb)

    def get_response(self, url, timeout, headers) -> bytes:
        args = self.get_timeout_args(timeout)
        response: Response = self.connection_pool.request(
            "GET", url, headers=headers, **args)
        # FIXME not implemented / not tested: handle redirects
        status = response.status
        data = response.read()
        if status == 200:
            # FIXME not tested with many endpoints
            return data
        else:
            raise AdapterHTTPError(
                status_code=status, headers=response.headers, text=data.decode())

    def get_json(self, url, *, timeout, headers):
        data = self.get_response(url, timeout, headers)
        return ujson.loads(data)

    def get_text(self, url, *, timeout, headers):
        data = self.get_response(url, timeout, headers)
        # FIXME this assumes UTF-8 encoding in the response
        return data.decode()


class AsyncHTTPCoreAdapter(HTTPCoreBaseAdapter[AsyncConnectionPool], BaseAsyncAdapter):
    # asynchronous adapter for HTTPCore support in GeoPy

    if TYPE_CHECKING:
        connection_pool: AsyncConnectionPool
        proxies: Optional[dict[str, str]]
        ssl_context: ssl.SSLContext

    def __init__(self, *, proxies: Optional[dict[str, str]], ssl_context: ssl.SSLContext):
        super().__init__(proxies=proxies, ssl_context=ssl_context)
        # store initargs for the connection pool
        self.proxies = proxies
        self.ssl_context = ssl_context

    def create_connection_pool(self, proxies: Optional[dict[str, str]], ssl_context: ssl.SSLContext) -> ConnectionPool:
        proxy = self.get_primary_proxy(proxies)
        if proxy:
            return AsyncHTTPProxy(proxy, ssl_context=ssl_context, http2=True)
        else:
            return AsyncConnectionPool(ssl_context=ssl_context, http2=True)

    async def __aenter__(self):
        # create the connection pool in the running loop
        self.connection_pool = self.create_connection_pool(
            self.proxies, self.ssl_context)
        return await super().__aenter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection_pool.aclose()
        return await super().__aexit__(exc_type, exc_val, exc_tb)

    async def get_response(self, url, timeout, headers) -> bytes:
        args = self.get_timeout_args(timeout)
        response: Response = await self.connection_pool.request("GET", url, headers=headers, **args)
        # FIXME not implemented / not tested: handle redirects
        status = response.status
        data = await response.aread()
        if status == 200:
            # FIXME not tested with many endpoints
            return data
        else:
            raise AdapterHTTPError(
                status_code=status, headers=response.headers, text=data.decode())

    async def get_json(self, url, *, timeout, headers):
        data = await self.get_response(url, timeout, headers)
        return ujson.loads(data)

    async def get_text(self, url, *, timeout, headers):
        data = await self.get_response(url, timeout, headers)
        # FIXME this assumes UTF-8 encoding in the response
        return data.decode()


# tests: see ./geo_nom.py
