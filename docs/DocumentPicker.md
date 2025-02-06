# DocumentPicker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**title** | **str** |  | [optional] [readonly] 
**summary** | **str** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.document_picker import DocumentPicker

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentPicker from a JSON string
document_picker_instance = DocumentPicker.from_json(json)
# print the JSON string representation of the object
print(DocumentPicker.to_json())

# convert the object into a dict
document_picker_dict = document_picker_instance.to_dict()
# create an instance of DocumentPicker from a dict
document_picker_from_dict = DocumentPicker.from_dict(document_picker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


