# GridpointWeatherValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_time** | [**ISO8601Interval**](ISO8601Interval.md) |  | 
**value** | [**List[GridpointWeatherValuesInnerValueInner]**](GridpointWeatherValuesInnerValueInner.md) |  | 

## Example

```python
from pynwsdata.models.gridpoint_weather_values_inner import GridpointWeatherValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointWeatherValuesInner from a JSON string
gridpoint_weather_values_inner_instance = GridpointWeatherValuesInner.from_json(json)
# print the JSON string representation of the object
print(GridpointWeatherValuesInner.to_json())

# convert the object into a dict
gridpoint_weather_values_inner_dict = gridpoint_weather_values_inner_instance.to_dict()
# create an instance of GridpointWeatherValuesInner from a dict
gridpoint_weather_values_inner_from_dict = GridpointWeatherValuesInner.from_dict(gridpoint_weather_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


