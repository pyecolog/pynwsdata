# CenterWeatherAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**issue_time** | **datetime** |  | [optional] 
**cwsu** | [**NWSCenterWeatherServiceUnitId**](NWSCenterWeatherServiceUnitId.md) |  | [optional] 
**sequence** | **int** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 
**observed_property** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from pynwsdata.models.center_weather_advisory import CenterWeatherAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of CenterWeatherAdvisory from a JSON string
center_weather_advisory_instance = CenterWeatherAdvisory.from_json(json)
# print the JSON string representation of the object
print(CenterWeatherAdvisory.to_json())

# convert the object into a dict
center_weather_advisory_dict = center_weather_advisory_instance.to_dict()
# create an instance of CenterWeatherAdvisory from a dict
center_weather_advisory_from_dict = CenterWeatherAdvisory.from_dict(center_weather_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


