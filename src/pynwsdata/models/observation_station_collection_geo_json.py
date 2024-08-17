

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.observation_station_collection_geo_json_all_of_features import ObservationStationCollectionGeoJsonAllOfFeatures
from pynwsdata.models.pagination_info import PaginationInfo
from pynwsdata.models.observation_station import ObservationStation
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ObservationStationCollectionGeoJson(ApiObject):
    """
    ObservationStationCollectionGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    type: str
    features: list[ObservationStationCollectionGeoJsonAllOfFeatures]
    observation_stations: Optional[list[str]] = ApiField(default=None, alias="observationStations")
    pagination: Optional[PaginationInfo] = None
    # post hoc, these cooked sources are so much a mess
    properties: Optional[ObservationStation] = None 


