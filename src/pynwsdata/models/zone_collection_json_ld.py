

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.zone import Zone
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ZoneCollectionJsonLd(ApiObject):
    """
    ZoneCollectionJsonLd
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    graph: Optional[list[Zone]] = ApiField(default=None, alias="@graph")


