

from typing import Any, ClassVar
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.metar_sky_coverage import MetarSkyCoverage
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ObservationCloudLayersInner(ApiObject):
    """
    ObservationCloudLayersInner
    """

    base: QuantitativeValue
    amount: MetarSkyCoverage


