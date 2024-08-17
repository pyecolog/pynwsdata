

from typing import Any, ClassVar
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.office_headline import OfficeHeadline
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class OfficeHeadlineCollection(ApiObject):
    """
    OfficeHeadlineCollection
    """

    context: JsonLdContext = ApiField(alias="@context")
    graph: list[OfficeHeadline] = ApiField(alias="@graph")


