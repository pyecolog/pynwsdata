
from aenum import Enum

class MetarSkyCoverage(str, Enum):
    """
    MetarSkyCoverage
    """

    """
    allowed enum values
    """
    OVC = 'OVC'
    BKN = 'BKN'
    SCT = 'SCT'
    FEW = 'FEW'
    SKC = 'SKC'
    CLR = 'CLR'
    VV = 'VV'
