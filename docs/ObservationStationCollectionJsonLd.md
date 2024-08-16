# ObservationStationCollectionJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**graph** | [**List[ObservationStation]**](ObservationStation.md) |  | [optional] 
**observation_stations** | **List[str]** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 

## Example

```python
from pynwsdata.models.observation_station_collection_json_ld import ObservationStationCollectionJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationStationCollectionJsonLd from a JSON string
observation_station_collection_json_ld_instance = ObservationStationCollectionJsonLd.from_json(json)
# print the JSON string representation of the object
print(ObservationStationCollectionJsonLd.to_json())

# convert the object into a dict
observation_station_collection_json_ld_dict = observation_station_collection_json_ld_instance.to_dict()
# create an instance of ObservationStationCollectionJsonLd from a dict
observation_station_collection_json_ld_from_dict = ObservationStationCollectionJsonLd.from_dict(observation_station_collection_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


