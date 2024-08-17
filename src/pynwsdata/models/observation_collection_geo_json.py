

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.observation_collection_geo_json_all_of_features import ObservationCollectionGeoJsonAllOfFeatures
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ObservationCollectionGeoJson(ApiObject):
    """
    ObservationCollectionGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    type: str
    features: list[ObservationCollectionGeoJsonAllOfFeatures]

