# Observation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**elevation** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**station** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**raw_message** | **str** |  | [optional] 
**text_description** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**present_weather** | [**List[MetarPhenomenon]**](MetarPhenomenon.md) |  | [optional] 
**temperature** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**dewpoint** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**wind_direction** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**wind_speed** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**wind_gust** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**barometric_pressure** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**sea_level_pressure** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**visibility** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**max_temperature_last24_hours** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**min_temperature_last24_hours** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**precipitation_last_hour** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**precipitation_last3_hours** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**precipitation_last6_hours** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**relative_humidity** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**wind_chill** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**heat_index** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**cloud_layers** | [**List[ObservationCloudLayersInner]**](ObservationCloudLayersInner.md) |  | [optional] 

## Example

```python
from pynwsdata.models.observation import Observation

# TODO update the JSON string below
json = "{}"
# create an instance of Observation from a JSON string
observation_instance = Observation.from_json(json)
# print the JSON string representation of the object
print(Observation.to_json())

# convert the object into a dict
observation_dict = observation_instance.to_dict()
# create an instance of Observation from a dict
observation_from_dict = Observation.from_dict(observation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


