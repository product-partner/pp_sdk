# PRD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 
**programs** | [**List[ProgramBase]**](ProgramBase.md) |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**due_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] [readonly] 
**owner_user** | [**UserBase**](UserBase.md) |  | [optional] 
**stakeholder_users** | [**List[UserBase]**](UserBase.md) |  | [optional] [readonly] 
**created_by** | [**UserBase**](UserBase.md) |  | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 

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


