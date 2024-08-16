# GridpointForecastJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | 
**units** | [**GridpointForecastUnits**](GridpointForecastUnits.md) |  | [optional] [default to GridpointForecastUnits.US]
**forecast_generator** | **str** | The internal generator class used to create the forecast text (used for NWS debugging). | [optional] 
**generated_at** | **datetime** | The time this forecast data was generated. | [optional] 
**update_time** | **datetime** | The last update time of the data this forecast was generated from. | [optional] 
**valid_times** | [**ISO8601Interval**](ISO8601Interval.md) |  | [optional] 
**elevation** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**periods** | [**List[GridpointForecastPeriod]**](GridpointForecastPeriod.md) | An array of forecast periods. | [optional] 

## Example

```python
from pynwsdata.models.gridpoint_forecast_json_ld import GridpointForecastJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointForecastJsonLd from a JSON string
gridpoint_forecast_json_ld_instance = GridpointForecastJsonLd.from_json(json)
# print the JSON string representation of the object
print(GridpointForecastJsonLd.to_json())

# convert the object into a dict
gridpoint_forecast_json_ld_dict = gridpoint_forecast_json_ld_instance.to_dict()
# create an instance of GridpointForecastJsonLd from a dict
gridpoint_forecast_json_ld_from_dict = GridpointForecastJsonLd.from_dict(gridpoint_forecast_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


