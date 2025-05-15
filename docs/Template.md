# Template


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**target_models** | **List[str]** |  | [optional] 
**short_description** | **str** |  | [optional] 
**instructions** | **str** |  | [optional] 
**prompt** | **str** |  | 
**examples** | **List[str]** |  | [optional] 
**organization** | **str** |  | [optional] [readonly] 
**created_by** | [**UserField**](UserField.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**template_sections** | [**List[TemplateSection]**](TemplateSection.md) |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


