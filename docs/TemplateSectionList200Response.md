# TemplateSectionList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TemplateSection]**](TemplateSection.md) |  | 

## Example

```python
from pp_sdk.models.template_section_list200_response import TemplateSectionList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSectionList200Response from a JSON string
template_section_list200_response_instance = TemplateSectionList200Response.from_json(json)
# print the JSON string representation of the object
print(TemplateSectionList200Response.to_json())

# convert the object into a dict
template_section_list200_response_dict = template_section_list200_response_instance.to_dict()
# create an instance of TemplateSectionList200Response from a dict
template_section_list200_response_from_dict = TemplateSectionList200Response.from_dict(template_section_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


