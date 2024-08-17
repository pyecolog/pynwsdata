

from typing import Any, ClassVar
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class ZoneForecastPeriodsInner(ApiObject):
    """
    ZoneForecastPeriodsInner
    """

    number: int = ApiField(description="""A sequential identifier number.""")
    name: str = ApiField(description="""A textual description of the period.""")
    detailed_forecast: str = ApiField(description="""A detailed textual forecast for the period.""", alias="detailedForecast")


