# openapi_client.UserstoryApi

All URIs are relative to *http://0.0.0.0:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userstory_search_list**](UserstoryApi.md#userstory_search_list) | **GET** /userstory/search/ | 


# **userstory_search_list**
> List[UserStory] userstory_search_list(status=status, search=search, sort=sort, limit=limit, x_user_id=x_user_id)



Search and filter UserStory data

### Example


```python
import openapi_client
from openapi_client.models.user_story import UserStory
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://0.0.0.0:8000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserstoryApi(api_client)
    status = 'status_example' # str | Filter by status (optional)
    search = 'search_example' # str | Search string for as_a, i_want_to, so_that, or freetext_override fields (optional)
    sort = 'sort_example' # str | Sort field (created_at, updated_at, due_date, priority, status). Use '-' prefix for descending order (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.userstory_search_list(status=status, search=search, sort=sort, limit=limit, x_user_id=x_user_id)
        print("The response of UserstoryApi->userstory_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserstoryApi->userstory_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by status | [optional] 
 **search** | **str**| Search string for as_a, i_want_to, so_that, or freetext_override fields | [optional] 
 **sort** | **str**| Sort field (created_at, updated_at, due_date, priority, status). Use &#39;-&#39; prefix for descending order | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[UserStory]**](UserStory.md)

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

