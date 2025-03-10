# RegisterGoogleDocRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_doc_id** | **str** | Google Doc ID to register | 

## Example

```python
from pp_sdk.models.register_google_doc_request import RegisterGoogleDocRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterGoogleDocRequest from a JSON string
register_google_doc_request_instance = RegisterGoogleDocRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterGoogleDocRequest.to_json())

# convert the object into a dict
register_google_doc_request_dict = register_google_doc_request_instance.to_dict()
# create an instance of RegisterGoogleDocRequest from a dict
register_google_doc_request_from_dict = RegisterGoogleDocRequest.from_dict(register_google_doc_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


