# DocumentListFieldInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document ID | 
**title** | **str** | Optional, only used in response | [optional] 
**type** | **str** | Optional, only used in response | [optional] 

## Example

```python
from pp_sdk.models.document_list_field_inner import DocumentListFieldInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentListFieldInner from a JSON string
document_list_field_inner_instance = DocumentListFieldInner.from_json(json)
# print the JSON string representation of the object
print(DocumentListFieldInner.to_json())

# convert the object into a dict
document_list_field_inner_dict = document_list_field_inner_instance.to_dict()
# create an instance of DocumentListFieldInner from a dict
document_list_field_inner_from_dict = DocumentListFieldInner.from_dict(document_list_field_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


