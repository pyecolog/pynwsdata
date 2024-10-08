
from pynwsdata.models.quantitative_value import QuantitativeValueInterim


class GridpointForecastPeriodTemperature(QuantitativeValueInterim):
    """
    High/low temperature for the period, depending on whether the period is day or night.

    This property as an integer value is deprecated. Future versions will express this value
    as a quantitative value object. To make use of the future standard format now, set the
    \"forecast_temperature_qv\" feature flag on the request.
    """
