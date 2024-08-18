
from typing import Annotated, ClassVar, Optional, Union
from pynwsdata.api_object import ApiField
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry

class GeoJSONPoint(GeoJsonGeometry):
    """
    GeoJSONPoint
    """

    type_code: ClassVar[str] = "Point"

    type: str
    coordinates: Annotated[list[Union[float, int]], ApiField(min_length=2)] = ApiField(
        description="""A GeoJSON coordinate.

        Please refer to IETF RFC 7946 for information on the GeoJSON format.""")
    bbox: Optional[Annotated[list[Union[float, int]], ApiField(min_length=4)]] = ApiField(
        default=None, description="""A GeoJSON bounding box.

        Please refer to IETF RFC 7946 for information on the GeoJSON format.""")

    def __repr__(self) -> str:
        inner = "%s (%s)" % (self.__class__.__name__, ", ".join(map(str, self.coordinates)))
        bbox = self.bbox
        if bbox:
            return "<%s @ %s>" % (inner, ", ".join(map(str, bbox)))
        else:
            return "<%s>" % inner
