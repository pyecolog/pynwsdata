
from typing import Annotated, ClassVar, Optional, Union
from pynwsdata.api_object import ApiField
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry


class GeoJSONMultiPolygon(GeoJsonGeometry):
    """
    GeoJSONMultiPolygon
    """

    type_code: ClassVar[str] = "MultiPolygon"

    type: str
    coordinates: list[list[Annotated[list[Annotated[list[Union[float, int]], ApiField(min_length=2)]], ApiField(min_length=4)]]]
    bbox: Optional[list[Union[float, int]]] = ApiField(default=None, min_length=4, description="""A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format.""")

