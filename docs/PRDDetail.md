# PRDDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 
**programs** | [**List[ProgramBase]**](ProgramBase.md) |  | 
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
**goals** | **str** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.prd_detail import PRDDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PRDDetail from a JSON string
prd_detail_instance = PRDDetail.from_json(json)
# print the JSON string representation of the object
print(PRDDetail.to_json())

# convert the object into a dict
prd_detail_dict = prd_detail_instance.to_dict()
# create an instance of PRDDetail from a dict
prd_detail_from_dict = PRDDetail.from_dict(prd_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


