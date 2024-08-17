
from datetime import datetime
from pynwsdata.api_object import ApiObject, ApiField
from typing import Any, ClassVar, Optional
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.metar_phenomenon import MetarPhenomenon
from pynwsdata.models.observation_cloud_layers_inner import ObservationCloudLayersInner
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from typing_extensions import Self

class Observation(ApiObject):
    """
    Observation
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    geometry: Optional[str] = ApiField(default=None, description="A geometry represented in Well-Known Text (WKT) format.")
    id: Optional[str] = ApiField(default=None, alias="@id")
    type: Optional[str] = ApiField(default=None, alias="@type")
    elevation: Optional[QuantitativeValue] = None
    station: Optional[str] = None
    timestamp: Optional[datetime] = None
    raw_message: Optional[str] = ApiField(default=None, alias="rawMessage")
    text_description: Optional[str] = ApiField(default=None, alias="textDescription")
    icon: Optional[str] = None
    present_weather: Optional[list[MetarPhenomenon]] = ApiField(default=None, alias="presentWeather")
    temperature: Optional[QuantitativeValue] = None
    dewpoint: Optional[QuantitativeValue] = None
    wind_direction: Optional[QuantitativeValue] = ApiField(default=None, alias="windDirection")
    wind_speed: Optional[QuantitativeValue] = ApiField(default=None, alias="windSpeed")
    wind_gust: Optional[QuantitativeValue] = ApiField(default=None, alias="windGust")
    barometric_pressure: Optional[QuantitativeValue] = ApiField(default=None, alias="barometricPressure")
    sea_level_pressure: Optional[QuantitativeValue] = ApiField(default=None, alias="seaLevelPressure")
    visibility: Optional[QuantitativeValue] = None
    max_temperature_last24_hours: Optional[QuantitativeValue] = ApiField(default=None, alias="maxTemperatureLast24Hours")
    min_temperature_last24_hours: Optional[QuantitativeValue] = ApiField(default=None, alias="minTemperatureLast24Hours")
    precipitation_last_hour: Optional[QuantitativeValue] = ApiField(default=None, alias="precipitationLastHour")
    precipitation_last3_hours: Optional[QuantitativeValue] = ApiField(default=None, alias="precipitationLast3Hours")
    precipitation_last6_hours: Optional[QuantitativeValue] = ApiField(default=None, alias="precipitationLast6Hours")
    relative_humidity: Optional[QuantitativeValue] = ApiField(default=None, alias="relativeHumidity")
    wind_chill: Optional[QuantitativeValue] = ApiField(default=None, alias="windChill")
    heat_index: Optional[QuantitativeValue] = ApiField(default=None, alias="heatIndex")
    cloud_layers: Optional[list[ObservationCloudLayersInner]] = ApiField(default=None, alias="cloudLayers")


