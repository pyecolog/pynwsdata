

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.observation_station import ObservationStation
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ObservationStationCollectionGeoJsonAllOfFeatures(ApiObject):
    """
    ObservationStationCollectionGeoJsonAllOfFeatures
    """

    id: Optional[str] = None
    type: Optional[str] = None
    geometry: Optional[GeoJsonGeometry] = None
    properties: Optional[ObservationStation] = None


