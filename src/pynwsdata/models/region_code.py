
from typing import Any, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.land_region_code import LandRegionCode
from pynwsdata.models.marine_region_code import MarineRegionCode
from typing import Union, Optional
from pynwsdata.api_object import ApiObject, ApiField

class RegionCode(ApiObject):
    """
    RegionCode
    """
    actual_instance: Optional[Union[LandRegionCode, MarineRegionCode]] = None
    one_of_schemas: frozenset[str] = frozenset(map(ApiObject.intern, [ "LandRegionCode", "MarineRegionCode" ]))
