# ProgramPicker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.program_picker import ProgramPicker

# TODO update the JSON string below
json = "{}"
# create an instance of ProgramPicker from a JSON string
program_picker_instance = ProgramPicker.from_json(json)
# print the JSON string representation of the object
print(ProgramPicker.to_json())

# convert the object into a dict
program_picker_dict = program_picker_instance.to_dict()
# create an instance of ProgramPicker from a dict
program_picker_from_dict = ProgramPicker.from_dict(program_picker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


