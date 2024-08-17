

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.alert import Alert
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class AlertJsonLd(ApiObject):
    """
    AlertJsonLd
    """

    graph: Optional[list[Alert]] = ApiField(default=None, alias="@graph")


