

from typing import Any, ClassVar, Union
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from typing_extensions import Self


class ProblemDetail(ApiObject):
    """
    Detail about an error. This document conforms to RFC 7807 (Problem Details for HTTP APIs).
    """

    type: str = ApiField(description="""A URI reference (RFC 3986) that identifies the problem type. This is only an identifier and is not necessarily a resolvable URL. """)
    title: str = ApiField(description="""A short, human-readable summary of the problem type.""")
    status: Union[Annotated[float, ApiField(le=999, ge=100)], Annotated[int, ApiField(le=999, ge=100)]] = ApiField(description="""The HTTP status code (RFC 7231, Section 6) generated by the origin server for this occurrence of the problem. """)
    detail: str = ApiField(description="""A human-readable explanation specific to this occurrence of the problem.""")
    instance: str = ApiField(description="""A URI reference (RFC 3986) that identifies the specific occurrence of the problem. This is only an identifier and is not necessarily a resolvable URL. """)
    correlation_id: str = ApiField(description="""A unique identifier for the request, used for NWS debugging purposes. Please include this identifier with any correspondence to help us investigate your issue. """, alias="correlationId")
    additional_properties: dict[str, Any] = {}


