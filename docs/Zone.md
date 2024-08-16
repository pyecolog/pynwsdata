# Zone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**id** | **str** | UGC identifier for a NWS forecast zone or county. The first two letters will correspond to either a state code or marine area code (see #/components/schemas/StateTerritoryCode and #/components/schemas/MarineAreaCode for lists of valid letter combinations). The third letter will be Z for public/fire zone or C for county.  | [optional] 
**type** | [**NWSZoneType**](NWSZoneType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**effective_date** | **datetime** |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**state** | [**ZoneState**](ZoneState.md) |  | [optional] 
**forecast_office** | **str** |  | [optional] 
**grid_identifier** | **str** |  | [optional] 
**awips_location_identifier** | **str** |  | [optional] 
**cwa** | [**List[NWSForecastOfficeId]**](NWSForecastOfficeId.md) |  | [optional] 
**forecast_offices** | **List[str]** |  | [optional] 
**time_zone** | **List[str]** |  | [optional] 
**observation_stations** | **List[str]** |  | [optional] 
**radar_station** | **str** |  | [optional] 

## Example

```python
from pynwsdata.models.zone import Zone

# TODO update the JSON string below
json = "{}"
# create an instance of Zone from a JSON string
zone_instance = Zone.from_json(json)
# print the JSON string representation of the object
print(Zone.to_json())

# convert the object into a dict
zone_dict = zone_instance.to_dict()
# create an instance of Zone from a dict
zone_from_dict = Zone.from_dict(zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


