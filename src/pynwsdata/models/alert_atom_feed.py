

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.alert_atom_entry import AlertAtomEntry
from pynwsdata.models.alert_atom_feed_author import AlertAtomFeedAuthor
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class AlertAtomFeed(ApiObject):
    """
    An alert feed in Atom format
    """

    id: Optional[str] = None
    generator: Optional[str] = None
    updated: Optional[str] = None
    author: Optional[AlertAtomFeedAuthor] = None
    title: Optional[str] = None
    entry: Optional[list[AlertAtomEntry]] = None


