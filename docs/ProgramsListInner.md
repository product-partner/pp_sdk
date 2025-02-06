# ProgramsListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Program ID | 
**name** | **str** | Optional, only used in response | [optional] 

## Example

```python
from pp_sdk.models.programs_list_inner import ProgramsListInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramsListInner from a JSON string
programs_list_inner_instance = ProgramsListInner.from_json(json)
# print the JSON string representation of the object
print(ProgramsListInner.to_json())

# convert the object into a dict
programs_list_inner_dict = programs_list_inner_instance.to_dict()
# create an instance of ProgramsListInner from a dict
programs_list_inner_from_dict = ProgramsListInner.from_dict(programs_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


