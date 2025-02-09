# pp_sdk.StatusApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_create**](StatusApi.md#status_create) | **POST** /status/ | 
[**status_delete**](StatusApi.md#status_delete) | **DELETE** /status/{status_id}/ | 
[**status_list**](StatusApi.md#status_list) | **GET** /status/ | 
[**status_partial_update**](StatusApi.md#status_partial_update) | **PATCH** /status/{status_id}/ | 
[**status_read**](StatusApi.md#status_read) | **GET** /status/{status_id}/ | 
[**status_update**](StatusApi.md#status_update) | **PUT** /status/{status_id}/ | 


# **status_create**
> Status status_create(data, x_user_id=x_user_id)



Create a new status for the authenticated user.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.status import Status
from pp_sdk.models.status_create_request import StatusCreateRequest
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://localhost:8000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UserIdAuth
configuration.api_key['UserIdAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserIdAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.StatusApi(api_client)
    data = pp_sdk.StatusCreateRequest() # StatusCreateRequest | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.status_create(data, x_user_id=x_user_id)
        print("The response of StatusApi->status_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**StatusCreateRequest**](StatusCreateRequest.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_delete**
> status_delete(status_id, x_user_id=x_user_id)



Delete a specific status.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://localhost:8000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UserIdAuth
configuration.api_key['UserIdAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserIdAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.StatusApi(api_client)
    status_id = 'status_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.status_delete(status_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling StatusApi->status_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_list**
> List[Status] status_list(page=page, x_user_id=x_user_id, status=status, search=search, sort=sort, liimit=liimit, goal_ids=goal_ids)



Get a list of all statuses for the authenticated user.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.status import Status
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://localhost:8000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UserIdAuth
configuration.api_key['UserIdAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserIdAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.StatusApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    status = 'status_example' # str | Filter by a status value (optional)
    search = 'search_example' # str | Search by keyword against status note or path to green (optional)
    sort = 'sort_example' # str | Sort by field (prefix with '-' for descending) (optional)
    liimit = 'liimit_example' # str | Sort by field (prefix with '-' for descending) (optional)
    goal_ids = 'goal_ids_example' # str | Filter on goals, using the UUID of the goal. (optional)

    try:
        api_response = api_instance.status_list(page=page, x_user_id=x_user_id, status=status, search=search, sort=sort, liimit=liimit, goal_ids=goal_ids)
        print("The response of StatusApi->status_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **status** | **str**| Filter by a status value | [optional] 
 **search** | **str**| Search by keyword against status note or path to green | [optional] 
 **sort** | **str**| Sort by field (prefix with &#39;-&#39; for descending) | [optional] 
 **liimit** | **str**| Sort by field (prefix with &#39;-&#39; for descending) | [optional] 
 **goal_ids** | **str**| Filter on goals, using the UUID of the goal. | [optional] 

### Return type

[**List[Status]**](Status.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_partial_update**
> Status status_partial_update(status_id, data, x_user_id=x_user_id)



Partially update a specific status.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.status import Status
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://localhost:8000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UserIdAuth
configuration.api_key['UserIdAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserIdAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.StatusApi(api_client)
    status_id = 'status_id_example' # str | 
    data = pp_sdk.Status() # Status | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.status_partial_update(status_id, data, x_user_id=x_user_id)
        print("The response of StatusApi->status_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**|  | 
 **data** | [**Status**](Status.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_read**
> Status status_read(status_id, x_user_id=x_user_id)



Get details of a specific status.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.status import Status
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://localhost:8000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UserIdAuth
configuration.api_key['UserIdAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserIdAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.StatusApi(api_client)
    status_id = 'status_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.status_read(status_id, x_user_id=x_user_id)
        print("The response of StatusApi->status_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_update**
> Status status_update(status_id, data, x_user_id=x_user_id)



Update a specific status.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.status import Status
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://localhost:8000/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UserIdAuth
configuration.api_key['UserIdAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserIdAuth'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.StatusApi(api_client)
    status_id = 'status_id_example' # str | 
    data = pp_sdk.Status() # Status | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.status_update(status_id, data, x_user_id=x_user_id)
        print("The response of StatusApi->status_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**|  | 
 **data** | [**Status**](Status.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

