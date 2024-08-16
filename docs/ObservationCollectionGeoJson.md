# ObservationCollectionGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**type** | **str** |  | 
**features** | [**List[ObservationCollectionGeoJsonAllOfFeatures]**](ObservationCollectionGeoJsonAllOfFeatures.md) |  | 

## Example

```python
from pynwsdata.models.observation_collection_geo_json import ObservationCollectionGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationCollectionGeoJson from a JSON string
observation_collection_geo_json_instance = ObservationCollectionGeoJson.from_json(json)
# print the JSON string representation of the object
print(ObservationCollectionGeoJson.to_json())

# convert the object into a dict
observation_collection_geo_json_dict = observation_collection_geo_json_instance.to_dict()
# create an instance of ObservationCollectionGeoJson from a dict
observation_collection_geo_json_from_dict = ObservationCollectionGeoJson.from_dict(observation_collection_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


