# AlertsActiveCount200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of active alerts | [optional] 
**land** | **int** | The total number of active alerts affecting land zones | [optional] 
**marine** | **int** | The total number of active alerts affecting marine zones | [optional] 
**regions** | **Dict[str, int]** | Active alerts by marine region | [optional] 
**areas** | **Dict[str, int]** | Active alerts by area (state/territory) | [optional] 
**zones** | **Dict[str, int]** | Active alerts by NWS public zone or county code | [optional] 

## Example

```python
from pynwsdata.models.alerts_active_count200_response import AlertsActiveCount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsActiveCount200Response from a JSON string
alerts_active_count200_response_instance = AlertsActiveCount200Response.from_json(json)
# print the JSON string representation of the object
print(AlertsActiveCount200Response.to_json())

# convert the object into a dict
alerts_active_count200_response_dict = alerts_active_count200_response_instance.to_dict()
# create an instance of AlertsActiveCount200Response from a dict
alerts_active_count200_response_from_dict = AlertsActiveCount200Response.from_dict(alerts_active_count200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


