# PRDField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.prd_field import PRDField

# TODO update the JSON string below
json = "{}"
# create an instance of PRDField from a JSON string
prd_field_instance = PRDField.from_json(json)
# print the JSON string representation of the object
print(PRDField.to_json())

# convert the object into a dict
prd_field_dict = prd_field_instance.to_dict()
# create an instance of PRDField from a dict
prd_field_from_dict = PRDField.from_dict(prd_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


