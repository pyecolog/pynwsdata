# AlertAtomEntry

An alert entry in an Atom feed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**updated** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**author** | [**AlertAtomEntryAuthor**](AlertAtomEntryAuthor.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**event** | **str** |  | [optional] 
**sent** | **str** |  | [optional] 
**effective** | **str** |  | [optional] 
**expires** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**msg_type** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**urgency** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**certainty** | **str** |  | [optional] 
**area_desc** | **str** |  | [optional] 
**polygon** | **str** |  | [optional] 
**geocode** | [**List[AlertXMLParameter]**](AlertXMLParameter.md) |  | [optional] 
**parameter** | [**List[AlertXMLParameter]**](AlertXMLParameter.md) |  | [optional] 

## Example

```python
from pynwsdata.models.alert_atom_entry import AlertAtomEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AlertAtomEntry from a JSON string
alert_atom_entry_instance = AlertAtomEntry.from_json(json)
# print the JSON string representation of the object
print(AlertAtomEntry.to_json())

# convert the object into a dict
alert_atom_entry_dict = alert_atom_entry_instance.to_dict()
# create an instance of AlertAtomEntry from a dict
alert_atom_entry_from_dict = AlertAtomEntry.from_dict(alert_atom_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


