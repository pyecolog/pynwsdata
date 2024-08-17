

from datetime import datetime
from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.alert import Alert
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.pagination_info import PaginationInfo
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class AlertCollectionJsonLd(ApiObject):
    """
    AlertCollectionJsonLd
    """

    title: Optional[str] = ApiField(default=None, description="""A title describing the alert collection""")
    updated: Optional[datetime] = ApiField(default=None, description="""The last time a change occurred to this collection""")
    pagination: Optional[PaginationInfo] = None
    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    graph: Optional[list[Alert]] = ApiField(default=None, alias="@graph")


