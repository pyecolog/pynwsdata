
import pprint
import re  # noqa: F401

from pynwsdata.api_object import ApiObject, ApiField
from typing import Any, ClassVar, Optional
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.relative_location import RelativeLocation
from typing import Optional
from typing_extensions import Self

class RelativeLocationGeoJson(ApiObject):
    """
    RelativeLocationGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    id: Optional[str] = None
    type: str
    geometry: Optional[GeoJsonGeometry]
    properties: RelativeLocation

