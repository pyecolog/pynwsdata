# ObservationCloudLayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**QuantitativeValue**](QuantitativeValue.md) |  | 
**amount** | [**MetarSkyCoverage**](MetarSkyCoverage.md) |  | 

## Example

```python
from pynwsdata.models.observation_cloud_layers_inner import ObservationCloudLayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationCloudLayersInner from a JSON string
observation_cloud_layers_inner_instance = ObservationCloudLayersInner.from_json(json)
# print the JSON string representation of the object
print(ObservationCloudLayersInner.to_json())

# convert the object into a dict
observation_cloud_layers_inner_dict = observation_cloud_layers_inner_instance.to_dict()
# create an instance of ObservationCloudLayersInner from a dict
observation_cloud_layers_inner_from_dict = ObservationCloudLayersInner.from_dict(observation_cloud_layers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


