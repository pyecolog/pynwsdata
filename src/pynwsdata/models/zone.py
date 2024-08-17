

from datetime import datetime
from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.nws_forecast_office_id import NWSForecastOfficeId
from pynwsdata.models.nws_zone_type import NWSZoneType
from pynwsdata.models.zone_state import ZoneState
from typing import Optional
from typing_extensions import Self


class Zone(ApiObject):
    """
    Zone
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    geometry: Optional[str] = ApiField(default=None, description="""A geometry represented in Well-Known Text (WKT) format.""")
    id: Optional[str] = ApiField(default=None, alias="@id")
    type: Optional[str] = ApiField(default=None, alias="@type")
    id: Optional[str] = ApiField(default=None, description="""UGC identifier for a NWS forecast zone or county. The first two letters will correspond to either a state code or marine area code (see #/components/schemas/StateTerritoryCode and #/components/schemas/MarineAreaCode for lists of valid letter combinations). The third letter will be Z for public/fire zone or C for county. """)
    type: Optional[NWSZoneType] = None
    name: Optional[str] = None
    effective_date: Optional[datetime] = ApiField(default=None, alias="effectiveDate")
    expiration_date: Optional[datetime] = ApiField(default=None, alias="expirationDate")
    state: Optional[ZoneState] = None
    forecast_office: Optional[str] = ApiField(default=None, alias="forecastOffice")
    grid_identifier: Optional[str] = ApiField(default=None, alias="gridIdentifier")
    awips_location_identifier: Optional[str] = ApiField(default=None, alias="awipsLocationIdentifier")
    cwa: Optional[list[NWSForecastOfficeId]] = None
    forecast_offices: Optional[list[str]] = ApiField(default=None, alias="forecastOffices")
    time_zone: Optional[list[str]] = ApiField(default=None, alias="timeZone")
    observation_stations: Optional[list[str]] = ApiField(default=None, alias="observationStations")
    radar_station: Optional[str] = ApiField(default=None, alias="radarStation")


