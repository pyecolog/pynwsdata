

from typing import Any, ClassVar
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.gridpoint_hazards_values_inner import GridpointHazardsValuesInner
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class GridpointHazards(ApiObject):
    """
    GridpointHazards
    """

    values: list[GridpointHazardsValuesInner]


