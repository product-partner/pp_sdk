# GoalPicker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**goal_language** | **str** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.goal_picker import GoalPicker

# TODO update the JSON string below
json = "{}"
# create an instance of GoalPicker from a JSON string
goal_picker_instance = GoalPicker.from_json(json)
# print the JSON string representation of the object
print(GoalPicker.to_json())

# convert the object into a dict
goal_picker_dict = goal_picker_instance.to_dict()
# create an instance of GoalPicker from a dict
goal_picker_from_dict = GoalPicker.from_dict(goal_picker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


