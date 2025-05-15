# TargetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**model_name** | **str** |  | 
**model_version** | **str** |  | 
**created_by** | [**UserField**](UserField.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**modified_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.target_model import TargetModel

# TODO update the JSON string below
json = "{}"
# create an instance of TargetModel from a JSON string
target_model_instance = TargetModel.from_json(json)
# print the JSON string representation of the object
print(TargetModel.to_json())

# convert the object into a dict
target_model_dict = target_model_instance.to_dict()
# create an instance of TargetModel from a dict
target_model_from_dict = TargetModel.from_dict(target_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


