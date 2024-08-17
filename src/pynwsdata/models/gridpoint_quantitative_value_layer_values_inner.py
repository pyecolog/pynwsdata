

from typing import Any, ClassVar, Optional, Union
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.iso8601_interval import ISO8601Interval
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class GridpointQuantitativeValueLayerValuesInner(ApiObject):
    """
    GridpointQuantitativeValueLayerValuesInner
    """

    valid_time: ISO8601Interval = ApiField(alias="validTime")
    value: Optional[Union[float, int]]


