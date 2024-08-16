# GridpointHazardsValuesInnerValueInner

A value object representing an expected hazard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phenomenon** | **str** | Hazard code. This value will correspond to a P-VTEC phenomenon code as defined in NWS Directive 10-1703.  | 
**significance** | **str** | Significance code. This value will correspond to a P-VTEC significance code as defined in NWS Directive 10-1703. This will most frequently be \&quot;A\&quot; for a watch or \&quot;Y\&quot; for an advisory.  | 
**event_number** | **int** | Event number. If this hazard refers to a national or regional center product (such as a Storm Prediction Center convective watch), this value will be the sequence number of that product.  | 

## Example

```python
from pynwsdata.models.gridpoint_hazards_values_inner_value_inner import GridpointHazardsValuesInnerValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointHazardsValuesInnerValueInner from a JSON string
gridpoint_hazards_values_inner_value_inner_instance = GridpointHazardsValuesInnerValueInner.from_json(json)
# print the JSON string representation of the object
print(GridpointHazardsValuesInnerValueInner.to_json())

# convert the object into a dict
gridpoint_hazards_values_inner_value_inner_dict = gridpoint_hazards_values_inner_value_inner_instance.to_dict()
# create an instance of GridpointHazardsValuesInnerValueInner from a dict
gridpoint_hazards_values_inner_value_inner_from_dict = GridpointHazardsValuesInnerValueInner.from_dict(gridpoint_hazards_values_inner_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


