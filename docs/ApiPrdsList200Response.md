# ApiPrdsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[PRD]**](PRD.md) |  | 

## Example

```python
from pp_sdk.models.api_prds_list200_response import ApiPrdsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPrdsList200Response from a JSON string
api_prds_list200_response_instance = ApiPrdsList200Response.from_json(json)
# print the JSON string representation of the object
print(ApiPrdsList200Response.to_json())

# convert the object into a dict
api_prds_list200_response_dict = api_prds_list200_response_instance.to_dict()
# create an instance of ApiPrdsList200Response from a dict
api_prds_list200_response_from_dict = ApiPrdsList200Response.from_dict(api_prds_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


