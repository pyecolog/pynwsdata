
from pynwsdata.api_object import ApiField
from typing import Optional
from pynwsdata.models.point_relative_location import PointRelativeLocation
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.relative_location import RelativeLocation

class RelativeLocationGeoJson(PointRelativeLocation):
    """
    RelativeLocationGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    id: Optional[str] = None
    type: str
    geometry: Optional[GeoJsonGeometry]
    properties: RelativeLocation

