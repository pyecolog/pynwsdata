
from pynwsdata.api_enum import ApiEnum

class AlertCertainty(ApiEnum):
    """
    AlertCertainty
    """

    OBSERVED = 'Observed'
    LIKELY = 'Likely'
    POSSIBLE = 'Possible'
    UNLIKELY = 'Unlikely'
    UNKNOWN = 'Unknown'
