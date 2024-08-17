

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.sigmet import Sigmet
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class SigmetGeoJson(ApiObject):
    """
    SigmetGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    id: Optional[str] = None
    type: str
    geometry: Optional[GeoJsonGeometry]
    properties: Sigmet

