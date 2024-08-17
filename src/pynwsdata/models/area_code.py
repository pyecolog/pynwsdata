
from typing import Any, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.marine_area_code import MarineAreaCode
from pynwsdata.models.state_territory_code import StateTerritoryCode
from typing import Union, Optional
from pynwsdata.api_object import ApiObject, ApiField

class AreaCode(ApiObject):
    """
    State/territory codes and marine area codes
    """

    actual_instance: Optional[Union[MarineAreaCode, StateTerritoryCode]] = None#



