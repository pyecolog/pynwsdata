

from datetime import datetime
from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.alert_certainty import AlertCertainty
from pynwsdata.models.alert_geocode import AlertGeocode
from pynwsdata.models.alert_message_type import AlertMessageType
from pynwsdata.models.alert_references_inner import AlertReferencesInner
from pynwsdata.models.alert_severity import AlertSeverity
from pynwsdata.models.alert_status import AlertStatus
from pynwsdata.models.alert_urgency import AlertUrgency
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class Alert(ApiObject):
    """
    An object representing a public alert message. Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information. http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://alerts.weather.gov/#technical-notes-v12
    """

    id: Optional[str] = ApiField(default=None, description="""The identifier of the alert message.""")
    area_desc: Optional[str] = ApiField(default=None, description="""A textual description of the area affected by the alert.""", alias="areaDesc")
    geocode: Optional[AlertGeocode] = None
    affected_zones: Optional[list[str]] = ApiField(default=None, description="""An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification. """, alias="affectedZones")
    references: Optional[list[AlertReferencesInner]] = ApiField(default=None, description="""A list of prior alerts that this alert updates or replaces.""")
    sent: Optional[datetime] = ApiField(default=None, description="""The time of the origination of the alert message.""")
    effective: Optional[datetime] = ApiField(default=None, description="""The effective time of the information of the alert message.""")
    onset: Optional[datetime] = ApiField(default=None, description="""The expected time of the beginning of the subject event of the alert message.""")
    expires: Optional[datetime] = ApiField(default=None, description="""The expiry time of the information of the alert message.""")
    ends: Optional[datetime] = ApiField(default=None, description="""The expected end time of the subject event of the alert message.""")
    status: Optional[AlertStatus] = None
    message_type: Optional[AlertMessageType] = ApiField(default=None, alias="messageType")
    category: Optional[str] = ApiField(default=None, description="""The code denoting the category of the subject event of the alert message.""")
    severity: Optional[AlertSeverity] = None
    certainty: Optional[AlertCertainty] = None
    urgency: Optional[AlertUrgency] = None
    event: Optional[str] = ApiField(default=None, description="""The text denoting the type of the subject event of the alert message.""")
    sender: Optional[str] = ApiField(default=None, description="""Email address of the NWS webmaster.""")
    sender_name: Optional[str] = ApiField(default=None, description="""The text naming the originator of the alert message.""", alias="senderName")
    headline: Optional[str] = ApiField(default=None, description="""The text headline of the alert message.""")
    description: Optional[str] = ApiField(default=None, description="""The text describing the subject event of the alert message.""")
    instruction: Optional[str] = ApiField(default=None, description="""The text describing the recommended action to be taken by recipients of the alert message. """)
    response: Optional[str] = ApiField(default=None, description="""The code denoting the type of action recommended for the target audience. This corresponds to responseType in the CAP specification. """)
    parameters: Optional[dict[str, list[Any]]] = ApiField(default=None, description="""System-specific additional parameters associated with the alert message. The keys in this object correspond to parameter definitions in the NWS CAP specification. """)


