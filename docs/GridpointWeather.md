# GridpointWeather


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[GridpointWeatherValuesInner]**](GridpointWeatherValuesInner.md) |  | 

## Example

```python
from pynwsdata.models.gridpoint_weather import GridpointWeather

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointWeather from a JSON string
gridpoint_weather_instance = GridpointWeather.from_json(json)
# print the JSON string representation of the object
print(GridpointWeather.to_json())

# convert the object into a dict
gridpoint_weather_dict = gridpoint_weather_instance.to_dict()
# create an instance of GridpointWeather from a dict
gridpoint_weather_from_dict = GridpointWeather.from_dict(gridpoint_weather_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


