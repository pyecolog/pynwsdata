
import io
from typing import  TYPE_CHECKING,Any, Optional, Union, TypeAlias, TypeVar
from warnings import warn

import httpcore

from pynwsdata.configuration import Configuration

RESTResponseType: TypeAlias = httpcore.Response


T = TypeVar("T")


class RequestInfo(object):
    # temporary request storage for redirect handling
    __slots__  = "__weakref__", "method", "url", "headers", "body"
    if TYPE_CHECKING:
        url: str
        method: str
        headers: Optional[dict[str, str]]
        body: Optional[str]

    def __init__(self, method: str, url: str, headers: Optional[dict[str, str]], body: Optional[str]) -> None:
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body



class RESTResponse(io.IOBase): # IOBase ?

    if TYPE_CHECKING:
        response: RESTResponseType
        status: int
        data: Optional[bytes]
        # values for redirect handling
        request_info: RequestInfo

    def __init__(self, resp: RESTResponseType, request_info: RequestInfo):
        self.response = resp
        self.status = resp.status
        self.data = None
        # values for redirect handling
        self.request_info = request_info

    def read(self) -> bytes:
        if self.data is None:
            self.data = self.response.read()
        return self.data

    def get_headers(self) -> list[tuple[bytes, bytes]]:
        """Returns the response headers."""
        return self.response.headers

    def get_header(self, name: Union[str, bytes], default: T = None) -> Union[bytes, T]:
        """Returns a given response header."""
        if isinstance(name, str):
            name = name.encode()
        for hname, hvalue in self.response.headers:
            if hname == name:
                return hvalue
        return default


class RESTClientObject:
    __slots__ = "__weakref__", "pool_manager", "proxy", "_extensions"

    if TYPE_CHECKING:
        pool_manager: httpcore.ConnectionPool
        proxy: Optional[httpcore.HTTPProxy]

    def __init__(self, config: Configuration) -> None:

        # maxsize is number of requests to host that are allowed in parallel
        maxsize = config.connection_pool_maxsize

        ssl_context = config.get_ssl_context()

        self.pool_manager = httpcore.ConnectionPool(
            http2=True,
            max_connections=maxsize,
            retries=config.retries,
            ssl_context=ssl_context,
        )

        proxy = config.proxy
        if isinstance(proxy, str):
            self.proxy = httpcore.HTTPProxy(proxy)
        elif isinstance(proxy, httpcore.HTTPProxy):
            self.proxy = proxy
        else:
            if proxy:
                warn(UserWarning("Unrecognized proxy", proxy), stacklevel=2)
            self.proxy = None

        # httpcore connection timeout
        timeout = config.timeout
        self._extensions = {"timeout": {"pool": timeout}}

    def close(self):
        self.pool_manager.close()

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[dict[str, str]]=None,
        body=None,
    ):
        """Execute request

        :param method: http request method
        :param url: http request url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        headers = headers or {}
        # url already contains the URL query string

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        args = {
            "method": method,
            "url": url,
            "extensions": self._extensions,
            "headers": headers
        }

        if self.proxy:
            args["proxy"] = self.proxy

        pool_manager = self.pool_manager

        request_info = RequestInfo(method, url, headers, body)

        r = pool_manager.request(**args)

        return RESTResponse(r, request_info)
