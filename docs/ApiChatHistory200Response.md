# ApiChatHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_history** | **List[object]** | List of chat history items | [optional] 
**has_next** | **bool** |  | [optional] 
**has_previous** | **bool** |  | [optional] 
**first_date** | **str** |  | [optional] 
**last_date** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**start_index** | **int** |  | [optional] 
**page** | **int** |  | [optional] 
**items_per_page** | **int** |  | [optional] 

## Example

```python
from pp_sdk.models.api_chat_history200_response import ApiChatHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiChatHistory200Response from a JSON string
api_chat_history200_response_instance = ApiChatHistory200Response.from_json(json)
# print the JSON string representation of the object
print(ApiChatHistory200Response.to_json())

# convert the object into a dict
api_chat_history200_response_dict = api_chat_history200_response_instance.to_dict()
# create an instance of ApiChatHistory200Response from a dict
api_chat_history200_response_from_dict = ApiChatHistory200Response.from_dict(api_chat_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


