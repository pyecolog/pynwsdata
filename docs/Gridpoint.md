# Gridpoint

Raw forecast data for a 2.5km grid square. This is a list of all potential data layers that may appear. Some layers may not be present in all areas. * temperature * dewpoint * maxTemperature * minTemperature * relativeHumidity * apparentTemperature * heatIndex * windChill * wetBulbGlobeTemperature * skyCover * windDirection * windSpeed * windGust * weather * hazards: Watch and advisory products in effect * probabilityOfPrecipitation * quantitativePrecipitation * iceAccumulation * snowfallAmount * snowLevel * ceilingHeight * visibility * transportWindSpeed * transportWindDirection * mixingHeight * hainesIndex * lightningActivityLevel * twentyFootWindSpeed * twentyFootWindDirection * waveHeight * wavePeriod * waveDirection * primarySwellHeight * primarySwellDirection * secondarySwellHeight * secondarySwellDirection * wavePeriod2 * windWaveHeight * dispersionIndex * pressure: Barometric pressure * probabilityOfTropicalStormWinds * probabilityOfHurricaneWinds * potentialOf15mphWinds * potentialOf25mphWinds * potentialOf35mphWinds * potentialOf45mphWinds * potentialOf20mphWindGusts * potentialOf30mphWindGusts * potentialOf40mphWindGusts * potentialOf50mphWindGusts * potentialOf60mphWindGusts * grasslandFireDangerIndex * probabilityOfThunder * davisStabilityIndex * atmosphericDispersionIndex * lowVisibilityOccurrenceRiskIndex * stability * redFlagThreatIndex 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_time** | **datetime** |  | [optional] 
**valid_times** | [**ISO8601Interval**](ISO8601Interval.md) |  | [optional] 
**elevation** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**forecast_office** | **str** |  | [optional] 
**grid_id** | **str** |  | [optional] 
**grid_x** | **int** |  | [optional] 
**grid_y** | **int** |  | [optional] 
**weather** | [**GridpointWeather**](GridpointWeather.md) |  | [optional] 
**hazards** | [**GridpointHazards**](GridpointHazards.md) |  | [optional] 

## Example

```python
from pynwsdata.models.gridpoint import Gridpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Gridpoint from a JSON string
gridpoint_instance = Gridpoint.from_json(json)
# print the JSON string representation of the object
print(Gridpoint.to_json())

# convert the object into a dict
gridpoint_dict = gridpoint_instance.to_dict()
# create an instance of Gridpoint from a dict
gridpoint_from_dict = Gridpoint.from_dict(gridpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


