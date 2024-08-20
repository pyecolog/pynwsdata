

from typing import Optional
from pynwsdata.api_object import ApiField
from pynwsdata.models.point_relative_location import PointRelativeLocation
from pynwsdata.models.quantitative_value import QuantitativeValue

class RelativeLocationJsonLd(PointRelativeLocation):
    """
    RelativeLocationJsonLd
    """

    city: Optional[str] = None
    state: Optional[str] = None
    distance: Optional[QuantitativeValue] = None
    bearing: Optional[QuantitativeValue] = None
    geometry: Optional[str] = ApiField(description="""A geometry represented in Well-Known Text (WKT) format.""")


