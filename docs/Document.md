# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] 
**title** | **str** |  | 
**body** | **str** |  | [optional] 
**created_by** | [**UserField**](UserField.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**reviewed_date** | **datetime** |  | [optional] 
**document_covering_period_start** | **datetime** |  | [optional] 
**document_covering_period_end** | **datetime** |  | [optional] 
**publishing_state** | **str** |  | [optional] 
**programs** | [**List[ProgramsListInner]**](ProgramsListInner.md) | Can accept either a list of program IDs (strings) or a list of objects with id field | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**stakeholder_users** | [**List[UserListOfUserFieldsInner]**](UserListOfUserFieldsInner.md) | Can accept either a list of user IDs (strings) or a list of objects with id field | [optional] 
**version** | **int** |  | [optional] [readonly] 
**version_summary** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] [readonly] 
**original_filename** | **str** |  | [optional] 
**blob_id** | **str** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


