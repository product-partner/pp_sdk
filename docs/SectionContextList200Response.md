# SectionContextList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SectionContext]**](SectionContext.md) |  | 

## Example

```python
from pp_sdk.models.section_context_list200_response import SectionContextList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SectionContextList200Response from a JSON string
section_context_list200_response_instance = SectionContextList200Response.from_json(json)
# print the JSON string representation of the object
print(SectionContextList200Response.to_json())

# convert the object into a dict
section_context_list200_response_dict = section_context_list200_response_instance.to_dict()
# create an instance of SectionContextList200Response from a dict
section_context_list200_response_from_dict = SectionContextList200Response.from_dict(section_context_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


