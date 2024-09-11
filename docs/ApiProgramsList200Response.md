# ApiProgramsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Program]**](Program.md) |  | 

## Example

```python
from pp_sdk.models.api_programs_list200_response import ApiProgramsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProgramsList200Response from a JSON string
api_programs_list200_response_instance = ApiProgramsList200Response.from_json(json)
# print the JSON string representation of the object
print(ApiProgramsList200Response.to_json())

# convert the object into a dict
api_programs_list200_response_dict = api_programs_list200_response_instance.to_dict()
# create an instance of ApiProgramsList200Response from a dict
api_programs_list200_response_from_dict = ApiProgramsList200Response.from_dict(api_programs_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


