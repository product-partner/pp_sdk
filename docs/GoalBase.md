# GoalBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**goal_language** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.goal_base import GoalBase

# TODO update the JSON string below
json = "{}"
# create an instance of GoalBase from a JSON string
goal_base_instance = GoalBase.from_json(json)
# print the JSON string representation of the object
print GoalBase.to_json()

# convert the object into a dict
goal_base_dict = goal_base_instance.to_dict()
# create an instance of GoalBase from a dict
goal_base_from_dict = GoalBase.from_dict(goal_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


