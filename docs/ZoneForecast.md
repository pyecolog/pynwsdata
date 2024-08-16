# ZoneForecast

An object representing a zone area forecast.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | [optional] 
**zone** | **str** | An API link to the zone this forecast is for. | [optional] 
**updated** | **datetime** | The time this zone forecast product was published. | [optional] 
**periods** | [**List[ZoneForecastPeriodsInner]**](ZoneForecastPeriodsInner.md) | An array of forecast periods. | [optional] 

## Example

```python
from pynwsdata.models.zone_forecast import ZoneForecast

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneForecast from a JSON string
zone_forecast_instance = ZoneForecast.from_json(json)
# print the JSON string representation of the object
print(ZoneForecast.to_json())

# convert the object into a dict
zone_forecast_dict = zone_forecast_instance.to_dict()
# create an instance of ZoneForecast from a dict
zone_forecast_from_dict = ZoneForecast.from_dict(zone_forecast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


