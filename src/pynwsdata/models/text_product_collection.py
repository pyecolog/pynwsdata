

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.text_product import TextProduct
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class TextProductCollection(ApiObject):
    """
    TextProductCollection
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    graph: Optional[list[TextProduct]] = ApiField(default=None, alias="@graph")


