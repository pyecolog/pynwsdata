
from typing import ClassVar, Optional, Union
from pynwsdata.api_object import ApiField
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry

class GeoJSONPoint(GeoJsonGeometry):
    """
    GeoJSONPoint
    """

    type_code: ClassVar[str] = "Point"

    type: str
    coordinates: list[Union[float, int]] = ApiField(
        min_length=2,
        description="""A GeoJSON coordinate.

        Please refer to IETF RFC 7946 for information on the GeoJSON format.""")

    bbox: Optional[list[Union[float, int]]] = ApiField(
        min_length=4, default=None,
        description="""A GeoJSON bounding box.

        Please refer to IETF RFC 7946 for information on the GeoJSON format.""")

    def __repr__(self) -> str:
        #
        # Ensure lat, long coordinates are presented in conventional order
        #
        # GeoJSON uses the ordering for coordinates:
        #   (longitude, latitude)
        # https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.1
        #
        # Known Limitations
        # - This string representation does not match the coordinate's encoding
        #
        inner = "%s (%s)" % (self.__class__.__name__, ", ".join(map(str, self.coordinates[::-1])))
        bbox = self.bbox
        if bbox:
            return "<%s @ %s>" % (inner, ", ".join(map(str, bbox)))
        else:
            return "<%s>" % inner
