# GridpointHazards


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[GridpointHazardsValuesInner]**](GridpointHazardsValuesInner.md) |  | 

## Example

```python
from pynwsdata.models.gridpoint_hazards import GridpointHazards

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointHazards from a JSON string
gridpoint_hazards_instance = GridpointHazards.from_json(json)
# print the JSON string representation of the object
print(GridpointHazards.to_json())

# convert the object into a dict
gridpoint_hazards_dict = gridpoint_hazards_instance.to_dict()
# create an instance of GridpointHazards from a dict
gridpoint_hazards_from_dict = GridpointHazards.from_dict(gridpoint_hazards_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


