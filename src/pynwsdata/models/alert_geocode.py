

from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from typing_extensions import Self


class AlertGeocode(ApiObject):
    """
    Lists of codes for NWS public zones and counties affected by the alert.
    """

    ugc: Optional[list[str]] = ApiField(default=None, description="""A list of NWS public zone or county identifiers.""", alias="UGC")
    same: Optional[list[str]] = ApiField(default=None, description="""A list of SAME (Specific Area Message Encoding) codes for affected counties.""", alias="SAME")


