# ApiChatUploadFile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**doc_id** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.api_chat_upload_file200_response import ApiChatUploadFile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiChatUploadFile200Response from a JSON string
api_chat_upload_file200_response_instance = ApiChatUploadFile200Response.from_json(json)
# print the JSON string representation of the object
print(ApiChatUploadFile200Response.to_json())

# convert the object into a dict
api_chat_upload_file200_response_dict = api_chat_upload_file200_response_instance.to_dict()
# create an instance of ApiChatUploadFile200Response from a dict
api_chat_upload_file200_response_from_dict = ApiChatUploadFile200Response.from_dict(api_chat_upload_file200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


