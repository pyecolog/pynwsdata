
from pynwsdata.api_object import ApiObject, ApiField
from typing import Any, ClassVar, Optional
from typing import Optional
from typing_extensions import Self

class MetarPhenomenon(ApiObject):
    """
    An object representing a decoded METAR phenomenon string.
    """

    intensity: Optional[str]
    modifier: Optional[str]
    weather: str
    raw_string: str = ApiField(alias="rawString")
    in_vicinity: Optional[bool] = ApiField(default=None, alias="inVicinity")

