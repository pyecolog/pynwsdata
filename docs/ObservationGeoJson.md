# ObservationGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**Observation**](Observation.md) |  | 

## Example

```python
from pynwsdata.models.observation_geo_json import ObservationGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationGeoJson from a JSON string
observation_geo_json_instance = ObservationGeoJson.from_json(json)
# print the JSON string representation of the object
print(ObservationGeoJson.to_json())

# convert the object into a dict
observation_geo_json_dict = observation_geo_json_instance.to_dict()
# create an instance of ObservationGeoJson from a dict
observation_geo_json_from_dict = ObservationGeoJson.from_dict(observation_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


