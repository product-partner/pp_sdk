# SectionContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**prompt** | **str** |  | 
**query_string** | **str** |  | 
**section** | **str** |  | [optional] 
**organization** | **str** |  | [optional] [readonly] 
**created_by** | [**UserField**](UserField.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.section_context import SectionContext

# TODO update the JSON string below
json = "{}"
# create an instance of SectionContext from a JSON string
section_context_instance = SectionContext.from_json(json)
# print the JSON string representation of the object
print(SectionContext.to_json())

# convert the object into a dict
section_context_dict = section_context_instance.to_dict()
# create an instance of SectionContext from a dict
section_context_from_dict = SectionContext.from_dict(section_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


