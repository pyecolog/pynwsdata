

from datetime import datetime
from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.gridpoint_forecast_period_temperature import GridpointForecastPeriodTemperature
from pynwsdata.models.gridpoint_forecast_period_wind_gust import GridpointForecastPeriodWindGust
from pynwsdata.models.gridpoint_forecast_period_wind_speed import GridpointForecastPeriodWindSpeed
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from typing_extensions import Self


class GridpointForecastPeriod(ApiObject):
    """
    An object containing forecast information for a specific time period (generally 12-hour or 1-hour). 
    """

    number: Optional[Annotated[int, ApiField(ge=1)]] = ApiField(default=None, description="""Sequential period number.""")
    name: Optional[str] = ApiField(default=None, description="""A textual identifier for the period. This value will not be present for hourly forecasts. """)
    start_time: Optional[datetime] = ApiField(default=None, description="""The starting time that this forecast period is valid for.""", alias="startTime")
    end_time: Optional[datetime] = ApiField(default=None, description="""The ending time that this forecast period is valid for.""", alias="endTime")
    is_daytime: Optional[bool] = ApiField(default=None, description="""Indicates whether this period is daytime or nighttime.""", alias="isDaytime")
    temperature: Optional[GridpointForecastPeriodTemperature] = None
    temperature_unit: Optional[str] = ApiField(default=None, description="""The unit of the temperature value (Fahrenheit or Celsius). This property is deprecated. Future versions will indicate the unit within the quantitative value object for the temperature property. To make use of the future standard format now, set the \"""forecast_temperature_qv\" feature flag on the request. ", alias="temperatureUnit""")
    temperature_trend: Optional[str] = ApiField(default=None, description="""If not null, indicates a non-diurnal temperature trend for the period (either rising temperature overnight, or falling temperature during the day) """, alias="temperatureTrend")
    probability_of_precipitation: Optional[QuantitativeValue] = ApiField(default=None, alias="probabilityOfPrecipitation")
    dewpoint: Optional[QuantitativeValue] = None
    relative_humidity: Optional[QuantitativeValue] = ApiField(default=None, alias="relativeHumidity")
    wind_speed: Optional[GridpointForecastPeriodWindSpeed] = ApiField(default=None, alias="windSpeed")
    wind_gust: Optional[GridpointForecastPeriodWindGust] = ApiField(default=None, alias="windGust")
    wind_direction: Optional[str] = ApiField(default=None, description="""The prevailing direction of the wind for the period, using a 16-point compass.""", alias="windDirection")
    icon: Optional[str] = ApiField(default=None, description="""A link to an icon representing the forecast summary.""")
    short_forecast: Optional[str] = ApiField(default=None, description="""A brief textual forecast summary for the period.""", alias="shortForecast")
    detailed_forecast: Optional[str] = ApiField(default=None, description="""A detailed textual forecast for the period.""", alias="detailedForecast")



