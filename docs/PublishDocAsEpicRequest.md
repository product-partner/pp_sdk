# PublishDocAsEpicRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**program_id** | **str** | Program ID to use for publishing (required if document is associated with multiple programs) | [optional] 

## Example

```python
from pp_sdk.models.publish_doc_as_epic_request import PublishDocAsEpicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishDocAsEpicRequest from a JSON string
publish_doc_as_epic_request_instance = PublishDocAsEpicRequest.from_json(json)
# print the JSON string representation of the object
print(PublishDocAsEpicRequest.to_json())

# convert the object into a dict
publish_doc_as_epic_request_dict = publish_doc_as_epic_request_instance.to_dict()
# create an instance of PublishDocAsEpicRequest from a dict
publish_doc_as_epic_request_from_dict = PublishDocAsEpicRequest.from_dict(publish_doc_as_epic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


