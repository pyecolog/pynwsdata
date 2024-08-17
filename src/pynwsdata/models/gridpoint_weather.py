

from typing import Any, ClassVar
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.gridpoint_weather_values_inner import GridpointWeatherValuesInner
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class GridpointWeather(ApiObject):
    """
    GridpointWeather
    """

    values: list[GridpointWeatherValuesInner]


