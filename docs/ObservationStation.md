# ObservationStation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**elevation** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**station_identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**forecast** | **str** | A link to the NWS public forecast zone containing this station. | [optional] 
**county** | **str** | A link to the NWS county zone containing this station. | [optional] 
**fire_weather_zone** | **str** | A link to the NWS fire weather forecast zone containing this station. | [optional] 

## Example

```python
from pynwsdata.models.observation_station import ObservationStation

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationStation from a JSON string
observation_station_instance = ObservationStation.from_json(json)
# print the JSON string representation of the object
print(ObservationStation.to_json())

# convert the object into a dict
observation_station_dict = observation_station_instance.to_dict()
# create an instance of ObservationStation from a dict
observation_station_from_dict = ObservationStation.from_dict(observation_station_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


