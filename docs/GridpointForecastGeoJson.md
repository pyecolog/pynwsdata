# GridpointForecastGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**GridpointForecast**](GridpointForecast.md) |  | 

## Example

```python
from pynwsdata.models.gridpoint_forecast_geo_json import GridpointForecastGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointForecastGeoJson from a JSON string
gridpoint_forecast_geo_json_instance = GridpointForecastGeoJson.from_json(json)
# print the JSON string representation of the object
print(GridpointForecastGeoJson.to_json())

# convert the object into a dict
gridpoint_forecast_geo_json_dict = gridpoint_forecast_geo_json_instance.to_dict()
# create an instance of GridpointForecastGeoJson from a dict
gridpoint_forecast_geo_json_from_dict = GridpointForecastGeoJson.from_dict(gridpoint_forecast_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


