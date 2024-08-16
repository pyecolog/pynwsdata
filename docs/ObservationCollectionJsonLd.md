# ObservationCollectionJsonLd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**graph** | [**List[Observation]**](Observation.md) |  | [optional] 

## Example

```python
from pynwsdata.models.observation_collection_json_ld import ObservationCollectionJsonLd

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationCollectionJsonLd from a JSON string
observation_collection_json_ld_instance = ObservationCollectionJsonLd.from_json(json)
# print the JSON string representation of the object
print(ObservationCollectionJsonLd.to_json())

# convert the object into a dict
observation_collection_json_ld_dict = observation_collection_json_ld_instance.to_dict()
# create an instance of ObservationCollectionJsonLd from a dict
observation_collection_json_ld_from_dict = ObservationCollectionJsonLd.from_dict(observation_collection_json_ld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


