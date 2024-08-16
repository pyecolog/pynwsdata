# ObservationStationJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | 
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
from pynwsdata.models.observation_station_json_ld import ObservationStationJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationStationJsonLd from a JSON string
observation_station_json_ld_instance = ObservationStationJsonLd.from_json(json)
# print the JSON string representation of the object
print(ObservationStationJsonLd.to_json())

# convert the object into a dict
observation_station_json_ld_dict = observation_station_json_ld_instance.to_dict()
# create an instance of ObservationStationJsonLd from a dict
observation_station_json_ld_from_dict = ObservationStationJsonLd.from_dict(observation_station_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


