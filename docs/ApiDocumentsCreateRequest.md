# ApiDocumentsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**body** | **str** |  | 
**type** | **str** |  | 
**publishing_state** | **str** |  | [optional] 
**document_covering_period_start** | **date** |  | [optional] 
**document_covering_period_end** | **date** |  | [optional] 
**tags** | **List[str]** | List of tags | [optional] 
**stakeholder_users** | **List[str]** | List of stakeholder user emails or UUIDs | [optional] 
**program** | **str** | Program UUID | [optional] 

## Example

```python
from pp_sdk.models.api_documents_create_request import ApiDocumentsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsCreateRequest from a JSON string
api_documents_create_request_instance = ApiDocumentsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsCreateRequest.to_json())

# convert the object into a dict
api_documents_create_request_dict = api_documents_create_request_instance.to_dict()
# create an instance of ApiDocumentsCreateRequest from a dict
api_documents_create_request_from_dict = ApiDocumentsCreateRequest.from_dict(api_documents_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


