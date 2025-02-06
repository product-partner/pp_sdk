# ChatUploadFile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Upload status message | [optional] 
**filename** | **str** | Name of the uploaded file | [optional] 
**doc_id** | **str** | Document ID of the uploaded file | [optional] 

## Example

```python
from pp_sdk.models.chat_upload_file200_response import ChatUploadFile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChatUploadFile200Response from a JSON string
chat_upload_file200_response_instance = ChatUploadFile200Response.from_json(json)
# print the JSON string representation of the object
print(ChatUploadFile200Response.to_json())

# convert the object into a dict
chat_upload_file200_response_dict = chat_upload_file200_response_instance.to_dict()
# create an instance of ChatUploadFile200Response from a dict
chat_upload_file200_response_from_dict = ChatUploadFile200Response.from_dict(chat_upload_file200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


