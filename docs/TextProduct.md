# TextProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**wmo_collective_id** | **str** |  | [optional] 
**issuing_office** | **str** |  | [optional] 
**issuance_time** | **datetime** |  | [optional] 
**product_code** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_text** | **str** |  | [optional] 

## Example

```python
from pynwsdata.models.text_product import TextProduct

# TODO update the JSON string below
json = "{}"
# create an instance of TextProduct from a JSON string
text_product_instance = TextProduct.from_json(json)
# print the JSON string representation of the object
print(TextProduct.to_json())

# convert the object into a dict
text_product_dict = text_product_instance.to_dict()
# create an instance of TextProduct from a dict
text_product_from_dict = TextProduct.from_dict(text_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


