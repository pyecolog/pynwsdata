# GridpointWeatherValuesInnerValueInner

A value object representing expected weather phenomena.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coverage** | **str** |  | 
**weather** | **str** |  | 
**intensity** | **str** |  | 
**visibility** | [**QuantitativeValue**](QuantitativeValue.md) |  | 
**attributes** | **List[str]** |  | 

## Example

```python
from pynwsdata.models.gridpoint_weather_values_inner_value_inner import GridpointWeatherValuesInnerValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointWeatherValuesInnerValueInner from a JSON string
gridpoint_weather_values_inner_value_inner_instance = GridpointWeatherValuesInnerValueInner.from_json(json)
# print the JSON string representation of the object
print(GridpointWeatherValuesInnerValueInner.to_json())

# convert the object into a dict
gridpoint_weather_values_inner_value_inner_dict = gridpoint_weather_values_inner_value_inner_instance.to_dict()
# create an instance of GridpointWeatherValuesInnerValueInner from a dict
gridpoint_weather_values_inner_value_inner_from_dict = GridpointWeatherValuesInnerValueInner.from_dict(gridpoint_weather_values_inner_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


