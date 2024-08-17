

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.sigmet_geo_json import SigmetGeoJson
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class SigmetCollectionGeoJson(ApiObject):
    """
    SigmetCollectionGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    type: str
    features: list[SigmetGeoJson]

