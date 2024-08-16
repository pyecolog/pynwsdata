# AlertCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A title describing the alert collection | [optional] 
**updated** | **datetime** | The last time a change occurred to this collection | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 

## Example

```python
from pynwsdata.models.alert_collection import AlertCollection

# TODO update the JSON string below
json = "{}"
# create an instance of AlertCollection from a JSON string
alert_collection_instance = AlertCollection.from_json(json)
# print the JSON string representation of the object
print(AlertCollection.to_json())

# convert the object into a dict
alert_collection_dict = alert_collection_instance.to_dict()
# create an instance of AlertCollection from a dict
alert_collection_from_dict = AlertCollection.from_dict(alert_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


