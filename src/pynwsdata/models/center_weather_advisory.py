

from datetime import datetime
from typing import Any, ClassVar, Optional
from typing_extensions import Annotated
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.nws_center_weather_service_unit_id import NWSCenterWeatherServiceUnitId
from typing import Optional
from typing_extensions import Self


class CenterWeatherAdvisory(ApiObject):
    """
    CenterWeatherAdvisory
    """

    id: Optional[str] = None
    issue_time: Optional[datetime] = ApiField(default=None, alias="issueTime")
    cwsu: Optional[NWSCenterWeatherServiceUnitId] = None
    sequence: Optional[int] = ApiField(None, ge=101)
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    observed_property: Optional[str] = ApiField(default=None, alias="observedProperty")
    text: Optional[str] = None


