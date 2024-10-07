# Status


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**goal** | **str** |  | 
**goal_details** | [**GoalBase**](GoalBase.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_display** | **str** |  | [optional] [readonly] 
**var_date** | **datetime** |  | [optional] 
**status_note** | **str** |  | [optional] 
**path_to_green** | **str** |  | [optional] 
**publishing_state** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] [readonly] 
**created_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print(Status.to_json())

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_from_dict = Status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


