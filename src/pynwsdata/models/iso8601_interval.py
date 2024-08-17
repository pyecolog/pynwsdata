
from pynwsdata.api_object import ApiObject
from typing import Union, Optional


class ISO8601Interval(ApiObject):
    """
    A time interval in ISO 8601 format. This can be one of:      1. Start and end time     2. Start time and duration     3. Duration and end time The string \"NOW\" can also be used in place of a start/end time. 
    """
    actual_instance: Optional[Union[str]] = None
    one_of_schemas: frozenset[str] = frozenset(map(ApiObject.intern, [ "str" ]))
