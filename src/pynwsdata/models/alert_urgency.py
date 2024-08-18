
from pynwsdata.api_enum import ApiEnum

class AlertUrgency(ApiEnum):
    """
    AlertUrgency
    """

    IMMEDIATE = 'Immediate'
    EXPECTED = 'Expected'
    FUTURE = 'Future'
    PAST = 'Past'
    UNKNOWN = 'Unknown'
