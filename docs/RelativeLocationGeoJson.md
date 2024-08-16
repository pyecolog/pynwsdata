# RelativeLocationGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**RelativeLocation**](RelativeLocation.md) |  | 

## Example

```python
from pynwsdata.models.relative_location_geo_json import RelativeLocationGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeLocationGeoJson from a JSON string
relative_location_geo_json_instance = RelativeLocationGeoJson.from_json(json)
# print the JSON string representation of the object
print(RelativeLocationGeoJson.to_json())

# convert the object into a dict
relative_location_geo_json_dict = relative_location_geo_json_instance.to_dict()
# create an instance of RelativeLocationGeoJson from a dict
relative_location_geo_json_from_dict = RelativeLocationGeoJson.from_dict(relative_location_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


