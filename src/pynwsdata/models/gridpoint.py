

from datetime import datetime
from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.gridpoint_hazards import GridpointHazards
from pynwsdata.models.gridpoint_weather import GridpointWeather
from pynwsdata.models.iso8601_interval import ISO8601Interval
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from typing_extensions import Self


class Gridpoint(ApiObject):
    """
    Raw forecast data for a 2.5km grid square. This is a list of all potential data layers that may appear. Some layers may not be present in all areas. * temperature * dewpoint * maxTemperature * minTemperature * relativeHumidity * apparentTemperature * heatIndex * windChill * wetBulbGlobeTemperature * skyCover * windDirection * windSpeed * windGust * weather * hazards: Watch and advisory products in effect * probabilityOfPrecipitation * quantitativePrecipitation * iceAccumulation * snowfallAmount * snowLevel * ceilingHeight * visibility * transportWindSpeed * transportWindDirection * mixingHeight * hainesIndex * lightningActivityLevel * twentyFootWindSpeed * twentyFootWindDirection * waveHeight * wavePeriod * waveDirection * primarySwellHeight * primarySwellDirection * secondarySwellHeight * secondarySwellDirection * wavePeriod2 * windWaveHeight * dispersionIndex * pressure: Barometric pressure * probabilityOfTropicalStormWinds * probabilityOfHurricaneWinds * potentialOf15mphWinds * potentialOf25mphWinds * potentialOf35mphWinds * potentialOf45mphWinds * potentialOf20mphWindGusts * potentialOf30mphWindGusts * potentialOf40mphWindGusts * potentialOf50mphWindGusts * potentialOf60mphWindGusts * grasslandFireDangerIndex * probabilityOfThunder * davisStabilityIndex * atmosphericDispersionIndex * lowVisibilityOccurrenceRiskIndex * stability * redFlagThreatIndex 
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    geometry: Optional[str] = ApiField(default=None, description="""A geometry represented in Well-Known Text (WKT) format.""")
    id: Optional[str] = ApiField(default=None, alias="@id")
    type: Optional[str] = ApiField(default=None, alias="@type")
    update_time: Optional[datetime] = ApiField(default=None, alias="updateTime")
    valid_times: Optional[ISO8601Interval.storage_type] = ApiField(default=None, alias="validTimes", interface_type = ISO8601Interval)
    elevation: Optional[QuantitativeValue] = None
    forecast_office: Optional[str] = ApiField(default=None, alias="forecastOffice")
    grid_id: Optional[str] = ApiField(default=None, alias="gridId")
    grid_x: Optional[Annotated[int, ApiField(ge=0)]] = ApiField(default=None, alias="gridX")
    grid_y: Optional[Annotated[int, ApiField(ge=0)]] = ApiField(default=None, alias="gridY")
    weather: Optional[GridpointWeather] = None
    hazards: Optional[GridpointHazards] = None
    additional_properties: dict[str, Any] = {}

