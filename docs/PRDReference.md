# PRDReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from pp_sdk.models.prd_reference import PRDReference

# TODO update the JSON string below
json = "{}"
# create an instance of PRDReference from a JSON string
prd_reference_instance = PRDReference.from_json(json)
# print the JSON string representation of the object
print(PRDReference.to_json())

# convert the object into a dict
prd_reference_dict = prd_reference_instance.to_dict()
# create an instance of PRDReference from a dict
prd_reference_from_dict = PRDReference.from_dict(prd_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


