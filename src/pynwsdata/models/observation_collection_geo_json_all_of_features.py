

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.observation import Observation
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ObservationCollectionGeoJsonAllOfFeatures(ApiObject):
    """
    ObservationCollectionGeoJsonAllOfFeatures
    """

    properties: Optional[Observation] = None


