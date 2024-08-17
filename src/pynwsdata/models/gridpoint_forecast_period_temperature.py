
from typing import Any, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Union, Optional
from pynwsdata.api_object import ApiObject, ApiField

class GridpointForecastPeriodTemperature(ApiObject):
    """
    High/low temperature for the period, depending on whether the period is day or night. This property as an integer value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the \"forecast_temperature_qv\" feature flag on the request. 
    """
    actual_instance: Optional[Union[QuantitativeValue, int]] = None
    one_of_schemas: frozenset[str] = frozenset(map(ApiObject.intern, [ "QuantitativeValue", "int" ]))
