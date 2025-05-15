# Example


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**example_text** | **str** |  | 
**is_public** | **bool** |  | [optional] 
**organization** | **str** |  | [optional] [readonly] 
**created_by** | [**UserField**](UserField.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.example import Example

# TODO update the JSON string below
json = "{}"
# create an instance of Example from a JSON string
example_instance = Example.from_json(json)
# print the JSON string representation of the object
print(Example.to_json())

# convert the object into a dict
example_dict = example_instance.to_dict()
# create an instance of Example from a dict
example_from_dict = Example.from_dict(example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


