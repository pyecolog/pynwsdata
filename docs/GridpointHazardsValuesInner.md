# GridpointHazardsValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_time** | [**ISO8601Interval**](ISO8601Interval.md) |  | 
**value** | [**List[GridpointHazardsValuesInnerValueInner]**](GridpointHazardsValuesInnerValueInner.md) |  | 

## Example

```python
from pynwsdata.models.gridpoint_hazards_values_inner import GridpointHazardsValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointHazardsValuesInner from a JSON string
gridpoint_hazards_values_inner_instance = GridpointHazardsValuesInner.from_json(json)
# print the JSON string representation of the object
print(GridpointHazardsValuesInner.to_json())

# convert the object into a dict
gridpoint_hazards_values_inner_dict = gridpoint_hazards_values_inner_instance.to_dict()
# create an instance of GridpointHazardsValuesInner from a dict
gridpoint_hazards_values_inner_from_dict = GridpointHazardsValuesInner.from_dict(gridpoint_hazards_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


