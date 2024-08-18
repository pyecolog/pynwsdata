
from pynwsdata.api_enum import ApiEnum

class NWSZoneType(ApiEnum):
    """
    NWSZoneType
    """

    LAND = 'land'
    MARINE = 'marine'
    FORECAST = 'forecast'
    PUBLIC = 'public'
    COASTAL = 'coastal'
    OFFSHORE = 'offshore'
    FIRE = 'fire'
    COUNTY = 'county'
