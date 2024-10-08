# PRDBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 

## Example

```python
from pp_sdk.models.prd_base import PRDBase

# TODO update the JSON string below
json = "{}"
# create an instance of PRDBase from a JSON string
prd_base_instance = PRDBase.from_json(json)
# print the JSON string representation of the object
print(PRDBase.to_json())

# convert the object into a dict
prd_base_dict = prd_base_instance.to_dict()
# create an instance of PRDBase from a dict
prd_base_from_dict = PRDBase.from_dict(prd_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


