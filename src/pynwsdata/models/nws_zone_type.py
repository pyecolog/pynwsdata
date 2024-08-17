
from aenum import Enum

class NWSZoneType(str, Enum):
    """
    NWSZoneType
    """

    """
    allowed enum values
    """
    LAND = 'land'
    MARINE = 'marine'
    FORECAST = 'forecast'
    PUBLIC = 'public'
    COASTAL = 'coastal'
    OFFSHORE = 'offshore'
    FIRE = 'fire'
    COUNTY = 'county'
