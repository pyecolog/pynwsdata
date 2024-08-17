

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class RelativeLocation(ApiObject):
    """
    RelativeLocation
    """

    city: Optional[str] = None
    state: Optional[str] = None
    distance: Optional[QuantitativeValue] = None
    bearing: Optional[QuantitativeValue] = None


