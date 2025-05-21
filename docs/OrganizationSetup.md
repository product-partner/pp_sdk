# OrganizationSetup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**organization** | **str** |  | [optional] [readonly] 
**project_system_setup_state** | **str** |  | [optional] 
**repo_setup_state** | **str** |  | [optional] 
**document_setup_state** | **str** |  | [optional] 
**retro_setup_state** | **str** |  | [optional] 
**users_setup_state** | **str** |  | [optional] 
**company_setup_state** | **str** |  | [optional] 
**setup_complete** | **bool** |  | [optional] 

## Example

```python
from pp_sdk.models.organization_setup import OrganizationSetup

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSetup from a JSON string
organization_setup_instance = OrganizationSetup.from_json(json)
# print the JSON string representation of the object
print(OrganizationSetup.to_json())

# convert the object into a dict
organization_setup_dict = organization_setup_instance.to_dict()
# create an instance of OrganizationSetup from a dict
organization_setup_from_dict = OrganizationSetup.from_dict(organization_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


