

from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.nws_forecast_office_id import NWSForecastOfficeId
from pynwsdata.models.point_relative_location import PointRelativeLocation
from typing import Optional
from typing_extensions import Self


class Point(ApiObject):
    """
    Point
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    geometry: Optional[str] = ApiField(default=None, description="""A geometry represented in Well-Known Text (WKT) format.""")
    id: Optional[str] = ApiField(default=None, alias="@id")
    type: Optional[str] = ApiField(default=None, alias="@type")
    cwa: Optional[NWSForecastOfficeId] = None
    forecast_office: Optional[str] = ApiField(default=None, alias="forecastOffice")
    grid_id: Optional[NWSForecastOfficeId] = ApiField(default=None, alias="gridId")
    grid_x: Optional[Annotated[int, ApiField(ge=0)]] = ApiField(default=None, alias="gridX")
    grid_y: Optional[Annotated[int, ApiField(ge=0)]] = ApiField(default=None, alias="gridY")
    forecast: Optional[str] = None
    forecast_hourly: Optional[str] = ApiField(default=None, alias="forecastHourly")
    forecast_grid_data: Optional[str] = ApiField(default=None, alias="forecastGridData")
    observation_stations: Optional[str] = ApiField(default=None, alias="observationStations")
    relative_location: Optional[PointRelativeLocation] = ApiField(default=None, alias="relativeLocation")
    forecast_zone: Optional[str] = ApiField(default=None, alias="forecastZone")
    county: Optional[str] = None
    fire_weather_zone: Optional[str] = ApiField(default=None, alias="fireWeatherZone")
    time_zone: Optional[str] = ApiField(default=None, alias="timeZone")
    radar_station: Optional[str] = ApiField(default=None, alias="radarStation")

