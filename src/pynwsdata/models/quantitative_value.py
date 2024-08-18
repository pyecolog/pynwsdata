import pprint
import re  # noqa: F401

from typing import Any, ClassVar, Optional, Union
from typing_extensions import Annotated
from typing import Optional
from typing_extensions import Self
from pynwsdata.api_object import ApiObject, ApiField


class QuantitativeValue(ApiObject):
    """
    A structured value representing a measurement and its unit of measure. This object is a slighly modified version of the schema.org definition at https://schema.org/QuantitativeValue
    """

    value: Optional[Union[float, int]] = ApiField(
        default=None, description="A measured value")
    max_value: Optional[Union[float, int]] = ApiField(
        default=None, description="The maximum value of a range of measured values", alias="maxValue")
    min_value: Optional[Union[float, int]] = ApiField(
        default=None, description="The minimum value of a range of measured values", alias="minValue")
    unit_code: Optional[str] = ApiField(default=None, description="A string denoting a unit of measure, expressed in the format \"{unit}\" or \"{namespace}:{unit}\". Units with the namespace \"wmo\" or \"wmoUnit\" are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace \"nwsUnit\" are currently custom and do not align to any standard. Units with no namespace or the namespace \"uc\" are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future. ", alias="unitCode")
    quality_control: Optional[str] = ApiField(
        default=None, description="For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml ", alias="qualityControl")

    def __repr__(self):
        value = self.value
        if value is None:
            return super().__repr__()
        unit = self.unit_code
        if unit is None:
            suffix = ""
        else:
            suffix = " %s " % unit
        vmin = self.min_value
        vmax = self.max_value
        clsname = self.__class__.__name__
        if vmin is None and vmax is None:
            return "<%s %s%s>" % (clsname, value, suffix)
        elif vmin is None:
            return "<%s %s (max %s)%s>" % (clsname, value, vmax, suffix)
        elif vmax is None:
            return "<%s %s (min %s)%s>" % (clsname, value, vmin, suffix)
        else:
            return "<%s %s (min %s) (max %s)%s>" % (clsname, value, vmin, vmax, suffix)


class QuantitativeValueInterim(QuantitativeValue):

    data: Union[str, QuantitativeValue]
