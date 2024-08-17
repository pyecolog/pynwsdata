

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.center_weather_advisory import CenterWeatherAdvisory
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures(ApiObject):
    """
    CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures
    """

    properties: Optional[CenterWeatherAdvisory] = None


