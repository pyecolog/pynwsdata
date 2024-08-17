
from aenum import Enum

class MarineAreaCode(str, Enum):
    """
    Marine area code as defined in NWS Directive 10-302: * AM: Western North Atlantic Ocean and along U.S. East Coast south of Currituck Beach Light NC following the coastline into Gulf of Mexico to Ocean Reef FL including the Caribbean * AN: Western North Atlantic Ocean and along U.S. East Coast from Canadian border south to Currituck Beach Light NC * GM: Gulf of Mexico and along the U.S. Gulf Coast from the Mexican border to Ocean Reef FL * LC: Lake St. Clair * LE: Lake Erie * LH: Lake Huron * LM: Lake Michigan * LO: Lake Ontario * LS: Lake Superior * PH: Central Pacific Ocean including Hawaiian waters * PK: North Pacific Ocean near Alaska and along Alaska coastline including the Bering Sea and the Gulf of Alaska * PM: Western Pacific Ocean including Mariana Island waters * PS: South Central Pacific Ocean including American Samoa waters * PZ: Eastern North Pacific Ocean and along U.S. West Coast from Canadian border to Mexican border * SL: St. Lawrence River above St. Regis 
    """

    """
    allowed enum values
    """
    AM = 'AM'
    AN = 'AN'
    GM = 'GM'
    LC = 'LC'
    LE = 'LE'
    LH = 'LH'
    LM = 'LM'
    LO = 'LO'
    LS = 'LS'
    PH = 'PH'
    PK = 'PK'
    PM = 'PM'
    PS = 'PS'
    PZ = 'PZ'
    SL = 'SL'
