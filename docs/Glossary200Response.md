# Glossary200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**JsonLdContext**](JsonLdContext.md) |  | [optional] 
**glossary** | [**List[Glossary200ResponseGlossaryInner]**](Glossary200ResponseGlossaryInner.md) | A list of glossary terms | [optional] 

## Example

```python
from pynwsdata.models.glossary200_response import Glossary200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Glossary200Response from a JSON string
glossary200_response_instance = Glossary200Response.from_json(json)
# print the JSON string representation of the object
print(Glossary200Response.to_json())

# convert the object into a dict
glossary200_response_dict = glossary200_response_instance.to_dict()
# create an instance of Glossary200Response from a dict
glossary200_response_from_dict = Glossary200Response.from_dict(glossary200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


