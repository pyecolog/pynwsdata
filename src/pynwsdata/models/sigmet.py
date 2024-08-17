

from datetime import datetime
from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from typing_extensions import Self


class Sigmet(ApiObject):
    """
    Sigmet
    """

    id: Optional[str] = None
    issue_time: Optional[datetime] = ApiField(default=None, alias="issueTime")
    fir: Optional[str] = None
    atsu: Optional[str] = ApiField(default=None, description="""ATSU Identifier""")
    sequence: Optional[str] = None
    phenomenon: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None

