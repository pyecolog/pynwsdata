

from datetime import datetime
from pyfields import Field
from timedelta_isoformat import timedelta
from typing import ClassVar, TypeAlias, Self

from pynwsdata.api_base import VALUE_TYPES, TransportInterface
from pynwsdata.api_object import ApiObject


DatetimeDuration: TypeAlias = tuple[datetime, datetime]

class ISO8601IntervalInterface(TransportInterface[str, tuple[datetime, datetime]]):

    def from_json_parsed(self, value: str) -> tuple[datetime, datetime]:
        return ISO8601Interval.from_json_parsed(value)

    def to_json_parsed(self, instance: tuple[datetime, datetime]) -> str:
        raise NotImplementedError


class ISO8601Interval(ApiObject):
    """
    A time interval in ISO 8601 format.

    This can be one of:
    1. Start and end time
    2. Start time and duration
    3. Duration and end time

    The string \"NOW\" can also be used in place of a start/end time.
    """

    storage_type: ClassVar[TypeAlias] = DatetimeDuration
    interface_type: ClassVar[type[TransportInterface[str, tuple[datetime, datetime]]]] = ISO8601IntervalInterface

    # value example, from a forecast series:
    #   <GridpointForecast:response>.valid_times = '2024-08-20T15:00:00+00:00/P7DT10H'

    @classmethod
    def from_json_parsed(self, value: str) -> DatetimeDuration:
        start, rest = value.split("/", 1)
        dt_start = datetime.fromisoformat(start)
        try:
            dt_end = datetime.fromisoformat(rest)
        except ValueError:
            duration = timedelta.fromisoformat(rest)
            return dt_start, dt_start + duration
        else:
            return dt_start, dt_end

