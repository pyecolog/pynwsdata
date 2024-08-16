# AlertGeocode

Lists of codes for NWS public zones and counties affected by the alert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ugc** | **List[str]** | A list of NWS public zone or county identifiers. | [optional] 
**same** | **List[str]** | A list of SAME (Specific Area Message Encoding) codes for affected counties. | [optional] 

## Example

```python
from pynwsdata.models.alert_geocode import AlertGeocode

# TODO update the JSON string below
json = "{}"
# create an instance of AlertGeocode from a JSON string
alert_geocode_instance = AlertGeocode.from_json(json)
# print the JSON string representation of the object
print(AlertGeocode.to_json())

# convert the object into a dict
alert_geocode_dict = alert_geocode_instance.to_dict()
# create an instance of AlertGeocode from a dict
alert_geocode_from_dict = AlertGeocode.from_dict(alert_geocode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


