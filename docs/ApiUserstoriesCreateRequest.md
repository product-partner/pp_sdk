# ApiUserstoriesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prd** | **str** | PRD UUID | 
**as_a** | **str** |  | [optional] 
**i_want_to** | **str** |  | [optional] 
**so_that** | **str** |  | [optional] 
**freetext_override** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 
**priority** | **str** |  | [optional] 
**tags** | **List[str]** | List of tag UUIDs | [optional] 

## Example

```python
from pp_sdk.models.api_userstories_create_request import ApiUserstoriesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUserstoriesCreateRequest from a JSON string
api_userstories_create_request_instance = ApiUserstoriesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiUserstoriesCreateRequest.to_json())

# convert the object into a dict
api_userstories_create_request_dict = api_userstories_create_request_instance.to_dict()
# create an instance of ApiUserstoriesCreateRequest from a dict
api_userstories_create_request_from_dict = ApiUserstoriesCreateRequest.from_dict(api_userstories_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


