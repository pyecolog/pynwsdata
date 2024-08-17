
from aenum import Enum

class AlertUrgency(str, Enum):
    """
    AlertUrgency
    """

    """
    allowed enum values
    """
    IMMEDIATE = 'Immediate'
    EXPECTED = 'Expected'
    FUTURE = 'Future'
    PAST = 'Past'
    UNKNOWN = 'Unknown'
