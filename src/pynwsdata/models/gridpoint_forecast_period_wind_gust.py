
from pynwsdata.models.quantitative_value import QuantitativeValueInterim


class GridpointForecastPeriodWindGust(QuantitativeValueInterim):
    """
    Peak wind gust for the period.

    This property as an string value is deprecated. Future versions will express this value
    as a quantitative value object. To make use of the future standard format now, set the
    \"forecast_wind_speed_qv\" feature flag on the request.
    """
