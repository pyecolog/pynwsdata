

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class OfficeAddress(ApiObject):
    """
    OfficeAddress
    """

    type: Optional[str] = ApiField(default=None, alias="@type")
    street_address: Optional[str] = ApiField(default=None, alias="streetAddress")
    address_locality: Optional[str] = ApiField(default=None, alias="addressLocality")
    address_region: Optional[str] = ApiField(default=None, alias="addressRegion")
    postal_code: Optional[str] = ApiField(default=None, alias="postalCode")

