# ApiDocumentsImageList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Document]**](Document.md) |  | 

## Example

```python
from pp_sdk.models.api_documents_image_list200_response import ApiDocumentsImageList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsImageList200Response from a JSON string
api_documents_image_list200_response_instance = ApiDocumentsImageList200Response.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsImageList200Response.to_json())

# convert the object into a dict
api_documents_image_list200_response_dict = api_documents_image_list200_response_instance.to_dict()
# create an instance of ApiDocumentsImageList200Response from a dict
api_documents_image_list200_response_from_dict = ApiDocumentsImageList200Response.from_dict(api_documents_image_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


