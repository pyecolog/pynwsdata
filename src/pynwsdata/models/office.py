

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.json_ld_context import JsonLdContext
from pynwsdata.models.office_address import OfficeAddress
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class Office(ApiObject):
    """
    Office
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    type: Optional[str] = ApiField(default=None, alias="@type")
    id: Optional[str] = ApiField(default=None, alias="@id")
    id: Optional[str] = None
    name: Optional[str] = None
    address: Optional[OfficeAddress] = None
    telephone: Optional[str] = None
    fax_number: Optional[str] = ApiField(default=None, alias="faxNumber")
    email: Optional[str] = None
    same_as: Optional[str] = ApiField(default=None, alias="sameAs")
    nws_region: Optional[str] = ApiField(default=None, alias="nwsRegion")
    parent_organization: Optional[str] = ApiField(default=None, alias="parentOrganization")
    responsible_counties: Optional[list[str]] = ApiField(default=None, alias="responsibleCounties")
    responsible_forecast_zones: Optional[list[str]] = ApiField(default=None, alias="responsibleForecastZones")
    responsible_fire_zones: Optional[list[str]] = ApiField(default=None, alias="responsibleFireZones")
    approved_observation_stations: Optional[list[str]] = ApiField(default=None, alias="approvedObservationStations")

