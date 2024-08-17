
from pynwsdata.models.relative_location_geo_json import RelativeLocationGeoJson
from pynwsdata.models.relative_location_json_ld import RelativeLocationJsonLd
from pynwsdata.api_object import ApiObject
from typing import Union, Optional

class PointRelativeLocation(ApiObject):
    """
    PointRelativeLocation
    """
    actual_instance: Optional[Union[RelativeLocationGeoJson, RelativeLocationJsonLd]] = None
    one_of_schemas: frozenset[str] = frozenset(map(ApiObject.intern, [ "RelativeLocationGeoJson", "RelativeLocationJsonLd" ]))
