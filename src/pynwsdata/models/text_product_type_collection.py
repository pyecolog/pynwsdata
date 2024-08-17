

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.text_product_type_collection_graph_inner import TextProductTypeCollectionGraphInner
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class TextProductTypeCollection(ApiObject):
    """
    TextProductTypeCollection
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    graph: Optional[list[TextProductTypeCollectionGraphInner]] = ApiField(default=None, alias="@graph")


