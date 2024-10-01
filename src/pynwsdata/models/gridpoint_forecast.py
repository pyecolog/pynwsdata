

from datetime import datetime
from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.gridpoint_forecast_period import GridpointForecastPeriod
from pynwsdata.models.gridpoint_forecast_units import GridpointForecastUnits
from pynwsdata.models.iso8601_interval import ISO8601Interval
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class GridpointForecast(ApiObject):
    """
    A multi-day forecast for a 2.5km grid square.
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    geometry: Optional[str] = ApiField(default=None, description="""A geometry represented in Well-Known Text (WKT) format.""")
    units: Optional[GridpointForecastUnits] = GridpointForecastUnits.US
    forecast_generator: Optional[str] = ApiField(default=None, description="""The internal generator class used to create the forecast text (used for NWS debugging).""", alias="forecastGenerator")
    generated_at: Optional[datetime] = ApiField(default=None, description="""The time this forecast data was generated.""", alias="generatedAt")
    update_time: Optional[datetime] = ApiField(default=None, description="""The last update time of the data this forecast was generated from.""", alias="updateTime")
    valid_times: Optional[ISO8601Interval.storage_type] = ApiField(default=None, alias="validTimes", interface_type=ISO8601Interval)
    elevation: Optional[QuantitativeValue] = None
    periods: Optional[list[GridpointForecastPeriod]] = ApiField(default=None, description="""An array of forecast periods.""")


