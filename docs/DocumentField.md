# DocumentField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.document_field import DocumentField

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentField from a JSON string
document_field_instance = DocumentField.from_json(json)
# print the JSON string representation of the object
print(DocumentField.to_json())

# convert the object into a dict
document_field_dict = document_field_instance.to_dict()
# create an instance of DocumentField from a dict
document_field_from_dict = DocumentField.from_dict(document_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


