# CenterWeatherAdvisoryGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**CenterWeatherAdvisory**](CenterWeatherAdvisory.md) |  | 

## Example

```python
from pynwsdata.models.center_weather_advisory_geo_json import CenterWeatherAdvisoryGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of CenterWeatherAdvisoryGeoJson from a JSON string
center_weather_advisory_geo_json_instance = CenterWeatherAdvisoryGeoJson.from_json(json)
# print the JSON string representation of the object
print(CenterWeatherAdvisoryGeoJson.to_json())

# convert the object into a dict
center_weather_advisory_geo_json_dict = center_weather_advisory_geo_json_instance.to_dict()
# create an instance of CenterWeatherAdvisoryGeoJson from a dict
center_weather_advisory_geo_json_from_dict = CenterWeatherAdvisoryGeoJson.from_dict(center_weather_advisory_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


