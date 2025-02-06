# UserListInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | User ID | 
**email** | **str** | Optional, only used in response | [optional] 
**first_name** | **str** | Optional, only used in response | [optional] 
**last_name** | **str** | Optional, only used in response | [optional] 

## Example

```python
from pp_sdk.models.user_list_inner import UserListInner

# TODO update the JSON string below
json = "{}"
# create an instance of UserListInner from a JSON string
user_list_inner_instance = UserListInner.from_json(json)
# print the JSON string representation of the object
print(UserListInner.to_json())

# convert the object into a dict
user_list_inner_dict = user_list_inner_instance.to_dict()
# create an instance of UserListInner from a dict
user_list_inner_from_dict = UserListInner.from_dict(user_list_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


