# GridpointGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**Gridpoint**](Gridpoint.md) |  | 

## Example

```python
from pynwsdata.models.gridpoint_geo_json import GridpointGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointGeoJson from a JSON string
gridpoint_geo_json_instance = GridpointGeoJson.from_json(json)
# print the JSON string representation of the object
print(GridpointGeoJson.to_json())

# convert the object into a dict
gridpoint_geo_json_dict = gridpoint_geo_json_instance.to_dict()
# create an instance of GridpointGeoJson from a dict
gridpoint_geo_json_from_dict = GridpointGeoJson.from_dict(gridpoint_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


