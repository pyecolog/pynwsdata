
from typing import Any, ClassVar, Optional, Union
from typing_extensions import Annotated
from pynwsdata.api_object import ApiField
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry
from typing import Optional
from typing_extensions import Self


class GeoJSONMultiLineString(GeoJsonGeometry):
    """
    GeoJSONMultiLineString
    """

    type_code: ClassVar[str] = "MultiLineString"

    type: str
    coordinates: list[Annotated[list[Annotated[list[Union[float, int]], ApiField(min_length=2)]], ApiField(min_length=2)]]
    bbox: Optional[Annotated[list[Union[float, int]], ApiField(min_length=4)]] = ApiField(default=None, description="""A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format.""")

