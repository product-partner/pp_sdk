# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] 
**title** | **str** |  | 
**body** | **str** |  | [optional] 
**created_by** | [**CreatedBy**](CreatedBy.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 
**reviewed_date** | **datetime** |  | [optional] 
**document_covering_period_start** | **datetime** |  | [optional] 
**document_covering_period_end** | **datetime** |  | [optional] 
**publishing_state** | **str** |  | [optional] 
**programs** | [**List[ProgramsInner]**](ProgramsInner.md) |  | [optional] [readonly] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] [readonly] 
**stakeholder_users** | [**List[StakeholderUsersInner]**](StakeholderUsersInner.md) |  | [optional] [readonly] 
**version** | **int** |  | [optional] [readonly] 
**version_summary** | **str** |  | [optional] 

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


