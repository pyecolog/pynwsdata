# AlertCollectionGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**type** | **str** |  | 
**features** | [**List[AlertCollectionGeoJsonAllOfFeatures]**](AlertCollectionGeoJsonAllOfFeatures.md) |  | 
**title** | **str** | A title describing the alert collection | [optional] 
**updated** | **datetime** | The last time a change occurred to this collection | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 

## Example

```python
from pynwsdata.models.alert_collection_geo_json import AlertCollectionGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of AlertCollectionGeoJson from a JSON string
alert_collection_geo_json_instance = AlertCollectionGeoJson.from_json(json)
# print the JSON string representation of the object
print(AlertCollectionGeoJson.to_json())

# convert the object into a dict
alert_collection_geo_json_dict = alert_collection_geo_json_instance.to_dict()
# create an instance of AlertCollectionGeoJson from a dict
alert_collection_geo_json_from_dict = AlertCollectionGeoJson.from_dict(alert_collection_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


