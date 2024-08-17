

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class AlertXMLParameter(ApiObject):
    """
    AlertXMLParameter
    """

    value_name: Optional[str] = ApiField(default=None, alias="valueName")
    value: Optional[str] = None


