# StakeholderUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.stakeholder_users_inner import StakeholderUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of StakeholderUsersInner from a JSON string
stakeholder_users_inner_instance = StakeholderUsersInner.from_json(json)
# print the JSON string representation of the object
print(StakeholderUsersInner.to_json())

# convert the object into a dict
stakeholder_users_inner_dict = stakeholder_users_inner_instance.to_dict()
# create an instance of StakeholderUsersInner from a dict
stakeholder_users_inner_from_dict = StakeholderUsersInner.from_dict(stakeholder_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


