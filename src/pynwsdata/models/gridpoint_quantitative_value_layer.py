

from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.gridpoint_quantitative_value_layer_values_inner import GridpointQuantitativeValueLayerValuesInner
from typing import Optional
from typing_extensions import Self


class GridpointQuantitativeValueLayer(ApiObject):
    """
    A gridpoint layer consisting of quantitative values (numeric values with associated units of measure). 
    """

    uom: Optional[str] = ApiField(default=None, description="""A string denoting a unit of measure, expressed in the format \"""{unit}\" or \"{namespace}:{unit}\". Units with the namespace \"wmo\" or \"wmoUnit\" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace \"nwsUnit\" are currently custom and do not align to any standard. Units with no namespace or the namespace \"uc\" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. """)
    values: list[GridpointQuantitativeValueLayerValuesInner]

