# GeoJsonGeometry

A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[List[List[float]]]]** |  | 
**bbox** | **List[float]** | A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. | [optional] 

## Example

```python
from pynwsdata.models.geo_json_geometry import GeoJsonGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonGeometry from a JSON string
geo_json_geometry_instance = GeoJsonGeometry.from_json(json)
# print the JSON string representation of the object
print(GeoJsonGeometry.to_json())

# convert the object into a dict
geo_json_geometry_dict = geo_json_geometry_instance.to_dict()
# create an instance of GeoJsonGeometry from a dict
geo_json_geometry_from_dict = GeoJsonGeometry.from_dict(geo_json_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


