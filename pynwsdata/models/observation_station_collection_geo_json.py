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
from pynwsdata.models.observation_station_collection_geo_json_all_of_features import ObservationStationCollectionGeoJsonAllOfFeatures
from pynwsdata.models.pagination_info import PaginationInfo
from typing import Optional, Set
from typing_extensions import Self

class ObservationStationCollectionGeoJson(BaseModel):
    """
    ObservationStationCollectionGeoJson
    """ # noqa: E501
    context: Optional[JsonLdContext] = Field(default=None, alias="@context")
    type: StrictStr
    features: List[ObservationStationCollectionGeoJsonAllOfFeatures]
    observation_stations: Optional[List[StrictStr]] = Field(default=None, alias="observationStations")
    pagination: Optional[PaginationInfo] = None
    __properties: ClassVar[List[str]] = ["@context", "type", "features", "observationStations", "pagination"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['FeatureCollection']):
            raise ValueError("must be one of enum values ('FeatureCollection')")
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
        """Create an instance of ObservationStationCollectionGeoJson from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item in self.features:
                if _item:
                    _items.append(_item.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObservationStationCollectionGeoJson from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "@context": JsonLdContext.from_dict(obj["@context"]) if obj.get("@context") is not None else None,
            "type": obj.get("type"),
            "features": [ObservationStationCollectionGeoJsonAllOfFeatures.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "observationStations": obj.get("observationStations"),
            "pagination": PaginationInfo.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None
        })
        return _obj


