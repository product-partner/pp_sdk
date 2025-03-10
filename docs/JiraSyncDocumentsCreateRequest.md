# JiraSyncDocumentsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_enabled** | **bool** | Whether to enable or disable Jira sync | 

## Example

```python
from pp_sdk.models.jira_sync_documents_create_request import JiraSyncDocumentsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JiraSyncDocumentsCreateRequest from a JSON string
jira_sync_documents_create_request_instance = JiraSyncDocumentsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(JiraSyncDocumentsCreateRequest.to_json())

# convert the object into a dict
jira_sync_documents_create_request_dict = jira_sync_documents_create_request_instance.to_dict()
# create an instance of JiraSyncDocumentsCreateRequest from a dict
jira_sync_documents_create_request_from_dict = JiraSyncDocumentsCreateRequest.from_dict(jira_sync_documents_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


