

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.zone_collection_geo_json_all_of_features import ZoneCollectionGeoJsonAllOfFeatures
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ZoneCollectionGeoJson(ApiObject):
    """
    ZoneCollectionGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    type: str
    features: list[ZoneCollectionGeoJsonAllOfFeatures]

