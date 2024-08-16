# AlertGeoJson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | [**GeoJsonGeometry**](GeoJsonGeometry.md) |  | 
**properties** | [**Alert**](Alert.md) |  | 

## Example

```python
from pynwsdata.models.alert_geo_json import AlertGeoJson

# TODO update the JSON string below
json = "{}"
# create an instance of AlertGeoJson from a JSON string
alert_geo_json_instance = AlertGeoJson.from_json(json)
# print the JSON string representation of the object
print(AlertGeoJson.to_json())

# convert the object into a dict
alert_geo_json_dict = alert_geo_json_instance.to_dict()
# create an instance of AlertGeoJson from a dict
alert_geo_json_from_dict = AlertGeoJson.from_dict(alert_geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


