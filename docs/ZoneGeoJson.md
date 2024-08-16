# ZoneGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**Zone**](Zone.md) |  | 

## Example

```python
from pynwsdata.models.zone_geo_json import ZoneGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneGeoJson from a JSON string
zone_geo_json_instance = ZoneGeoJson.from_json(json)
# print the JSON string representation of the object
print(ZoneGeoJson.to_json())

# convert the object into a dict
zone_geo_json_dict = zone_geo_json_instance.to_dict()
# create an instance of ZoneGeoJson from a dict
zone_geo_json_from_dict = ZoneGeoJson.from_dict(zone_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


