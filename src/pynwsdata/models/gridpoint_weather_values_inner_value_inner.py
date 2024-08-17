

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class GridpointWeatherValuesInnerValueInner(ApiObject):
    """
    A value object representing expected weather phenomena.
    """

    coverage: Optional[str]
    weather: Optional[str]
    intensity: Optional[str]
    visibility: QuantitativeValue
    attributes: list[str]


