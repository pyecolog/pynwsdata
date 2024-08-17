

from datetime import datetime
from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class AlertReferencesInner(ApiObject):
    """
    AlertReferencesInner
    """

    id: Optional[str] = ApiField(default=None, description="""An API link to the prior alert.""", alias="@id")
    identifier: Optional[str] = ApiField(default=None, description="""The identifier of the alert message.""")
    sender: Optional[str] = ApiField(default=None, description="""The sender of the prior alert.""")
    sent: Optional[datetime] = ApiField(default=None, description="""The time the prior alert was sent.""")


