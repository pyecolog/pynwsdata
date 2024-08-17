

from typing import Optional
from pynwsdata.api_object import ApiObject
from pynwsdata.models.alert import Alert


class AlertCollectionGeoJsonAllOfFeatures(ApiObject):
    """
    AlertCollectionGeoJsonAllOfFeatures
    """

    id: Optional[str] = None
    
    properties: Optional[Alert] = None
