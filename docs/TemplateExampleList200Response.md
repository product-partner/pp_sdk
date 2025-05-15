# TemplateExampleList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Example]**](Example.md) |  | 

## Example

```python
from pp_sdk.models.template_example_list200_response import TemplateExampleList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateExampleList200Response from a JSON string
template_example_list200_response_instance = TemplateExampleList200Response.from_json(json)
# print the JSON string representation of the object
print(TemplateExampleList200Response.to_json())

# convert the object into a dict
template_example_list200_response_dict = template_example_list200_response_instance.to_dict()
# create an instance of TemplateExampleList200Response from a dict
template_example_list200_response_from_dict = TemplateExampleList200Response.from_dict(template_example_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


