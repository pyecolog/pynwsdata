# Glossary200ResponseGlossaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** | The term being defined | [optional] 
**definition** | **str** | A definition for the term | [optional] 

## Example

```python
from pynwsdata.models.glossary200_response_glossary_inner import Glossary200ResponseGlossaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of Glossary200ResponseGlossaryInner from a JSON string
glossary200_response_glossary_inner_instance = Glossary200ResponseGlossaryInner.from_json(json)
# print the JSON string representation of the object
print(Glossary200ResponseGlossaryInner.to_json())

# convert the object into a dict
glossary200_response_glossary_inner_dict = glossary200_response_glossary_inner_instance.to_dict()
# create an instance of Glossary200ResponseGlossaryInner from a dict
glossary200_response_glossary_inner_from_dict = Glossary200ResponseGlossaryInner.from_dict(glossary200_response_glossary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


