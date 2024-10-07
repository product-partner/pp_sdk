# PRD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**tags** | **str** |  | [optional] [readonly] 
**stakeholder_users** | **str** |  | [optional] [readonly] 
**programs** | **str** |  | [optional] [readonly] 
**created_by** | **str** |  | [optional] [readonly] 
**created_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.prd import PRD

# TODO update the JSON string below
json = "{}"
# create an instance of PRD from a JSON string
prd_instance = PRD.from_json(json)
# print the JSON string representation of the object
print(PRD.to_json())

# convert the object into a dict
prd_dict = prd_instance.to_dict()
# create an instance of PRD from a dict
prd_from_dict = PRD.from_dict(prd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


