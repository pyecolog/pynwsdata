# AlertsTypes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_types** | **List[str]** | A list of recognized event types | [optional] 

## Example

```python
from pynwsdata.models.alerts_types200_response import AlertsTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsTypes200Response from a JSON string
alerts_types200_response_instance = AlertsTypes200Response.from_json(json)
# print the JSON string representation of the object
print(AlertsTypes200Response.to_json())

# convert the object into a dict
alerts_types200_response_dict = alerts_types200_response_instance.to_dict()
# create an instance of AlertsTypes200Response from a dict
alerts_types200_response_from_dict = AlertsTypes200Response.from_dict(alerts_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


