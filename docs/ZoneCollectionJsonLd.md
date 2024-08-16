# ZoneCollectionJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**graph** | [**List[Zone]**](Zone.md) |  | [optional] 

## Example

```python
from pynwsdata.models.zone_collection_json_ld import ZoneCollectionJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneCollectionJsonLd from a JSON string
zone_collection_json_ld_instance = ZoneCollectionJsonLd.from_json(json)
# print the JSON string representation of the object
print(ZoneCollectionJsonLd.to_json())

# convert the object into a dict
zone_collection_json_ld_dict = zone_collection_json_ld_instance.to_dict()
# create an instance of ZoneCollectionJsonLd from a dict
zone_collection_json_ld_from_dict = ZoneCollectionJsonLd.from_dict(zone_collection_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


