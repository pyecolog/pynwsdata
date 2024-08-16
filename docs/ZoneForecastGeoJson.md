# ZoneForecastGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**ZoneForecast**](ZoneForecast.md) |  | 

## Example

```python
from pynwsdata.models.zone_forecast_geo_json import ZoneForecastGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneForecastGeoJson from a JSON string
zone_forecast_geo_json_instance = ZoneForecastGeoJson.from_json(json)
# print the JSON string representation of the object
print(ZoneForecastGeoJson.to_json())

# convert the object into a dict
zone_forecast_geo_json_dict = zone_forecast_geo_json_instance.to_dict()
# create an instance of ZoneForecastGeoJson from a dict
zone_forecast_geo_json_from_dict = ZoneForecastGeoJson.from_dict(zone_forecast_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


