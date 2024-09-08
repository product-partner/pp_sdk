# openapi_client.ProgramsApi

All URIs are relative to *http://0.0.0.0:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**programs_list**](ProgramsApi.md#programs_list) | **GET** /programs/ | 
[**programs_list_list**](ProgramsApi.md#programs_list_list) | **GET** /programs/list/ | 
[**programs_search_list**](ProgramsApi.md#programs_search_list) | **GET** /programs/search/ | 


# **programs_list**
> List[Program] programs_list(tags=tags, search=search, sort=sort, limit=limit, x_user_id=x_user_id)



Search for programs

### Example


```python
import openapi_client
from openapi_client.models.program import Program
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
    api_instance = openapi_client.ProgramsApi(api_client)
    tags = 'tags_example' # str | Comma-separated list of tags (optional)
    search = 'search_example' # str | Search term for name and description (optional)
    sort = 'sort_example' # str | Sort field (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.programs_list(tags=tags, search=search, sort=sort, limit=limit, x_user_id=x_user_id)
        print("The response of ProgramsApi->programs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgramsApi->programs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| Comma-separated list of tags | [optional] 
 **search** | **str**| Search term for name and description | [optional] 
 **sort** | **str**| Sort field | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Program]**](Program.md)

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

# **programs_list_list**
> List[Program] programs_list_list(tags=tags, search=search, sort=sort, limit=limit, x_user_id=x_user_id)



Search for programs

### Example


```python
import openapi_client
from openapi_client.models.program import Program
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
    api_instance = openapi_client.ProgramsApi(api_client)
    tags = 'tags_example' # str | Comma-separated list of tags (optional)
    search = 'search_example' # str | Search term for name and description (optional)
    sort = 'sort_example' # str | Sort field (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.programs_list_list(tags=tags, search=search, sort=sort, limit=limit, x_user_id=x_user_id)
        print("The response of ProgramsApi->programs_list_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgramsApi->programs_list_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| Comma-separated list of tags | [optional] 
 **search** | **str**| Search term for name and description | [optional] 
 **sort** | **str**| Sort field | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Program]**](Program.md)

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

# **programs_search_list**
> List[Program] programs_search_list(tags=tags, search=search, sort=sort, limit=limit, x_user_id=x_user_id)



Search for programs

### Example


```python
import openapi_client
from openapi_client.models.program import Program
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
    api_instance = openapi_client.ProgramsApi(api_client)
    tags = 'tags_example' # str | Comma-separated list of tags (optional)
    search = 'search_example' # str | Search term for name and description (optional)
    sort = 'sort_example' # str | Sort field (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.programs_search_list(tags=tags, search=search, sort=sort, limit=limit, x_user_id=x_user_id)
        print("The response of ProgramsApi->programs_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProgramsApi->programs_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| Comma-separated list of tags | [optional] 
 **search** | **str**| Search term for name and description | [optional] 
 **sort** | **str**| Sort field | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Program]**](Program.md)

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

