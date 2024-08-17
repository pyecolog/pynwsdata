
from aenum import Enum

class AlertStatus(str, Enum):
    """
    AlertStatus
    """

    """
    allowed enum values
    """
    ACTUAL = 'Actual'
    EXERCISE = 'Exercise'
    SYSTEM = 'System'
    TEST = 'Test'
    DRAFT = 'Draft'
