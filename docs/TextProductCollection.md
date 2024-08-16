# TextProductCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**graph** | [**List[TextProduct]**](TextProduct.md) |  | [optional] 

## Example

```python
from pynwsdata.models.text_product_collection import TextProductCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TextProductCollection from a JSON string
text_product_collection_instance = TextProductCollection.from_json(json)
# print the JSON string representation of the object
print(TextProductCollection.to_json())

# convert the object into a dict
text_product_collection_dict = text_product_collection_instance.to_dict()
# create an instance of TextProductCollection from a dict
text_product_collection_from_dict = TextProductCollection.from_dict(text_product_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


