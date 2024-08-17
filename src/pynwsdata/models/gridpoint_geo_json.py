

from pynwsdata.api_object import ApiObject, ApiField
from typing import Any, ClassVar, Optional
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry
from pynwsdata.models.gridpoint import Gridpoint
from pynwsdata.models.json_ld_context import JsonLdContext
from typing import Optional
from typing_extensions import Self

class GridpointGeoJson(ApiObject):
    """
    GridpointGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    id: Optional[str] = None
    type: str
    geometry: Optional[GeoJsonGeometry]
    properties: Gridpoint

