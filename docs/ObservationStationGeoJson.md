# ObservationStationGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**ObservationStation**](ObservationStation.md) |  | 

## Example

```python
from pynwsdata.models.observation_station_geo_json import ObservationStationGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationStationGeoJson from a JSON string
observation_station_geo_json_instance = ObservationStationGeoJson.from_json(json)
# print the JSON string representation of the object
print(ObservationStationGeoJson.to_json())

# convert the object into a dict
observation_station_geo_json_dict = observation_station_geo_json_instance.to_dict()
# create an instance of ObservationStationGeoJson from a dict
observation_station_geo_json_from_dict = ObservationStationGeoJson.from_dict(observation_station_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


