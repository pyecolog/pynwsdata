# OfficeAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 
**address_locality** | **str** |  | [optional] 
**address_region** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from pynwsdata.models.office_address import OfficeAddress

# TODO update the JSON string below
json = "{}"
# create an instance of OfficeAddress from a JSON string
office_address_instance = OfficeAddress.from_json(json)
# print the JSON string representation of the object
print(OfficeAddress.to_json())

# convert the object into a dict
office_address_dict = office_address_instance.to_dict()
# create an instance of OfficeAddress from a dict
office_address_from_dict = OfficeAddress.from_dict(office_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


