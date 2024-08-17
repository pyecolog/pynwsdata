
from aenum import Enum

class AlertCertainty(str, Enum):
    """
    AlertCertainty
    """

    """
    allowed enum values
    """
    OBSERVED = 'Observed'
    LIKELY = 'Likely'
    POSSIBLE = 'Possible'
    UNLIKELY = 'Unlikely'
    UNKNOWN = 'Unknown'
