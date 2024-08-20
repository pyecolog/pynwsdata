
from pynwsdata.api_object import AbstractApiObject, SubtypeMap
from typing import ClassVar

class PointRelativeLocation(AbstractApiObject):
    """
    PointRelativeLocation
    """

    subtype_map: ClassVar[SubtypeMap] = {
        #
        # The Feature type was encountered in server response data.
        #
        # In this usage, it appears to denote a RelativeLocationGeoJson type.
        "Feature": ("RelativeLocationGeoJson", "relative_location_geo_json")
    }
