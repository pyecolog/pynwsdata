# AlertJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Alert]**](Alert.md) |  | [optional] 

## Example

```python
from pynwsdata.models.alert_json_ld import AlertJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of AlertJsonLd from a JSON string
alert_json_ld_instance = AlertJsonLd.from_json(json)
# print the JSON string representation of the object
print(AlertJsonLd.to_json())

# convert the object into a dict
alert_json_ld_dict = alert_json_ld_instance.to_dict()
# create an instance of AlertJsonLd from a dict
alert_json_ld_from_dict = AlertJsonLd.from_dict(alert_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


