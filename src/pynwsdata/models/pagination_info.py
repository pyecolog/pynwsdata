

from typing import Any, ClassVar
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class PaginationInfo(ApiObject):
    """
    Links for retrieving more data from paged data sets
    """

    next: str = ApiField(description="""A link to the next page of records""")


