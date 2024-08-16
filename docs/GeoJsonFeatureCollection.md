# GeoJsonFeatureCollection

A GeoJSON feature collection. Please refer to IETF RFC 7946 for information on the GeoJSON format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**type** | **str** |  | 
**features** | [**List[GeoJsonFeature]**](GeoJsonFeature.md) |  | 

## Example

```python
from pynwsdata.models.geo_json_feature_collection import GeoJsonFeatureCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonFeatureCollection from a JSON string
geo_json_feature_collection_instance = GeoJsonFeatureCollection.from_json(json)
# print the JSON string representation of the object
print(GeoJsonFeatureCollection.to_json())

# convert the object into a dict
geo_json_feature_collection_dict = geo_json_feature_collection_instance.to_dict()
# create an instance of GeoJsonFeatureCollection from a dict
geo_json_feature_collection_from_dict = GeoJsonFeatureCollection.from_dict(geo_json_feature_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


