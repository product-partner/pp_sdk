# ProgramBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 

## Example

```python
from pp_sdk.models.program_base import ProgramBase

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramBase from a JSON string
program_base_instance = ProgramBase.from_json(json)
# print the JSON string representation of the object
print ProgramBase.to_json()

# convert the object into a dict
program_base_dict = program_base_instance.to_dict()
# create an instance of ProgramBase from a dict
program_base_from_dict = ProgramBase.from_dict(program_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


