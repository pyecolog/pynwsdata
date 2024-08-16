# PointGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**Point**](Point.md) |  | 

## Example

```python
from pynwsdata.models.point_geo_json import PointGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of PointGeoJson from a JSON string
point_geo_json_instance = PointGeoJson.from_json(json)
# print the JSON string representation of the object
print(PointGeoJson.to_json())

# convert the object into a dict
point_geo_json_dict = point_geo_json_instance.to_dict()
# create an instance of PointGeoJson from a dict
point_geo_json_from_dict = PointGeoJson.from_dict(point_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


