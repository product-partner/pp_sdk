# UserStory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**prd** | [**PRDReference**](PRDReference.md) |  | [optional] 
**as_a** | **str** |  | [optional] 
**i_want_to** | **str** |  | [optional] 
**so_that** | **str** |  | [optional] 
**freetext_override** | **str** |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**due_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] [readonly] 
**created_by** | [**CreatedBy**](CreatedBy.md) |  | [optional] 

## Example

```python
from pp_sdk.models.user_story import UserStory

# TODO update the JSON string below
json = "{}"
# create an instance of UserStory from a JSON string
user_story_instance = UserStory.from_json(json)
# print the JSON string representation of the object
print(UserStory.to_json())

# convert the object into a dict
user_story_dict = user_story_instance.to_dict()
# create an instance of UserStory from a dict
user_story_from_dict = UserStory.from_dict(user_story_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


