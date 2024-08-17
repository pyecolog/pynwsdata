
from pynwsdata.api_object import ApiObject
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Union, Optional

class GridpointForecastPeriodWindSpeed(QuantitativeValue):
    """
    Wind speed for the period. This property as an string value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the \"forecast_wind_speed_qv\" feature flag on the request. 
    """
    actual_instance: Optional[Union[QuantitativeValue, str]] = None
    one_of_schemas: frozenset[str] = frozenset(map(ApiObject.intern, [ "QuantitativeValue", "str" ]))

