# RelativeLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**distance** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**bearing** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 

## Example

```python
from pynwsdata.models.relative_location import RelativeLocation

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeLocation from a JSON string
relative_location_instance = RelativeLocation.from_json(json)
# print the JSON string representation of the object
print(RelativeLocation.to_json())

# convert the object into a dict
relative_location_dict = relative_location_instance.to_dict()
# create an instance of RelativeLocation from a dict
relative_location_from_dict = RelativeLocation.from_dict(relative_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


