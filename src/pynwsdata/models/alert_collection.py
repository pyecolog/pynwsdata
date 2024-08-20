

from datetime import datetime
from typing import Optional
from pynwsdata.api_object import PagedApiObject, ApiField
from pynwsdata.models.pagination_info import PaginationInfo


class AlertCollection(PagedApiObject):
    """
    AlertCollection
    """

    title: Optional[str] = ApiField(default=None, description="""A title describing the alert collection""")
    updated: Optional[datetime] = ApiField(default=None, description="""The last time a change occurred to this collection""")
    pagination: Optional[PaginationInfo] = None

