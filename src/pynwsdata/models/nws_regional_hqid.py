
from aenum import Enum

class NWSRegionalHQId(str, Enum):
    """
    Three-letter identifier for a NWS Regional HQ.
    """

    """
    allowed enum values
    """
    ARH = 'ARH'
    CRH = 'CRH'
    ERH = 'ERH'
    PRH = 'PRH'
    SRH = 'SRH'
    WRH = 'WRH'
