

from typing import Optional
from pynwsdata.api_object import ApiObject
from pynwsdata.models.alert import Alert
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry

class AlertCollectionGeoJsonAllOfFeatures(ApiObject):
    """
    AlertCollectionGeoJsonAllOfFeatures
    """

    id: Optional[str] = None
    type: Optional[str] = None
    geometry: Optional[GeoJsonGeometry] = None

    properties: Optional[Alert] = None
