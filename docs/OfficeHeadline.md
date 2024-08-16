# OfficeHeadline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**office** | **str** |  | [optional] 
**important** | **bool** |  | [optional] 
**issuance_time** | **datetime** |  | [optional] 
**link** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from pynwsdata.models.office_headline import OfficeHeadline

# TODO update the JSON string below
json = "{}"
# create an instance of OfficeHeadline from a JSON string
office_headline_instance = OfficeHeadline.from_json(json)
# print the JSON string representation of the object
print(OfficeHeadline.to_json())

# convert the object into a dict
office_headline_dict = office_headline_instance.to_dict()
# create an instance of OfficeHeadline from a dict
office_headline_from_dict = OfficeHeadline.from_dict(office_headline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


