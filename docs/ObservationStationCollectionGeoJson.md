# ObservationStationCollectionGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**type** | **str** |  | 
**features** | [**List[ObservationStationCollectionGeoJsonAllOfFeatures]**](ObservationStationCollectionGeoJsonAllOfFeatures.md) |  | 
**observation_stations** | **List[str]** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 

## Example

```python
from pynwsdata.models.observation_station_collection_geo_json import ObservationStationCollectionGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationStationCollectionGeoJson from a JSON string
observation_station_collection_geo_json_instance = ObservationStationCollectionGeoJson.from_json(json)
# print the JSON string representation of the object
print(ObservationStationCollectionGeoJson.to_json())

# convert the object into a dict
observation_station_collection_geo_json_dict = observation_station_collection_geo_json_instance.to_dict()
# create an instance of ObservationStationCollectionGeoJson from a dict
observation_station_collection_geo_json_from_dict = ObservationStationCollectionGeoJson.from_dict(observation_station_collection_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


