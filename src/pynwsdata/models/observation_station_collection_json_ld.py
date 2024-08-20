

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import PagedApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.observation_station import ObservationStation
from pynwsdata.models.pagination_info import PaginationInfo
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ObservationStationCollectionJsonLd(PagedApiObject):
    """
    ObservationStationCollectionJsonLd
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    graph: Optional[list[ObservationStation]] = ApiField(default=None, alias="@graph")
    observation_stations: Optional[list[str]] = ApiField(default=None, alias="observationStations")
    pagination: Optional[PaginationInfo] = None


