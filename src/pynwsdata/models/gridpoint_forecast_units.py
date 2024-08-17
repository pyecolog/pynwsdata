
from aenum import Enum

class GridpointForecastUnits(str, Enum):
    """
    Denotes the units used in the textual portions of the forecast.
    """

    """
    allowed enum values
    """
    US = 'us'
    SI = 'si'
