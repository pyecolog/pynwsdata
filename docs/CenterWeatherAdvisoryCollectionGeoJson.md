# CenterWeatherAdvisoryCollectionGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**type** | **str** |  | 
**features** | [**List[CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures]**](CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures.md) |  | 

## Example

```python
from pynwsdata.models.center_weather_advisory_collection_geo_json import CenterWeatherAdvisoryCollectionGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of CenterWeatherAdvisoryCollectionGeoJson from a JSON string
center_weather_advisory_collection_geo_json_instance = CenterWeatherAdvisoryCollectionGeoJson.from_json(json)
# print the JSON string representation of the object
print(CenterWeatherAdvisoryCollectionGeoJson.to_json())

# convert the object into a dict
center_weather_advisory_collection_geo_json_dict = center_weather_advisory_collection_geo_json_instance.to_dict()
# create an instance of CenterWeatherAdvisoryCollectionGeoJson from a dict
center_weather_advisory_collection_geo_json_from_dict = CenterWeatherAdvisoryCollectionGeoJson.from_dict(center_weather_advisory_collection_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


