
from typing import TYPE_CHECKING, ClassVar, Union
from pynwsdata.api_object import AbstractApiObject, SubtypeMap


class GeoJsonGeometry(AbstractApiObject):
    # abstract base class
    """
    A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    """

    type_code: ClassVar[str]

    if TYPE_CHECKING:
        # common attributes of subclasses
        type: str
        coordinates: list[Union[float, int]]
        bbox: list[Union[float, int]]

    subtype_map: ClassVar[SubtypeMap] = {
    # mapping from 'type' strings to class names and submodules of __package__
    "Point": ("GeoJSONPoint", "geo_json_point"),
    "Polygon": ("GeoJSONPolygon", "geo_json_polygon"),
    "LineString":  ("GeoJSONLineString", "geo_json_line_string"),
    "MultiPolygon": ("GeoJSONMultiPolygon", "geo_json_multi_polygon"),
    "MultiLineString": ("GeoJSONMultiLineString", "geo_json_multi_line_string"),
    "MultiPoint": ("GeoJSONMultiPoint", "geo_json_multi_point")
    }

