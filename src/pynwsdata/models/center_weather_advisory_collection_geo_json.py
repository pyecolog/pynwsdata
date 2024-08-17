

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.center_weather_advisory_collection_geo_json_all_of_features import CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures
from pynwsdata.models.json_ld_context import JsonLdContext
from typing import Optional
from typing_extensions import Self


class CenterWeatherAdvisoryCollectionGeoJson(ApiObject):
    """
    CenterWeatherAdvisoryCollectionGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    type: str
    features: list[CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures]

