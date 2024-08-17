
from aenum import Enum

class AlertMessageType(str, Enum):
    """
    AlertMessageType
    """

    """
    allowed enum values
    """
    ALERT = 'Alert'
    UPDATE = 'Update'
    CANCEL = 'Cancel'
    ACK = 'Ack'
    ERROR = 'Error'
