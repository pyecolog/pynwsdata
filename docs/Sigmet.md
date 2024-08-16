# Sigmet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**issue_time** | **datetime** |  | [optional] 
**fir** | **str** |  | [optional] 
**atsu** | **str** | ATSU Identifier | [optional] 
**sequence** | **str** |  | [optional] 
**phenomenon** | **str** |  | [optional] 
**start** | **datetime** |  | [optional] 
**end** | **datetime** |  | [optional] 

## Example

```python
from pynwsdata.models.sigmet import Sigmet

# TODO update the JSON string below
json = "{}"
# create an instance of Sigmet from a JSON string
sigmet_instance = Sigmet.from_json(json)
# print the JSON string representation of the object
print(Sigmet.to_json())

# convert the object into a dict
sigmet_dict = sigmet_instance.to_dict()
# create an instance of Sigmet from a dict
sigmet_from_dict = Sigmet.from_dict(sigmet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


