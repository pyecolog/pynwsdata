
from pynwsdata.api_object import ApiObject
from pynwsdata.models.state_territory_code import StateTerritoryCode
from typing import Union, Optional

class ZoneState(ApiObject):
    """
    ZoneState
    """
    actual_instance: Optional[Union[StateTerritoryCode, str]] = None
    one_of_schemas: frozenset[str] = frozenset(map(ApiObject.intern, [ "StateTerritoryCode", "str" ]))
