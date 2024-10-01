

from typing import Any, ClassVar
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.gridpoint_hazards_values_inner_value_inner import GridpointHazardsValuesInnerValueInner
from pynwsdata.models.iso8601_interval import ISO8601Interval
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class GridpointHazardsValuesInner(ApiObject):
    """
    GridpointHazardsValuesInner
    """

    valid_time: ISO8601Interval.storage_type = ApiField(alias="validTime", interface_type=ISO8601Interval)
    value: list[GridpointHazardsValuesInnerValueInner]


