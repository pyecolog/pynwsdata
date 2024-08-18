
from pynwsdata.api_enum import ApiEnum

class AlertStatus(ApiEnum):
    """
    AlertStatus
    """

    ACTUAL = 'Actual'
    EXERCISE = 'Exercise'
    SYSTEM = 'System'
    TEST = 'Test'
    DRAFT = 'Draft'
