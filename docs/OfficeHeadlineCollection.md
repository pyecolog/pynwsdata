# OfficeHeadlineCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | 
**graph** | [**List[OfficeHeadline]**](OfficeHeadline.md) |  | 

## Example

```python
from pynwsdata.models.office_headline_collection import OfficeHeadlineCollection

# TODO update the JSON string below
json = "{}"
# create an instance of OfficeHeadlineCollection from a JSON string
office_headline_collection_instance = OfficeHeadlineCollection.from_json(json)
# print the JSON string representation of the object
print(OfficeHeadlineCollection.to_json())

# convert the object into a dict
office_headline_collection_dict = office_headline_collection_instance.to_dict()
# create an instance of OfficeHeadlineCollection from a dict
office_headline_collection_from_dict = OfficeHeadlineCollection.from_dict(office_headline_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


