# pp_sdk.PrdApi

All URIs are relative to *http://0.0.0.0:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prd_list_list**](PrdApi.md#prd_list_list) | **GET** /prd/list/ | 


# **prd_list_list**
> List[PRD] prd_list_list(q=q, x_user_id=x_user_id)



Search for PRDs

### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.prd import PRD
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000"
)


# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.PrdApi(api_client)
    q = 'q_example' # str | query string, to search across name or description (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.prd_list_list(q=q, x_user_id=x_user_id)
        print("The response of PrdApi->prd_list_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrdApi->prd_list_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| query string, to search across name or description | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[PRD]**](PRD.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

