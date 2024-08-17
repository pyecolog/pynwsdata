

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.alert_atom_entry_author import AlertAtomEntryAuthor
from pynwsdata.models.alert_xml_parameter import AlertXMLParameter
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class AlertAtomEntry(ApiObject):
    """
    An alert entry in an Atom feed
    """

    id: Optional[str] = None
    updated: Optional[str] = None
    published: Optional[str] = None
    author: Optional[AlertAtomEntryAuthor] = None
    summary: Optional[str] = None
    event: Optional[str] = None
    sent: Optional[str] = None
    effective: Optional[str] = None
    expires: Optional[str] = None
    status: Optional[str] = None
    msg_type: Optional[str] = ApiField(default=None, alias="msgType")
    category: Optional[str] = None
    urgency: Optional[str] = None
    severity: Optional[str] = None
    certainty: Optional[str] = None
    area_desc: Optional[str] = ApiField(default=None, alias="areaDesc")
    polygon: Optional[str] = None
    geocode: Optional[list[AlertXMLParameter]] = None
    parameter: Optional[list[AlertXMLParameter]] = None


