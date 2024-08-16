# ISO8601Interval

A time interval in ISO 8601 format. This can be one of:      1. Start and end time     2. Start time and duration     3. Duration and end time The string \"NOW\" can also be used in place of a start/end time. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from pynwsdata.models.iso8601_interval import ISO8601Interval

# TODO update the JSON string below
json = "{}"
# create an instance of ISO8601Interval from a JSON string
iso8601_interval_instance = ISO8601Interval.from_json(json)
# print the JSON string representation of the object
print(ISO8601Interval.to_json())

# convert the object into a dict
iso8601_interval_dict = iso8601_interval_instance.to_dict()
# create an instance of ISO8601Interval from a dict
iso8601_interval_from_dict = ISO8601Interval.from_dict(iso8601_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


