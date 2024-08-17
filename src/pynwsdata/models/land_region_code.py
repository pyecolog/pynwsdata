
from aenum import Enum

class LandRegionCode(str, Enum):
    """
    Land region code. These correspond to the six NWS regional headquarters: * AR: Alaska Region * CR: Central Region * ER: Eastern Region * PR: Pacific Region * SR: Southern Region * WR: Western Region 
    """

    """
    allowed enum values
    """
    AR = 'AR'
    CR = 'CR'
    ER = 'ER'
    PR = 'PR'
    SR = 'SR'
    WR = 'WR'
