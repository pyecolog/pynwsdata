

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class TextProductLocationCollection(ApiObject):
    """
    TextProductLocationCollection
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    locations: Optional[dict[str, Optional[str]]] = None


