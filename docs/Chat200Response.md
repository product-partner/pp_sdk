# Chat200Response

Response can be either chat content, a stream URL, a UI command, or a status message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Chat message content | [optional] 
**stream_url** | **str** | URL for streaming chat responses | [optional] 
**show_object_id** | **str** | ID of object to show | [optional] 
**show_object_type** | **str** | Type of object to show | [optional] 
**action_type** | **str** | Type of action to perform | [optional] 
**status_message** | **str** | Status message to show in the UI | [optional] 
**id** | **str** | Associated ID | [optional] 

## Example

```python
from pp_sdk.models.chat200_response import Chat200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Chat200Response from a JSON string
chat200_response_instance = Chat200Response.from_json(json)
# print the JSON string representation of the object
print(Chat200Response.to_json())

# convert the object into a dict
chat200_response_dict = chat200_response_instance.to_dict()
# create an instance of Chat200Response from a dict
chat200_response_from_dict = Chat200Response.from_dict(chat200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


