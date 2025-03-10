# GoogleDocsWebhook200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the webhook processing | [optional] 

## Example

```python
from pp_sdk.models.google_docs_webhook200_response import GoogleDocsWebhook200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDocsWebhook200Response from a JSON string
google_docs_webhook200_response_instance = GoogleDocsWebhook200Response.from_json(json)
# print the JSON string representation of the object
print(GoogleDocsWebhook200Response.to_json())

# convert the object into a dict
google_docs_webhook200_response_dict = google_docs_webhook200_response_instance.to_dict()
# create an instance of GoogleDocsWebhook200Response from a dict
google_docs_webhook200_response_from_dict = GoogleDocsWebhook200Response.from_dict(google_docs_webhook200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


