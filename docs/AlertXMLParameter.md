# AlertXMLParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from pynwsdata.models.alert_xml_parameter import AlertXMLParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AlertXMLParameter from a JSON string
alert_xml_parameter_instance = AlertXMLParameter.from_json(json)
# print the JSON string representation of the object
print(AlertXMLParameter.to_json())

# convert the object into a dict
alert_xml_parameter_dict = alert_xml_parameter_instance.to_dict()
# create an instance of AlertXMLParameter from a dict
alert_xml_parameter_from_dict = AlertXMLParameter.from_dict(alert_xml_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


