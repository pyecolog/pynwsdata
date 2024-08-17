
from aenum import Enum

class AlertSeverity(str, Enum):
    """
    AlertSeverity
    """

    """
    allowed enum values
    """
    EXTREME = 'Extreme'
    SEVERE = 'Severe'
    MODERATE = 'Moderate'
    MINOR = 'Minor'
    UNKNOWN = 'Unknown'
