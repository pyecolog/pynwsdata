# AlertAtomFeed

An alert feed in Atom format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**generator** | **str** |  | [optional] 
**updated** | **str** |  | [optional] 
**author** | [**AlertAtomFeedAuthor**](AlertAtomFeedAuthor.md) |  | [optional] 
**title** | **str** |  | [optional] 
**entry** | [**List[AlertAtomEntry]**](AlertAtomEntry.md) |  | [optional] 

## Example

```python
from pynwsdata.models.alert_atom_feed import AlertAtomFeed

# TODO update the JSON string below
json = "{}"
# create an instance of AlertAtomFeed from a JSON string
alert_atom_feed_instance = AlertAtomFeed.from_json(json)
# print the JSON string representation of the object
print(AlertAtomFeed.to_json())

# convert the object into a dict
alert_atom_feed_dict = alert_atom_feed_instance.to_dict()
# create an instance of AlertAtomFeed from a dict
alert_atom_feed_from_dict = AlertAtomFeed.from_dict(alert_atom_feed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


