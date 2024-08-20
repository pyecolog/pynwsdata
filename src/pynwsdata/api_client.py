
from pynwsdata.version import VERSION
from aenum import Enum
import datetime
from dateutil.parser import parse
import logging
import mimetypes
import os
import re
import sys
from urllib.parse import quote, urlparse
import ujson
from typing import TYPE_CHECKING, cast, Any, Optional, Union, Self

from pynwsdata.configuration import Configuration
from pynwsdata.api_object import (
    ApiObject, ApiType, EMPTY, PagedApiObject, ApiField
)
from pynwsdata.api_base import (
    ValueType, SeriesType
)
from pynwsdata.api_response import ApiResponse, T as ApiResponseT
from pynwsdata import rest
from pynwsdata.exceptions import (
    ApiValueError,
    ApiException,
)

RequestSerialized = tuple[str, str, dict[str, str], Optional[str], list[str]]

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections
REDIRECT_STATUS: frozenset[int] = frozenset((301, 302, 303, 307, 308))


APPLICATION: str = __package__ or __name__
USER_AGENT: str = "/".join((APPLICATION, VERSION,
                           sys.implementation.name, sys.version.split()[0]))


class ApiClient:
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    """


    if TYPE_CHECKING:
        configuration: Configuration
        default_headers: dict[str, str]
        cookie: Optional[str]
        user_agent: str

    def __init__(
        self,
        configuration: Optional[Configuration] = None,
        header_name: Optional[str] = None,
        header_value: Optional[str] = None,
        cookie: Optional[str] = None
    ) -> None:
        # use default configuration if none is provided
        if configuration is None:
            configuration = Configuration.get_default()
        self.configuration = configuration

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        self.user_agent = USER_AGENT

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self.rest_client.close()

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    @property
    def logger(self) -> logging.Logger:
        return self.configuration.logger

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    _default = None

    @classmethod
    def get_default(cls) -> Self:
        """Return new instance of ApiClient.

        This method returns newly created, based on default constructor,
        object of ApiClient class or returns a copy of default
        ApiClient.

        :return: The ApiClient object.
        """
        if cls._default is None:
            cls._default = ApiClient()
        return cls._default

    @classmethod
    def set_default(cls, default):
        """Set default instance of ApiClient.

        It stores default ApiClient.

        :param default: object of ApiClient.
        """
        cls._default = default

    @classmethod
    def set_verbose_logging(cls):
        root_logger = logging.getLogger(None)
        if not root_logger.handlers:
            hdlr = logging.StreamHandler(sys.stderr)
            hdlr.setFormatter(
                logging.Formatter(
                    "[%(process)d %(asctime)s.%(msecs).03d %(thread)x] [%(name)s] [%(levelname)s] %(message)s",
                    datefmt="%m.%d %X"
                ))
            root_logger.addHandler(hdlr)
        root_logger.setLevel(logging.INFO)

    def param_serialize(
        self,
        method,
        resource_path,
        path_params=None,
        query_params=None,
        header_params=None,
        body=None,
        post_params=None,
        files=None, auth_settings=None,
        collection_formats=None,
        _host=None,
        _request_auth=None
    ) -> RequestSerialized:
        """Builds the HTTP request params needed by the request.
        :param method: Method to call.
        :param resource_path: Path to method endpoint.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param files dict: key -> filename, value -> filepath,
            for `multipart/form-data`.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :return: tuple of form (path, http_method, query_params, header_params,
            body, post_params, files)
        """

        config = self.configuration

        # set request headers, including User-Agent
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(
                self.parameters_to_tuples(header_params, collection_formats)
            )

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(
                path_params,
                collection_formats
            )
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(
                post_params,
                collection_formats
            )
            if files:
                post_params.extend(self.files_parameters(files))

        # auth setting
        self.update_params_for_auth(
            header_params,
            query_params,
            auth_settings,
            resource_path,
            method,
            body,
            request_auth=_request_auth
        )

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # request url
        if _host is None or config.ignore_operation_servers:
            url = "".join((config.host, resource_path))
        else:
            # use server/host defined in path or operation instead
            url = "".join((_host, resource_path))

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            url_query = self.parameters_to_url_query(
                query_params,
                collection_formats
            )
            url = "?".join((url, url_query))

        return method, url, header_params, body, post_params

    def call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        _request_timeout=None
    ) -> rest.RESTResponse:
        """Makes the HTTP request (synchronous)
        :param method: Method to call.
        :param url: Path to method endpoint.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param _request_timeout: timeout setting for this request.
        :return: RESTResponse
        """

        try:
            # perform request and return response
            response_data = self.rest_client.request(
                method, url,
                headers=header_params,
                body=body,
            )

        except ApiException as e:
            raise e

        return response_data

    def response_deserialize(
        self,
        response_data: rest.RESTResponse,
        response_types_map: dict[int, type[ApiResponseT]]
    ) -> ApiResponse[ApiResponseT]:
        """Deserializes response into an object.
        :param response_data: RESTResponse object to be deserialized.
        :param response_types_map: dict of response types.
        :return: ApiResponse
        """

        status = response_data.status
        if status in REDIRECT_STATUS:
            # handle redirect
            info = response_data.request_info
            req_mtd = info.method
            req_hdrs = info.headers
            req_body = info.body
            dst_loc = response_data.get_header(b'location')
            dst_base = urlparse(info.url)[:2]
            dst_url = "%s://%s%s" % (*dst_base, dst_loc.decode())
            if __debug__:
                # server response message may include an explanation of the redirect
                config = self.configuration
                msg = response_data.read().decode()
                config.logger.info("redirect %d %s => %s %s",
                                   status, info.url, dst_url, msg)
            nxt = self.rest_client.request(
                req_mtd, dst_url, req_hdrs, req_body)
            return self.response_deserialize(nxt, response_types_map)

        response_type: Optional[type[ApiObject]] = response_types_map.get(
            response_data.status, None)

        data = response_data.read()

        if response_type is None:
            # assuming an error response
            raise ApiException.from_response(
                http_resp=response_data,
                body=data.decode()
            )

        # deserialize response data
        response_text = None
        return_data = None
        try:
            match = None
            content_type = response_data.get_header(b'content-type').decode()
            if content_type is not None:
                match = re.search(
                    r"charset=([a-zA-Z\-\d]+)[\s;]?", content_type)
            encoding = match.group(1) if match else "utf-8"
            response_text = data.decode(encoding)
            return_data: ApiObject = self.deserialize(
                response_text, response_type, content_type)
            if isinstance(return_data, PagedApiObject):
                pagination = return_data.pagination
                if pagination:
                    next_url = pagination.next
                    if next_url:
                        rcls = return_data.__class__
                        jf: ApiField = rcls.join_field
                        ownv: list = jf.__get__(return_data, rcls)
                        #
                        # continue only if this request's join_field value was not empty,
                        # otherwise, the paged request series might continue indefinitely.
                        #
                        # subsequent responses may provide a generally equivalent next_url
                        # such that may differ only in  the 'cursor' query value, compared
                        # to the previous request URL in the paged series
                        #
                        # - seen with the station_observation_latest() endpoint
                        #   @ observation station collection
                        #
                        # - tested (preliminary) with the alert endpoint
                        #
                        if ownv:
                            if __debug__:
                                self.configuration.logger.info(
                                    "request paged %s => %s", response_data.request_info.url, next_url)
                            mtd = response_data.request_info.method
                            hdrs = response_data.request_info.headers

                            next_data = self.rest_client.request(
                                mtd, next_url, hdrs)
                            next_re: ApiResponse = self.response_deserialize(next_data, {
                                                                             200: rcls})
                            next_o = next_re.data

                            nxtv: list = jf.__get__(next_o, rcls)
                            if nxtv:
                                ownv.extend(nxtv)
                    if not __debug__:
                        del return_data.pagination
        finally:
            if not 200 <= status <= 308:
                raise ApiException.from_response(
                    http_resp=response_data,
                    body=response_text,
                    data=return_data,
                )

        return ApiResponse(
            status_code=response_data.status,
            data=return_data,
            headers=response_data.get_headers(),
            raw_data=response_data.data
        )

    def sanitize_for_serialization(self, obj):
        """Builds a JSON POST object.

        If obj is None, return None.
        If obj is SecretStr, return obj.get_secret_value()
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.

        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if obj is None:
            return None
        elif isinstance(obj, Enum):
            return obj.value
        # elif isinstance(obj, SecretStr):
        #     return obj.get_secret_value()
        elif isinstance(obj, ValueType):
            return obj
        elif isinstance(obj, SeriesType):
            return obj.__class__(self.sanitize_for_serialization(sub_obj) for sub_obj in obj)
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()

        elif isinstance(obj, dict):
            obj_dict = obj
        else:
            assert isinstance(obj, ApiObject)
            obj_dict = dict()
            cls = cast(ApiType, obj.__class__)
            for name, field in cls.fields.items():
                try:
                    val = field.__get__(obj, cls)
                except AttributeError:
                    continue
                if val is not EMPTY:
                    obj_dict[name] = val

        return {
            key: self.sanitize_for_serialization(val)
            for key, val in obj_dict.items()
        }

    def deserialize(self, response_text: str, cls: type[ApiObject], content_type: Optional[str]):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: class literal for
            deserialized object, or string of class name.
        :param content_type: content type of response.

        :return: deserialized object.
        """

        # load data from client response
        if content_type is None:
            try:
                data = ujson.loads(response_text, precise_float=True)
            except ValueError:
                data = response_text
        elif content_type.endswith("json"):
            if response_text == "":
                data = ""
            else:
                data = ujson.loads(response_text)
        elif content_type.startswith("text/plain"):
            data = response_text
        else:
            raise ApiException(
                status=0,
                reason="Unsupported content type: {0}".format(content_type)
            )

        return cls.model_interface.from_json_parsed(data)

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params: list[tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    def parameters_to_url_query(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: URL query string (e.g. a=Hello%20World&b=123)
        """
        new_params: list[tuple[str, str]] = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:
            if isinstance(v, bool):
                v = str(v).lower()
            if isinstance(v, (int, float)):
                v = str(v)
            if isinstance(v, dict):
                v = ujson.dumps(v, ensure_ascii=False)

            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, str(value)) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(quote(str(value)) for value in v))
                    )
            else:
                new_params.append((k, quote(str(v))))

        return "&".join(["=".join(map(str, item)) for item in new_params])

    def files_parameters(self, files: dict[str, Union[str, bytes]]):
        """Builds form parameters.

        :param files: File parameters.
        :return: Form parameters with files.
        """
        params = []
        for k, v in files.items():
            if isinstance(v, str):
                with open(v, 'rb') as f:
                    filename = os.path.basename(f.name)
                    filedata = f.read()
            elif isinstance(v, bytes):
                filename = k
                filedata = v
            else:
                raise ValueError("Unsupported file value")
            mimetype = (
                mimetypes.guess_type(filename)[0]
                or 'application/octet-stream'
            )
            params.append(
                tuple([k, tuple([filename, filedata, mimetype])])
            )
        return params

    def select_header_accept(self, accepts: list[str]) -> Optional[str]:
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: list of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        for accept in accepts:
            if re.search('json', accept, re.IGNORECASE):
                return accept

        return accepts[0]

    def select_header_content_type(self, content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: list of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        for content_type in content_types:
            if re.search('json', content_type, re.IGNORECASE):
                return content_type

        return content_types[0]

    def update_params_for_auth(
        self,
        headers,
        queries,
        auth_settings,
        resource_path,
        method,
        body,
        request_auth=None
    ) -> None:
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param request_auth: if set, the provided settings will
                             override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auth:
            self._apply_auth_params(
                headers,
                queries,
                resource_path,
                method,
                body,
                request_auth
            )
        else:
            for auth in auth_settings:
                auth_setting = self.configuration.auth_settings().get(auth)
                if auth_setting:
                    self._apply_auth_params(
                        headers,
                        queries,
                        resource_path,
                        method,
                        body,
                        auth_setting
                    )

    def _apply_auth_params(
        self,
        headers,
        queries,
        resource_path,
        method,
        body,
        auth_setting
    ) -> None:
        """Updates the request parameters based on a single auth_setting

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :resource_path: A string representation of the HTTP request resource path.
        :method: A string representation of the HTTP request method.
        :body: A object representing the body of the HTTP request.
        The object type is the return value of sanitize_for_serialization().
        :param auth_setting: auth settings for the endpoint
        """
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )

    def __deserialize_primitive(self, data, klass):
        """Deserializes string to primitive type.

        :param data: str.
        :param klass: class literal.

        :return: int, long, float, str, bool.
        """
        try:
            return klass(data)
        except UnicodeEncodeError:
            return str(data)
        except TypeError:
            return data

    def __deserialize_object(self, value):
        """Return an original value.

        :return: object.
        """
        return value

    def __deserialize_date(self, string):
        """Deserializes string to date.

        :param string: str.
        :return: date.
        """
        try:
            return parse(string).date()
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason="Failed to parse `{0}` as date object".format(string)
            )

    def __deserialize_datetime(self, string):
        """Deserializes string to datetime.

        The string should be in iso8601 datetime format.

        :param string: str.
        :return: datetime.
        """
        try:
            return parse(string)
        except ImportError:
            return string
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as datetime object"
                    .format(string)
                )
            )

    def __deserialize_enum(self, data, klass):
        """Deserializes primitive type to enum.

        :param data: primitive type.
        :param klass: class literal.
        :return: enum value.
        """
        try:
            return klass(data)
        except ValueError:
            raise rest.ApiException(
                status=0,
                reason=(
                    "Failed to parse `{0}` as `{1}`"
                    .format(data, klass)
                )
            )

    def __deserialize_model(self, data: Union[dict[str, Any], list], cls: type[ApiObject]):
        """Deserializes list or dict to model.

        :param data: dict, list.
        :param klass: class literal.
        :return: model object.
        """

        return cls.model_interface.from_json_parsed(data)
