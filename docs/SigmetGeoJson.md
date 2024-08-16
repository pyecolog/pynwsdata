# SigmetGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**Sigmet**](Sigmet.md) |  | 

## Example

```python
from pynwsdata.models.sigmet_geo_json import SigmetGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of SigmetGeoJson from a JSON string
sigmet_geo_json_instance = SigmetGeoJson.from_json(json)
# print the JSON string representation of the object
print(SigmetGeoJson.to_json())

# convert the object into a dict
sigmet_geo_json_dict = sigmet_geo_json_instance.to_dict()
# create an instance of SigmetGeoJson from a dict
sigmet_geo_json_from_dict = SigmetGeoJson.from_dict(sigmet_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


