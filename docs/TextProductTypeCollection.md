# TextProductTypeCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**graph** | [**List[TextProductTypeCollectionGraphInner]**](TextProductTypeCollectionGraphInner.md) |  | [optional] 

## Example

```python
from pynwsdata.models.text_product_type_collection import TextProductTypeCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TextProductTypeCollection from a JSON string
text_product_type_collection_instance = TextProductTypeCollection.from_json(json)
# print the JSON string representation of the object
print(TextProductTypeCollection.to_json())

# convert the object into a dict
text_product_type_collection_dict = text_product_type_collection_instance.to_dict()
# create an instance of TextProductTypeCollection from a dict
text_product_type_collection_from_dict = TextProductTypeCollection.from_dict(text_product_type_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


