# Goal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**goal_language** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**why_it_matters** | **str** |  | [optional] 
**prd** | [**List[DocumentListFieldInner]**](DocumentListFieldInner.md) | Can accept either a list of document IDs (strings) or a list of objects with id field | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**original_due_date** | **datetime** |  | [optional] 
**current_due_date** | **datetime** |  | [optional] 
**owner_users** | [**List[UserListOfUserFieldsInner]**](UserListOfUserFieldsInner.md) | Can accept either a list of user IDs (strings) or a list of objects with id field | [optional] 
**programs** | [**List[ProgramsListInner]**](ProgramsListInner.md) | Can accept either a list of program IDs (strings) or a list of objects with id field | [optional] 
**stakeholder_users** | [**List[UserListOfUserFieldsInner]**](UserListOfUserFieldsInner.md) | Can accept either a list of user IDs (strings) or a list of objects with id field | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**version** | **int** |  | [optional] 
**version_summary** | **str** |  | [optional] 
**created_by** | [**UserField**](UserField.md) |  | [optional] 
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


