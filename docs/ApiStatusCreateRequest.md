# ApiStatusCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | **str** |  | 
**status** | **str** |  | 
**var_date** | **datetime** |  | [optional] 
**status_note** | **str** |  | [optional] 
**path_to_green** | **str** |  | [optional] 
**publishing_state** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.api_status_create_request import ApiStatusCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiStatusCreateRequest from a JSON string
api_status_create_request_instance = ApiStatusCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiStatusCreateRequest.to_json())

# convert the object into a dict
api_status_create_request_dict = api_status_create_request_instance.to_dict()
# create an instance of ApiStatusCreateRequest from a dict
api_status_create_request_from_dict = ApiStatusCreateRequest.from_dict(api_status_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


