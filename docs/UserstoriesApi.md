# pp_sdk.UserstoriesApi

All URIs are relative to *http://0.0.0.0:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userstories_create**](UserstoriesApi.md#userstories_create) | **POST** /userstories/ | 
[**userstories_delete**](UserstoriesApi.md#userstories_delete) | **DELETE** /userstories/{userstory_id}/ | 
[**userstories_list**](UserstoriesApi.md#userstories_list) | **GET** /userstories/ | 
[**userstories_partial_update**](UserstoriesApi.md#userstories_partial_update) | **PATCH** /userstories/{userstory_id}/ | 
[**userstories_read**](UserstoriesApi.md#userstories_read) | **GET** /userstories/{userstory_id}/ | 
[**userstories_update**](UserstoriesApi.md#userstories_update) | **PUT** /userstories/{userstory_id}/ | 


# **userstories_create**
> UserStory userstories_create(data, x_user_id=x_user_id)



Create a new user story.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
from pp_sdk.models.userstories_create_request import UserstoriesCreateRequest
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
)


# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.UserstoriesApi(api_client)
    data = pp_sdk.UserstoriesCreateRequest() # UserstoriesCreateRequest | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.userstories_create(data, x_user_id=x_user_id)
        print("The response of UserstoriesApi->userstories_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserstoriesApi->userstories_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserstoriesCreateRequest**](UserstoriesCreateRequest.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**UserStory**](UserStory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userstories_delete**
> userstories_delete(userstory_id, x_user_id=x_user_id)



Delete a specific user story.

### Example


```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
)


# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.UserstoriesApi(api_client)
    userstory_id = 'userstory_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.userstories_delete(userstory_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling UserstoriesApi->userstories_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userstory_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userstories_list**
> List[UserStory] userstories_list(search=search, status=status, prd=prd, sort=sort, limit=limit, x_user_id=x_user_id, format=format)



List or Search for User Stories

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
)


# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.UserstoriesApi(api_client)
    search = 'search_example' # str | Search term for as_a, i_want_to, so_that, or freetext_override fields (optional)
    status = 'status_example' # str | Filter by status (optional)
    prd = 56 # int | Filter by PRD ID (optional)
    sort = 'sort_example' # str | Sort field (prefix with '-' for descending order) (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    format = 'format_example' # str | Response format (json or excel, default is json) (optional)

    try:
        api_response = api_instance.userstories_list(search=search, status=status, prd=prd, sort=sort, limit=limit, x_user_id=x_user_id, format=format)
        print("The response of UserstoriesApi->userstories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserstoriesApi->userstories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term for as_a, i_want_to, so_that, or freetext_override fields | [optional] 
 **status** | **str**| Filter by status | [optional] 
 **prd** | **int**| Filter by PRD ID | [optional] 
 **sort** | **str**| Sort field (prefix with &#39;-&#39; for descending order) | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **format** | **str**| Response format (json or excel, default is json) | [optional] 

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

# **userstories_partial_update**
> UserStory userstories_partial_update(userstory_id, data, x_user_id=x_user_id)



Partially update a specific user story.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
)


# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.UserstoriesApi(api_client)
    userstory_id = 'userstory_id_example' # str | 
    data = pp_sdk.UserStory() # UserStory | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.userstories_partial_update(userstory_id, data, x_user_id=x_user_id)
        print("The response of UserstoriesApi->userstories_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserstoriesApi->userstories_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userstory_id** | **str**|  | 
 **data** | [**UserStory**](UserStory.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**UserStory**](UserStory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **userstories_read**
> UserStory userstories_read(userstory_id, x_user_id=x_user_id)



Get details of a specific user story.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
)


# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.UserstoriesApi(api_client)
    userstory_id = 'userstory_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.userstories_read(userstory_id, x_user_id=x_user_id)
        print("The response of UserstoriesApi->userstories_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserstoriesApi->userstories_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userstory_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**UserStory**](UserStory.md)

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

# **userstories_update**
> UserStory userstories_update(userstory_id, data, x_user_id=x_user_id)



Update a specific user story.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
)


# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.UserstoriesApi(api_client)
    userstory_id = 'userstory_id_example' # str | 
    data = pp_sdk.UserStory() # UserStory | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.userstories_update(userstory_id, data, x_user_id=x_user_id)
        print("The response of UserstoriesApi->userstories_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserstoriesApi->userstories_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userstory_id** | **str**|  | 
 **data** | [**UserStory**](UserStory.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**UserStory**](UserStory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

