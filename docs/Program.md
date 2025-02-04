# Program


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**mission** | **str** |  | [optional] 
**charter** | **str** |  | [optional] 
**principal_users** | [**List[StakeholderUsersInner]**](StakeholderUsersInner.md) |  | [optional] [readonly] 
**stakeholder_users** | [**List[StakeholderUsersInner]**](StakeholderUsersInner.md) |  | [optional] [readonly] 
**parent** | **str** |  | [optional] 
**tags** | [**List[TagsInner]**](TagsInner.md) |  | [optional] 
**created_by** | [**CreatedBy**](CreatedBy.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.program import Program

# TODO update the JSON string below
json = "{}"
# create an instance of Program from a JSON string
program_instance = Program.from_json(json)
# print the JSON string representation of the object
print(Program.to_json())

# convert the object into a dict
program_dict = program_instance.to_dict()
# create an instance of Program from a dict
program_from_dict = Program.from_dict(program_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


