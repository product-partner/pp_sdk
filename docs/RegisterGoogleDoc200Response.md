# RegisterGoogleDoc200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Success message | [optional] 
**document_id** | **str** | ID of the created or existing document | [optional] 
**title** | **str** | Document title | [optional] 
**already_registered** | **bool** | Whether the document was already registered | [optional] 

## Example

```python
from pp_sdk.models.register_google_doc200_response import RegisterGoogleDoc200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterGoogleDoc200Response from a JSON string
register_google_doc200_response_instance = RegisterGoogleDoc200Response.from_json(json)
# print the JSON string representation of the object
print(RegisterGoogleDoc200Response.to_json())

# convert the object into a dict
register_google_doc200_response_dict = register_google_doc200_response_instance.to_dict()
# create an instance of RegisterGoogleDoc200Response from a dict
register_google_doc200_response_from_dict = RegisterGoogleDoc200Response.from_dict(register_google_doc200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


