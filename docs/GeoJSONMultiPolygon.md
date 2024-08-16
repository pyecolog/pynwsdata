# GeoJSONMultiPolygon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[List[List[float]]]]** |  | 
**bbox** | **List[float]** | A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. | [optional] 

## Example

```python
from pynwsdata.models.geo_json_multi_polygon import GeoJSONMultiPolygon

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONMultiPolygon from a JSON string
geo_json_multi_polygon_instance = GeoJSONMultiPolygon.from_json(json)
# print the JSON string representation of the object
print(GeoJSONMultiPolygon.to_json())

# convert the object into a dict
geo_json_multi_polygon_dict = geo_json_multi_polygon_instance.to_dict()
# create an instance of GeoJSONMultiPolygon from a dict
geo_json_multi_polygon_from_dict = GeoJSONMultiPolygon.from_dict(geo_json_multi_polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


