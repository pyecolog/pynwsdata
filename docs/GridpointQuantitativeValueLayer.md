# GridpointQuantitativeValueLayer

A gridpoint layer consisting of quantitative values (numeric values with associated units of measure). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uom** | **str** | A string denoting a unit of measure, expressed in the format \&quot;{unit}\&quot; or \&quot;{namespace}:{unit}\&quot;. Units with the namespace \&quot;wmo\&quot; or \&quot;wmoUnit\&quot; are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace \&quot;nwsUnit\&quot; are currently custom and do not align to any standard. Units with no namespace or the namespace \&quot;uc\&quot; are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future.  | [optional] 
**values** | [**List[GridpointQuantitativeValueLayerValuesInner]**](GridpointQuantitativeValueLayerValuesInner.md) |  | 

## Example

```python
from pynwsdata.models.gridpoint_quantitative_value_layer import GridpointQuantitativeValueLayer

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointQuantitativeValueLayer from a JSON string
gridpoint_quantitative_value_layer_instance = GridpointQuantitativeValueLayer.from_json(json)
# print the JSON string representation of the object
print(GridpointQuantitativeValueLayer.to_json())

# convert the object into a dict
gridpoint_quantitative_value_layer_dict = gridpoint_quantitative_value_layer_instance.to_dict()
# create an instance of GridpointQuantitativeValueLayer from a dict
gridpoint_quantitative_value_layer_from_dict = GridpointQuantitativeValueLayer.from_dict(gridpoint_quantitative_value_layer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


