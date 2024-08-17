

from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from typing_extensions import Self


class AlertsActiveCount200Response(ApiObject):
    """
    AlertsActiveCount200Response
    """

    total: Optional[Annotated[int, ApiField(ge=0)]] = ApiField(default=None, description="""The total number of active alerts""")
    land: Optional[Annotated[int, ApiField(ge=0)]] = ApiField(default=None, description="""The total number of active alerts affecting land zones""")
    marine: Optional[Annotated[int, ApiField(ge=0)]] = ApiField(default=None, description="""The total number of active alerts affecting marine zones""")
    regions: Optional[dict[str, Annotated[int, ApiField(ge=1)]]] = ApiField(default=None, description="""Active alerts by marine region""")
    areas: Optional[dict[str, Annotated[int, ApiField(ge=1)]]] = ApiField(default=None, description="""Active alerts by area (state/territory)""")
    zones: Optional[dict[str, Annotated[int, ApiField(ge=1)]]] = ApiField(default=None, description="""Active alerts by NWS public zone or county code""")


