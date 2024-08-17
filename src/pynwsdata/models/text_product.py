

from datetime import datetime
from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class TextProduct(ApiObject):
    """
    TextProduct
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    id: Optional[str] = ApiField(default=None, alias="@id")
    id: Optional[str] = None
    wmo_collective_id: Optional[str] = ApiField(default=None, alias="wmoCollectiveId")
    issuing_office: Optional[str] = ApiField(default=None, alias="issuingOffice")
    issuance_time: Optional[datetime] = ApiField(default=None, alias="issuanceTime")
    product_code: Optional[str] = ApiField(default=None, alias="productCode")
    product_name: Optional[str] = ApiField(default=None, alias="productName")
    product_text: Optional[str] = ApiField(default=None, alias="productText")


