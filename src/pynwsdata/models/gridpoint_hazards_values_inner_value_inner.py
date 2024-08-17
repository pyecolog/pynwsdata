

from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from typing_extensions import Self


class GridpointHazardsValuesInnerValueInner(ApiObject):
    """
    A value object representing an expected hazard.
    """

    phenomenon: str = ApiField(description="""Hazard code. This value will correspond to a P-VTEC phenomenon code as defined in NWS Directive 10-1703. """)
    significance: str = ApiField(description="""Significance code. This value will correspond to a P-VTEC significance code as defined in NWS Directive 10-1703. This will most frequently be \"""A\" for a watch or \"Y\" for an advisory. """)
    event_number: Optional[int] = ApiField(description="""Event number. If this hazard refers to a national or regional center product (such as a Storm Prediction Center convective watch), this value will be the sequence number of that product. """)


