# UserstoriesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prd** | **str** | PRD UUID | 
**as_a** | **str** |  | [optional] 
**i_want_to** | **str** |  | [optional] 
**so_that** | **str** |  | [optional] 
**freetext_override** | **str** |  | [optional] 
**acceptance_criteria** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**tags** | **List[str]** | List of tag UUIDs | [optional] 

## Example

```python
from pp_sdk.models.userstories_create_request import UserstoriesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserstoriesCreateRequest from a JSON string
userstories_create_request_instance = UserstoriesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(UserstoriesCreateRequest.to_json())

# convert the object into a dict
userstories_create_request_dict = userstories_create_request_instance.to_dict()
# create an instance of UserstoriesCreateRequest from a dict
userstories_create_request_from_dict = UserstoriesCreateRequest.from_dict(userstories_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


