

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry
from pynwsdata.models.json_ld_context import JsonLdContext
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class GeoJsonFeature(ApiObject):
    """
    A GeoJSON feature. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    id: Optional[str] = None
    type: str
    geometry: Optional[GeoJsonGeometry]
    properties: dict[str, Any]

