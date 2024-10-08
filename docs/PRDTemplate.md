# PRDTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**organization** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 
**template** | **str** |  | 
**created_by** | [**CreatedBy**](CreatedBy.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.prd_template import PRDTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PRDTemplate from a JSON string
prd_template_instance = PRDTemplate.from_json(json)
# print the JSON string representation of the object
print(PRDTemplate.to_json())

# convert the object into a dict
prd_template_dict = prd_template_instance.to_dict()
# create an instance of PRDTemplate from a dict
prd_template_from_dict = PRDTemplate.from_dict(prd_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


