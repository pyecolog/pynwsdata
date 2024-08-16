# IconsSummary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**icons** | [**Dict[str, IconsSummary200ResponseIconsValue]**](IconsSummary200ResponseIconsValue.md) |  | 

## Example

```python
from pynwsdata.models.icons_summary200_response import IconsSummary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of IconsSummary200Response from a JSON string
icons_summary200_response_instance = IconsSummary200Response.from_json(json)
# print the JSON string representation of the object
print(IconsSummary200Response.to_json())

# convert the object into a dict
icons_summary200_response_dict = icons_summary200_response_instance.to_dict()
# create an instance of IconsSummary200Response from a dict
icons_summary200_response_from_dict = IconsSummary200Response.from_dict(icons_summary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


