# MetarPhenomenon

An object representing a decoded METAR phenomenon string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intensity** | **str** |  | 
**modifier** | **str** |  | 
**weather** | **str** |  | 
**raw_string** | **str** |  | 
**in_vicinity** | **bool** |  | [optional] 

## Example

```python
from pynwsdata.models.metar_phenomenon import MetarPhenomenon

# TODO update the JSON string below
json = "{}"
# create an instance of MetarPhenomenon from a JSON string
metar_phenomenon_instance = MetarPhenomenon.from_json(json)
# print the JSON string representation of the object
print(MetarPhenomenon.to_json())

# convert the object into a dict
metar_phenomenon_dict = metar_phenomenon_instance.to_dict()
# create an instance of MetarPhenomenon from a dict
metar_phenomenon_from_dict = MetarPhenomenon.from_dict(metar_phenomenon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


