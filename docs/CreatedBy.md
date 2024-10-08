# CreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.created_by import CreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedBy from a JSON string
created_by_instance = CreatedBy.from_json(json)
# print the JSON string representation of the object
print(CreatedBy.to_json())

# convert the object into a dict
created_by_dict = created_by_instance.to_dict()
# create an instance of CreatedBy from a dict
created_by_from_dict = CreatedBy.from_dict(created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


