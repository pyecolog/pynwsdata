# GridpointForecastPeriod

An object containing forecast information for a specific time period (generally 12-hour or 1-hour). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Sequential period number. | [optional] 
**name** | **str** | A textual identifier for the period. This value will not be present for hourly forecasts.  | [optional] 
**start_time** | **datetime** | The starting time that this forecast period is valid for. | [optional] 
**end_time** | **datetime** | The ending time that this forecast period is valid for. | [optional] 
**is_daytime** | **bool** | Indicates whether this period is daytime or nighttime. | [optional] 
**temperature** | [**GridpointForecastPeriodTemperature**](GridpointForecastPeriodTemperature.md) |  | [optional] 
**temperature_unit** | **str** | The unit of the temperature value (Fahrenheit or Celsius). This property is deprecated. Future versions will indicate the unit within the quantitative value object for the temperature property. To make use of the future standard format now, set the \&quot;forecast_temperature_qv\&quot; feature flag on the request.  | [optional] 
**temperature_trend** | **str** | If not null, indicates a non-diurnal temperature trend for the period (either rising temperature overnight, or falling temperature during the day)  | [optional] 
**probability_of_precipitation** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**dewpoint** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**relative_humidity** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**wind_speed** | [**GridpointForecastPeriodWindSpeed**](GridpointForecastPeriodWindSpeed.md) |  | [optional] 
**wind_gust** | [**GridpointForecastPeriodWindGust**](GridpointForecastPeriodWindGust.md) |  | [optional] 
**wind_direction** | **str** | The prevailing direction of the wind for the period, using a 16-point compass. | [optional] 
**icon** | **str** | A link to an icon representing the forecast summary. | [optional] 
**short_forecast** | **str** | A brief textual forecast summary for the period. | [optional] 
**detailed_forecast** | **str** | A detailed textual forecast for the period. | [optional] 

## Example

```python
from pynwsdata.models.gridpoint_forecast_period import GridpointForecastPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointForecastPeriod from a JSON string
gridpoint_forecast_period_instance = GridpointForecastPeriod.from_json(json)
# print the JSON string representation of the object
print(GridpointForecastPeriod.to_json())

# convert the object into a dict
gridpoint_forecast_period_dict = gridpoint_forecast_period_instance.to_dict()
# create an instance of GridpointForecastPeriod from a dict
gridpoint_forecast_period_from_dict = GridpointForecastPeriod.from_dict(gridpoint_forecast_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


