

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.observation import Observation
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ObservationCollectionJsonLd(ApiObject):
    """
    ObservationCollectionJsonLd
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    graph: Optional[list[Observation]] = ApiField(default=None, alias="@graph")


