

from datetime import datetime
from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.zone_forecast_periods_inner import ZoneForecastPeriodsInner
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ZoneForecast(ApiObject):
    """
    An object representing a zone area forecast.
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    geometry: Optional[str] = ApiField(default=None, description="""A geometry represented in Well-Known Text (WKT) format.""")
    zone: Optional[str] = ApiField(default=None, description="""An API link to the zone this forecast is for.""")
    updated: Optional[datetime] = ApiField(default=None, description="""The time this zone forecast product was published.""")
    periods: Optional[list[ZoneForecastPeriodsInner]] = ApiField(default=None, description="""An array of forecast periods.""")


