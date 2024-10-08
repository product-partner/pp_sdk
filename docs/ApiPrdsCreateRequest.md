# ApiPrdsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | 
**body** | **str** |  | 
**status** | **str** |  | [optional] 
**due_date** | **date** |  | [optional] 
**tags** | **List[str]** | List of tags | [optional] 
**stakeholder_users** | **List[str]** | List of stakeholder user emails or UUIDs | [optional] 
**programs** | **List[str]** | List of program UUIDs | [optional] 

## Example

```python
from pp_sdk.models.api_prds_create_request import ApiPrdsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPrdsCreateRequest from a JSON string
api_prds_create_request_instance = ApiPrdsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiPrdsCreateRequest.to_json())

# convert the object into a dict
api_prds_create_request_dict = api_prds_create_request_instance.to_dict()
# create an instance of ApiPrdsCreateRequest from a dict
api_prds_create_request_from_dict = ApiPrdsCreateRequest.from_dict(api_prds_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


