

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ObservationStationJsonLd(ApiObject):
    """
    ObservationStationJsonLd
    """

    context: JsonLdContext = ApiField(alias="@context")
    geometry: Optional[str] = ApiField(description="""A geometry represented in Well-Known Text (WKT) format.""")
    id: Optional[str] = ApiField(default=None, alias="@id")
    type: Optional[str] = ApiField(default=None, alias="@type")
    elevation: Optional[QuantitativeValue] = None
    station_identifier: Optional[str] = ApiField(default=None, alias="stationIdentifier")
    name: Optional[str] = None
    time_zone: Optional[str] = ApiField(default=None, alias="timeZone")
    forecast: Optional[str] = ApiField(default=None, description="""A link to the NWS public forecast zone containing this station.""")
    county: Optional[str] = ApiField(default=None, description="""A link to the NWS county zone containing this station.""")
    fire_weather_zone: Optional[str] = ApiField(default=None, description="""A link to the NWS fire weather forecast zone containing this station.""", alias="fireWeatherZone")

