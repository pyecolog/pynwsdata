# AlertCollectionJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A title describing the alert collection | [optional] 
**updated** | **datetime** | The last time a change occurred to this collection | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**graph** | [**List[Alert]**](Alert.md) |  | [optional] 

## Example

```python
from pynwsdata.models.alert_collection_json_ld import AlertCollectionJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of AlertCollectionJsonLd from a JSON string
alert_collection_json_ld_instance = AlertCollectionJsonLd.from_json(json)
# print the JSON string representation of the object
print(AlertCollectionJsonLd.to_json())

# convert the object into a dict
alert_collection_json_ld_dict = alert_collection_json_ld_instance.to_dict()
# create an instance of AlertCollectionJsonLd from a dict
alert_collection_json_ld_from_dict = AlertCollectionJsonLd.from_dict(alert_collection_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


