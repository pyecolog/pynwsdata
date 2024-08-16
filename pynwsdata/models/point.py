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
from typing_extensions import Annotated
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.nws_forecast_office_id import NWSForecastOfficeId
from pynwsdata.models.point_relative_location import PointRelativeLocation
from typing import Optional, Set
from typing_extensions import Self

class Point(BaseModel):
    """
    Point
    """ # noqa: E501
    context: Optional[JsonLdContext] = Field(default=None, alias="@context")
    geometry: Optional[StrictStr] = Field(default=None, description="A geometry represented in Well-Known Text (WKT) format.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[StrictStr] = Field(default=None, alias="@type")
    cwa: Optional[NWSForecastOfficeId] = None
    forecast_office: Optional[StrictStr] = Field(default=None, alias="forecastOffice")
    grid_id: Optional[NWSForecastOfficeId] = Field(default=None, alias="gridId")
    grid_x: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="gridX")
    grid_y: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="gridY")
    forecast: Optional[StrictStr] = None
    forecast_hourly: Optional[StrictStr] = Field(default=None, alias="forecastHourly")
    forecast_grid_data: Optional[StrictStr] = Field(default=None, alias="forecastGridData")
    observation_stations: Optional[StrictStr] = Field(default=None, alias="observationStations")
    relative_location: Optional[PointRelativeLocation] = Field(default=None, alias="relativeLocation")
    forecast_zone: Optional[StrictStr] = Field(default=None, alias="forecastZone")
    county: Optional[StrictStr] = None
    fire_weather_zone: Optional[StrictStr] = Field(default=None, alias="fireWeatherZone")
    time_zone: Optional[StrictStr] = Field(default=None, alias="timeZone")
    radar_station: Optional[StrictStr] = Field(default=None, alias="radarStation")
    __properties: ClassVar[List[str]] = ["@context", "geometry", "@id", "@type", "cwa", "forecastOffice", "gridId", "gridX", "gridY", "forecast", "forecastHourly", "forecastGridData", "observationStations", "relativeLocation", "forecastZone", "county", "fireWeatherZone", "timeZone", "radarStation"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['wx:Point']):
            raise ValueError("must be one of enum values ('wx:Point')")
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
        """Create an instance of Point from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of relative_location
        if self.relative_location:
            _dict['relativeLocation'] = self.relative_location.to_dict()
        # set to None if geometry (nullable) is None
        # and model_fields_set contains the field
        if self.geometry is None and "geometry" in self.model_fields_set:
            _dict['geometry'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Point from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@context": JsonLdContext.from_dict(obj["@context"]) if obj.get("@context") is not None else None,
            "geometry": obj.get("geometry"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "cwa": obj.get("cwa"),
            "forecastOffice": obj.get("forecastOffice"),
            "gridId": obj.get("gridId"),
            "gridX": obj.get("gridX"),
            "gridY": obj.get("gridY"),
            "forecast": obj.get("forecast"),
            "forecastHourly": obj.get("forecastHourly"),
            "forecastGridData": obj.get("forecastGridData"),
            "observationStations": obj.get("observationStations"),
            "relativeLocation": PointRelativeLocation.from_dict(obj["relativeLocation"]) if obj.get("relativeLocation") is not None else None,
            "forecastZone": obj.get("forecastZone"),
            "county": obj.get("county"),
            "fireWeatherZone": obj.get("fireWeatherZone"),
            "timeZone": obj.get("timeZone"),
            "radarStation": obj.get("radarStation")
        })
        return _obj


