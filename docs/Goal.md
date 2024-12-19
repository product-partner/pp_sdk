# Goal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**goal_language** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**why_it_matters** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**original_due_date** | **datetime** |  | [optional] 
**current_due_date** | **datetime** |  | [optional] 
**owner_users** | [**List[StakeholderUsersInner]**](StakeholderUsersInner.md) |  | [optional] [readonly] 
**programs** | [**List[ProgramsInner]**](ProgramsInner.md) |  | [optional] [readonly] 
**stakeholder_users** | [**List[StakeholderUsersInner]**](StakeholderUsersInner.md) |  | [optional] [readonly] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] [readonly] 
**version** | **int** |  | [optional] 
**version_summary** | **str** |  | [optional] 
**created_by** | [**CreatedBy**](CreatedBy.md) |  | [optional] 
**status** | [**Status1**](Status1.md) |  | [optional] 

## Example

```python
from pp_sdk.models.goal import Goal

# TODO update the JSON string below
json = "{}"
# create an instance of Goal from a JSON string
goal_instance = Goal.from_json(json)
# print the JSON string representation of the object
print(Goal.to_json())

# convert the object into a dict
goal_dict = goal_instance.to_dict()
# create an instance of Goal from a dict
goal_from_dict = Goal.from_dict(goal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


