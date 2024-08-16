# TextProductLocationCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**locations** | **Dict[str, Optional[str]]** |  | [optional] 

## Example

```python
from pynwsdata.models.text_product_location_collection import TextProductLocationCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TextProductLocationCollection from a JSON string
text_product_location_collection_instance = TextProductLocationCollection.from_json(json)
# print the JSON string representation of the object
print(TextProductLocationCollection.to_json())

# convert the object into a dict
text_product_location_collection_dict = text_product_location_collection_instance.to_dict()
# create an instance of TextProductLocationCollection from a dict
text_product_location_collection_from_dict = TextProductLocationCollection.from_dict(text_product_location_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


