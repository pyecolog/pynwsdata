# Office


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**address** | [**OfficeAddress**](OfficeAddress.md) |  | [optional] 
**telephone** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**same_as** | **str** |  | [optional] 
**nws_region** | **str** |  | [optional] 
**parent_organization** | **str** |  | [optional] 
**responsible_counties** | **List[str]** |  | [optional] 
**responsible_forecast_zones** | **List[str]** |  | [optional] 
**responsible_fire_zones** | **List[str]** |  | [optional] 
**approved_observation_stations** | **List[str]** |  | [optional] 

## Example

```python
from pynwsdata.models.office import Office

# TODO update the JSON string below
json = "{}"
# create an instance of Office from a JSON string
office_instance = Office.from_json(json)
# print the JSON string representation of the object
print(Office.to_json())

# convert the object into a dict
office_dict = office_instance.to_dict()
# create an instance of Office from a dict
office_from_dict = Office.from_dict(office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


