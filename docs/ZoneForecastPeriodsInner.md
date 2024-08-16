# ZoneForecastPeriodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | A sequential identifier number. | 
**name** | **str** | A textual description of the period. | 
**detailed_forecast** | **str** | A detailed textual forecast for the period. | 

## Example

```python
from pynwsdata.models.zone_forecast_periods_inner import ZoneForecastPeriodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneForecastPeriodsInner from a JSON string
zone_forecast_periods_inner_instance = ZoneForecastPeriodsInner.from_json(json)
# print the JSON string representation of the object
print(ZoneForecastPeriodsInner.to_json())

# convert the object into a dict
zone_forecast_periods_inner_dict = zone_forecast_periods_inner_instance.to_dict()
# create an instance of ZoneForecastPeriodsInner from a dict
zone_forecast_periods_inner_from_dict = ZoneForecastPeriodsInner.from_dict(zone_forecast_periods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


