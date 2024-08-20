
from typing import ClassVar, Optional, Union
from pynwsdata.api_object import ApiField
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry

class GeoJSONLineString(GeoJsonGeometry):
    """
    GeoJSONLineString
    """

    type_code: ClassVar[str] = "LineString"

    type: str
    coordinates: list[Union[float, int]] = ApiField(min_length=2,
        description="A GeoJSON line string. Please refer to IETF RFC 7946 for information on the GeoJSON format.")
    bbox: Optional[list[Union[float, int]]]= ApiField(min_length=4,
        default=None, description="A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format.")

