

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class RelativeLocationJsonLd(ApiObject):
    """
    RelativeLocationJsonLd
    """

    city: Optional[str] = None
    state: Optional[str] = None
    distance: Optional[QuantitativeValue] = None
    bearing: Optional[QuantitativeValue] = None
    geometry: Optional[str] = ApiField(description="""A geometry represented in Well-Known Text (WKT) format.""")


