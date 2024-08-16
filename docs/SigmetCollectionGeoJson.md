# SigmetCollectionGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**type** | **str** |  | 
**features** | [**List[SigmetGeoJson]**](SigmetGeoJson.md) |  | 

## Example

```python
from pynwsdata.models.sigmet_collection_geo_json import SigmetCollectionGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of SigmetCollectionGeoJson from a JSON string
sigmet_collection_geo_json_instance = SigmetCollectionGeoJson.from_json(json)
# print the JSON string representation of the object
print(SigmetCollectionGeoJson.to_json())

# convert the object into a dict
sigmet_collection_geo_json_dict = sigmet_collection_geo_json_instance.to_dict()
# create an instance of SigmetCollectionGeoJson from a dict
sigmet_collection_geo_json_from_dict = SigmetCollectionGeoJson.from_dict(sigmet_collection_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


