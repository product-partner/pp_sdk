# ChatThreadDelete500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Operation success status | [optional] 
**error** | **str** | Error message | [optional] 

## Example

```python
from pp_sdk.models.chat_thread_delete500_response import ChatThreadDelete500Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChatThreadDelete500Response from a JSON string
chat_thread_delete500_response_instance = ChatThreadDelete500Response.from_json(json)
# print the JSON string representation of the object
print(ChatThreadDelete500Response.to_json())

# convert the object into a dict
chat_thread_delete500_response_dict = chat_thread_delete500_response_instance.to_dict()
# create an instance of ChatThreadDelete500Response from a dict
chat_thread_delete500_response_from_dict = ChatThreadDelete500Response.from_dict(chat_thread_delete500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


