
from pynwsdata.models.region_code import RegionCode

class MarineRegionCode(RegionCode):
    """
    Marine region code. These are groups of marine areas combined.
    * AL: Alaska waters (PK)
    * AT: Atlantic Ocean (AM, AN)
    * GL: Great Lakes (LC, LE, LH, LM, LO, LS, SL)
    * GM: Gulf of Mexico (GM)
    * PA: Eastern Pacific Ocean and U.S. West Coast (PZ)
    * PI: Central and Western Pacific (PH, PM, PS)
    """

    AL = 'AL'
    AT = 'AT'
    GL = 'GL'
    GM = 'GM'
    PA = 'PA'
    PI = 'PI'
