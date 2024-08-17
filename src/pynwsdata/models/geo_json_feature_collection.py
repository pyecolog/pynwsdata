

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.geo_json_feature import GeoJsonFeature
from pynwsdata.models.json_ld_context import JsonLdContext
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class GeoJsonFeatureCollection(ApiObject):
    """
    A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    type: str
    features: list[GeoJsonFeature]

