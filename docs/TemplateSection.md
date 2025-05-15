# TemplateSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**template** | **str** |  | 
**section** | **str** |  | 
**order** | **int** |  | [optional] 
**created_by** | [**UserField**](UserField.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**deleted** | **bool** |  | [optional] 

## Example

```python
from pp_sdk.models.template_section import TemplateSection

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSection from a JSON string
template_section_instance = TemplateSection.from_json(json)
# print the JSON string representation of the object
print(TemplateSection.to_json())

# convert the object into a dict
template_section_dict = template_section_instance.to_dict()
# create an instance of TemplateSection from a dict
template_section_from_dict = TemplateSection.from_dict(template_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


