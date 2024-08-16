# PointRelativeLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **str** |  | 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | 
**properties** | [**RelativeLocation**](RelativeLocation.md) |  | 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**distance** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**bearing** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 

## Example

```python
from pynwsdata.models.point_relative_location import PointRelativeLocation

# TODO update the JSON string below
json = "{}"
# create an instance of PointRelativeLocation from a JSON string
point_relative_location_instance = PointRelativeLocation.from_json(json)
# print the JSON string representation of the object
print(PointRelativeLocation.to_json())

# convert the object into a dict
point_relative_location_dict = point_relative_location_instance.to_dict()
# create an instance of PointRelativeLocation from a dict
point_relative_location_from_dict = PointRelativeLocation.from_dict(point_relative_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


