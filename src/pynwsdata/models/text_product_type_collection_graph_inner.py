

from typing import Any, ClassVar
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class TextProductTypeCollectionGraphInner(ApiObject):
    """
    TextProductTypeCollectionGraphInner
    """

    product_code: str = ApiField(alias="productCode")
    product_name: str = ApiField(alias="productName")


