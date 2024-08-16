# AlertReferencesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An API link to the prior alert. | [optional] 
**identifier** | **str** | The identifier of the alert message. | [optional] 
**sender** | **str** | The sender of the prior alert. | [optional] 
**sent** | **datetime** | The time the prior alert was sent. | [optional] 

## Example

```python
from pynwsdata.models.alert_references_inner import AlertReferencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlertReferencesInner from a JSON string
alert_references_inner_instance = AlertReferencesInner.from_json(json)
# print the JSON string representation of the object
print(AlertReferencesInner.to_json())

# convert the object into a dict
alert_references_inner_dict = alert_references_inner_instance.to_dict()
# create an instance of AlertReferencesInner from a dict
alert_references_inner_from_dict = AlertReferencesInner.from_dict(alert_references_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


