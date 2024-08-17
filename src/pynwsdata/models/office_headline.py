

from datetime import datetime
from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class OfficeHeadline(ApiObject):
    """
    OfficeHeadline
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    id: Optional[str] = ApiField(default=None, alias="@id")
    id: Optional[str] = None
    office: Optional[str] = None
    important: Optional[bool] = None
    issuance_time: Optional[datetime] = ApiField(default=None, alias="issuanceTime")
    link: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None


