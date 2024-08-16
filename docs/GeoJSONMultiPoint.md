# GeoJSONMultiPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[float]]** |  | 
**bbox** | **List[float]** | A GeoJSON bounding box. Please refer to IETF RFC 7946 for information on the GeoJSON format. | [optional] 

## Example

```python
from pynwsdata.models.geo_json_multi_point import GeoJSONMultiPoint

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONMultiPoint from a JSON string
geo_json_multi_point_instance = GeoJSONMultiPoint.from_json(json)
# print the JSON string representation of the object
print(GeoJSONMultiPoint.to_json())

# convert the object into a dict
geo_json_multi_point_dict = geo_json_multi_point_instance.to_dict()
# create an instance of GeoJSONMultiPoint from a dict
geo_json_multi_point_from_dict = GeoJSONMultiPoint.from_dict(geo_json_multi_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


