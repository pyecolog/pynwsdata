# RelativeLocationJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**distance** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**bearing** | [**QuantitativeValue**](QuantitativeValue.md) |  | [optional] 
**geometry** | **str** | A geometry represented in Well-Known Text (WKT) format. | 

## Example

```python
from pynwsdata.models.relative_location_json_ld import RelativeLocationJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of RelativeLocationJsonLd from a JSON string
relative_location_json_ld_instance = RelativeLocationJsonLd.from_json(json)
# print the JSON string representation of the object
print(RelativeLocationJsonLd.to_json())

# convert the object into a dict
relative_location_json_ld_dict = relative_location_json_ld_instance.to_dict()
# create an instance of RelativeLocationJsonLd from a dict
relative_location_json_ld_from_dict = RelativeLocationJsonLd.from_dict(relative_location_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


