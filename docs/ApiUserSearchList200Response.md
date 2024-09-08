# ApiUserSearchList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[User]**](User.md) |  | 

## Example

```python
from pp_sdk.models.api_user_search_list200_response import ApiUserSearchList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUserSearchList200Response from a JSON string
api_user_search_list200_response_instance = ApiUserSearchList200Response.from_json(json)
# print the JSON string representation of the object
print(ApiUserSearchList200Response.to_json())

# convert the object into a dict
api_user_search_list200_response_dict = api_user_search_list200_response_instance.to_dict()
# create an instance of ApiUserSearchList200Response from a dict
api_user_search_list200_response_from_dict = ApiUserSearchList200Response.from_dict(api_user_search_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


