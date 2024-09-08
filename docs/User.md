# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**email** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_staff** | **bool** |  | [optional] 
**date_joined** | **datetime** |  | [optional] 
**last_login** | **datetime** |  | [optional] 
**organization** | [**Organization**](Organization.md) |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**user_facts** | **object** |  | [optional] 
**walkthrough_status** | **object** |  | [optional] 

## Example

```python
from pp_sdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


