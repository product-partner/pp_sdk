# ChatNewList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Operation success status | [optional] 
**chat_thread_id** | **str** | UUID of the newly created chat thread | [optional] 

## Example

```python
from pp_sdk.models.chat_new_list200_response import ChatNewList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChatNewList200Response from a JSON string
chat_new_list200_response_instance = ChatNewList200Response.from_json(json)
# print the JSON string representation of the object
print(ChatNewList200Response.to_json())

# convert the object into a dict
chat_new_list200_response_dict = chat_new_list200_response_instance.to_dict()
# create an instance of ChatNewList200Response from a dict
chat_new_list200_response_from_dict = ChatNewList200Response.from_dict(chat_new_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


