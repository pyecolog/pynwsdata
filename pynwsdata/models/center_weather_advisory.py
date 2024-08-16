# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pynwsdata.models.nws_center_weather_service_unit_id import NWSCenterWeatherServiceUnitId
from typing import Optional, Set
from typing_extensions import Self

class CenterWeatherAdvisory(BaseModel):
    """
    CenterWeatherAdvisory
    """ # noqa: E501
    id: Optional[StrictStr] = None
    issue_time: Optional[datetime] = Field(default=None, alias="issueTime")
    cwsu: Optional[NWSCenterWeatherServiceUnitId] = None
    sequence: Optional[Annotated[int, Field(strict=True, ge=101)]] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    observed_property: Optional[StrictStr] = Field(default=None, alias="observedProperty")
    text: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "issueTime", "cwsu", "sequence", "start", "end", "observedProperty", "text"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CenterWeatherAdvisory from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CenterWeatherAdvisory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "issueTime": obj.get("issueTime"),
            "cwsu": obj.get("cwsu"),
            "sequence": obj.get("sequence"),
            "start": obj.get("start"),
            "end": obj.get("end"),
            "observedProperty": obj.get("observedProperty"),
            "text": obj.get("text")
        })
        return _obj


