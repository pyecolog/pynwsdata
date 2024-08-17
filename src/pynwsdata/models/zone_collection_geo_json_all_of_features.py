

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.zone import Zone
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ZoneCollectionGeoJsonAllOfFeatures(ApiObject):
    """
    ZoneCollectionGeoJsonAllOfFeatures
    """

    properties: Optional[Zone] = None


