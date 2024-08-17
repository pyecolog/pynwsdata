

from datetime import datetime
from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.alert_collection_geo_json_all_of_features import AlertCollectionGeoJsonAllOfFeatures
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.pagination_info import PaginationInfo
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class AlertCollectionGeoJson(ApiObject):
    """
    AlertCollectionGeoJson
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    type: str
    features: list[AlertCollectionGeoJsonAllOfFeatures]
    title: Optional[str] = ApiField(default=None, description="""A title describing the alert collection""")
    updated: Optional[datetime] = ApiField(default=None, description="""The last time a change occurred to this collection""")
    pagination: Optional[PaginationInfo] = None

