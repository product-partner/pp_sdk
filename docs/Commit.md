# Commit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**user** | [**UserField**](UserField.md) |  | [optional] 
**commit_hash** | **str** |  | 
**repo** | **str** |  | 
**user_lines_changed** | **int** |  | [optional] 
**ai_lines_changed** | **int** |  | [optional] 
**user_lines_list** | **object** |  | [optional] 
**ai_lines_list** | **object** |  | [optional] 
**created_date** | **datetime** |  | [optional] [readonly] 
**last_updated_date** | **datetime** |  | [optional] [readonly] 

## Example

```python
from pp_sdk.models.commit import Commit

# TODO update the JSON string below
json = "{}"
# create an instance of Commit from a JSON string
commit_instance = Commit.from_json(json)
# print the JSON string representation of the object
print(Commit.to_json())

# convert the object into a dict
commit_dict = commit_instance.to_dict()
# create an instance of Commit from a dict
commit_from_dict = Commit.from_dict(commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


