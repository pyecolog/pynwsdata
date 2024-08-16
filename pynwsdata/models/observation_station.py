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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.quantitative_value import QuantitativeValue
from typing import Optional, Set
from typing_extensions import Self

class ObservationStation(BaseModel):
    """
    ObservationStation
    """ # noqa: E501
    context: Optional[JsonLdContext] = Field(default=None, alias="@context")
    geometry: Optional[StrictStr] = Field(default=None, description="A geometry represented in Well-Known Text (WKT) format.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[StrictStr] = Field(default=None, alias="@type")
    elevation: Optional[QuantitativeValue] = None
    station_identifier: Optional[StrictStr] = Field(default=None, alias="stationIdentifier")
    name: Optional[StrictStr] = None
    time_zone: Optional[StrictStr] = Field(default=None, alias="timeZone")
    forecast: Optional[StrictStr] = Field(default=None, description="A link to the NWS public forecast zone containing this station.")
    county: Optional[StrictStr] = Field(default=None, description="A link to the NWS county zone containing this station.")
    fire_weather_zone: Optional[StrictStr] = Field(default=None, description="A link to the NWS fire weather forecast zone containing this station.", alias="fireWeatherZone")
    __properties: ClassVar[List[str]] = ["@context", "geometry", "@id", "@type", "elevation", "stationIdentifier", "name", "timeZone", "forecast", "county", "fireWeatherZone"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['wx:ObservationStation']):
            raise ValueError("must be one of enum values ('wx:ObservationStation')")
        return value

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
        """Create an instance of ObservationStation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['@context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of elevation
        if self.elevation:
            _dict['elevation'] = self.elevation.to_dict()
        # set to None if geometry (nullable) is None
        # and model_fields_set contains the field
        if self.geometry is None and "geometry" in self.model_fields_set:
            _dict['geometry'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObservationStation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@context": JsonLdContext.from_dict(obj["@context"]) if obj.get("@context") is not None else None,
            "geometry": obj.get("geometry"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "elevation": QuantitativeValue.from_dict(obj["elevation"]) if obj.get("elevation") is not None else None,
            "stationIdentifier": obj.get("stationIdentifier"),
            "name": obj.get("name"),
            "timeZone": obj.get("timeZone"),
            "forecast": obj.get("forecast"),
            "county": obj.get("county"),
            "fireWeatherZone": obj.get("fireWeatherZone")
        })
        return _obj


