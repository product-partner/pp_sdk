# OwnerUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.owner_users_inner import OwnerUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerUsersInner from a JSON string
owner_users_inner_instance = OwnerUsersInner.from_json(json)
# print the JSON string representation of the object
print(OwnerUsersInner.to_json())

# convert the object into a dict
owner_users_inner_dict = owner_users_inner_instance.to_dict()
# create an instance of OwnerUsersInner from a dict
owner_users_inner_from_dict = OwnerUsersInner.from_dict(owner_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


