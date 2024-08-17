"""API response object."""

from typing import (
    Any, Optional, Generic, Mapping, TypeVar, Never
)
from pynwsdata.api_object import ApiObject, ApiField

T = TypeVar("T", bound=ApiObject)


class ApiResponse(ApiObject, Generic[T]):
    """
    API response object
    """
    status_code: int = ApiField(description="""HTTP status code""")
    headers: Optional[Mapping[str, str]] = ApiField(
        None, description="""HTTP headers""")
    data: T = ApiField(description="""Deserialized data given the data type""")
    raw_data: bytes = ApiField(description="""Raw data (HTTP response body)""")

    @classmethod
    def from_json_map(cls, data: dict[str, Any]) -> Never:
        raise ValueError(
            "dictionary transform not supported for this type", cls)

    def to_json_map(self) -> Never:
        raise ValueError(
            "dictionary transform not supported for this type", self.__class__)
