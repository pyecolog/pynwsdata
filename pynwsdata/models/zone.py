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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.nws_forecast_office_id import NWSForecastOfficeId
from pynwsdata.models.nws_zone_type import NWSZoneType
from pynwsdata.models.zone_state import ZoneState
from typing import Optional, Set
from typing_extensions import Self

class Zone(BaseModel):
    """
    Zone
    """ # noqa: E501
    context: Optional[JsonLdContext] = Field(default=None, alias="@context")
    geometry: Optional[StrictStr] = Field(default=None, description="A geometry represented in Well-Known Text (WKT) format.")
    id: Optional[StrictStr] = Field(default=None, alias="@id")
    type: Optional[StrictStr] = Field(default=None, alias="@type")
    id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="UGC identifier for a NWS forecast zone or county. The first two letters will correspond to either a state code or marine area code (see #/components/schemas/StateTerritoryCode and #/components/schemas/MarineAreaCode for lists of valid letter combinations). The third letter will be Z for public/fire zone or C for county. ")
    type: Optional[NWSZoneType] = None
    name: Optional[StrictStr] = None
    effective_date: Optional[datetime] = Field(default=None, alias="effectiveDate")
    expiration_date: Optional[datetime] = Field(default=None, alias="expirationDate")
    state: Optional[ZoneState] = None
    forecast_office: Optional[StrictStr] = Field(default=None, alias="forecastOffice")
    grid_identifier: Optional[StrictStr] = Field(default=None, alias="gridIdentifier")
    awips_location_identifier: Optional[StrictStr] = Field(default=None, alias="awipsLocationIdentifier")
    cwa: Optional[List[NWSForecastOfficeId]] = None
    forecast_offices: Optional[List[StrictStr]] = Field(default=None, alias="forecastOffices")
    time_zone: Optional[List[StrictStr]] = Field(default=None, alias="timeZone")
    observation_stations: Optional[List[StrictStr]] = Field(default=None, alias="observationStations")
    radar_station: Optional[StrictStr] = Field(default=None, alias="radarStation")
    __properties: ClassVar[List[str]] = ["@context", "geometry", "@id", "@type", "id", "type", "name", "effectiveDate", "expirationDate", "state", "forecastOffice", "gridIdentifier", "awipsLocationIdentifier", "cwa", "forecastOffices", "timeZone", "observationStations", "radarStation"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['wx:Zone']):
            raise ValueError("must be one of enum values ('wx:Zone')")
        return value

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$", value):
            raise ValueError(r"must validate the regular expression /^(A[KLMNRSZ]|C[AOT]|D[CE]|F[LM]|G[AMU]|I[ADLN]|K[SY]|L[ACEHMOS]|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[AHKMRSWZ]|S[CDL]|T[NX]|UT|V[AIT]|W[AIVY]|[HR]I)[CZ]\d{3}$/")
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
        """Create an instance of Zone from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if geometry (nullable) is None
        # and model_fields_set contains the field
        if self.geometry is None and "geometry" in self.model_fields_set:
            _dict['geometry'] = None

        # set to None if radar_station (nullable) is None
        # and model_fields_set contains the field
        if self.radar_station is None and "radar_station" in self.model_fields_set:
            _dict['radarStation'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Zone from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@context": JsonLdContext.from_dict(obj["@context"]) if obj.get("@context") is not None else None,
            "geometry": obj.get("geometry"),
            "@id": obj.get("@id"),
            "@type": obj.get("@type"),
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "effectiveDate": obj.get("effectiveDate"),
            "expirationDate": obj.get("expirationDate"),
            "state": ZoneState.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "forecastOffice": obj.get("forecastOffice"),
            "gridIdentifier": obj.get("gridIdentifier"),
            "awipsLocationIdentifier": obj.get("awipsLocationIdentifier"),
            "cwa": obj.get("cwa"),
            "forecastOffices": obj.get("forecastOffices"),
            "timeZone": obj.get("timeZone"),
            "observationStations": obj.get("observationStations"),
            "radarStation": obj.get("radarStation")
        })
        return _obj


