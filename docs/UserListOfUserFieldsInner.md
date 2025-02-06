# UserListOfUserFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID | 
**email** | **str** | Optional, only used in response | [optional] 
**first_name** | **str** | Optional, only used in response | [optional] 
**last_name** | **str** | Optional, only used in response | [optional] 

## Example

```python
from pp_sdk.models.user_list_of_user_fields_inner import UserListOfUserFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserListOfUserFieldsInner from a JSON string
user_list_of_user_fields_inner_instance = UserListOfUserFieldsInner.from_json(json)
# print the JSON string representation of the object
print(UserListOfUserFieldsInner.to_json())

# convert the object into a dict
user_list_of_user_fields_inner_dict = user_list_of_user_fields_inner_instance.to_dict()
# create an instance of UserListOfUserFieldsInner from a dict
user_list_of_user_fields_inner_from_dict = UserListOfUserFieldsInner.from_dict(user_list_of_user_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


