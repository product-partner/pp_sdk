# UserField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.user_field import UserField

# TODO update the JSON string below
json = "{}"
# create an instance of UserField from a JSON string
user_field_instance = UserField.from_json(json)
# print the JSON string representation of the object
print(UserField.to_json())

# convert the object into a dict
user_field_dict = user_field_instance.to_dict()
# create an instance of UserField from a dict
user_field_from_dict = UserField.from_dict(user_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


