# ZoneCollectionGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**type** | **str** |  | 
**features** | [**List[ZoneCollectionGeoJsonAllOfFeatures]**](ZoneCollectionGeoJsonAllOfFeatures.md) |  | 

## Example

```python
from pynwsdata.models.zone_collection_geo_json import ZoneCollectionGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneCollectionGeoJson from a JSON string
zone_collection_geo_json_instance = ZoneCollectionGeoJson.from_json(json)
# print the JSON string representation of the object
print(ZoneCollectionGeoJson.to_json())

# convert the object into a dict
zone_collection_geo_json_dict = zone_collection_geo_json_instance.to_dict()
# create an instance of ZoneCollectionGeoJson from a dict
zone_collection_geo_json_from_dict = ZoneCollectionGeoJson.from_dict(zone_collection_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


