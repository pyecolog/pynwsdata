

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class AlertsTypes200Response(ApiObject):
    """
    AlertsTypes200Response
    """

    event_types: Optional[list[str]] = ApiField(default=None, description="""A list of recognized event types""", alias="eventTypes")


