# PointJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**cwa** | [**NWSForecastOfficeId**](NWSForecastOfficeId.md) |  | [optional] 
**forecast_office** | **str** |  | [optional] 
**grid_id** | [**NWSForecastOfficeId**](NWSForecastOfficeId.md) |  | [optional] 
**grid_x** | **int** |  | [optional] 
**grid_y** | **int** |  | [optional] 
**forecast** | **str** |  | [optional] 
**forecast_hourly** | **str** |  | [optional] 
**forecast_grid_data** | **str** |  | [optional] 
**observation_stations** | **str** |  | [optional] 
**relative_location** | [**PointRelativeLocation**](PointRelativeLocation.md) |  | [optional] 
**forecast_zone** | **str** |  | [optional] 
**county** | **str** |  | [optional] 
**fire_weather_zone** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**radar_station** | **str** |  | [optional] 

## Example

```python
from pynwsdata.models.point_json_ld import PointJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of PointJsonLd from a JSON string
point_json_ld_instance = PointJsonLd.from_json(json)
# print the JSON string representation of the object
print(PointJsonLd.to_json())

# convert the object into a dict
point_json_ld_dict = point_json_ld_instance.to_dict()
# create an instance of PointJsonLd from a dict
point_json_ld_from_dict = PointJsonLd.from_dict(point_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


