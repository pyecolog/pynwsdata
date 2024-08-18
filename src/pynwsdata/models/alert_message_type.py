
from pynwsdata.api_enum import ApiEnum

class AlertMessageType(ApiEnum):
    """
    AlertMessageType
    """

    ALERT = 'Alert'
    UPDATE = 'Update'
    CANCEL = 'Cancel'
    ACK = 'Ack'
    ERROR = 'Error'
