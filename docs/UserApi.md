# pp_sdk.UserApi

All URIs are relative to *http://0.0.0.0:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create**](UserApi.md#user_create) | **POST** /user/ | 
[**user_delete**](UserApi.md#user_delete) | **DELETE** /user/{id}/ | 
[**user_list**](UserApi.md#user_list) | **GET** /user/ | 
[**user_partial_update**](UserApi.md#user_partial_update) | **PATCH** /user/{id}/ | 
[**user_picker_list**](UserApi.md#user_picker_list) | **GET** /user/picker/ | 
[**user_read**](UserApi.md#user_read) | **GET** /user/{id}/ | 
[**user_update**](UserApi.md#user_update) | **PUT** /user/{id}/ | 


# **user_create**
> User user_create(data, x_user_id=x_user_id)



Create a new user for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.user import User
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
    api_instance = pp_sdk.UserApi(api_client)
    data = pp_sdk.User() # User | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.user_create(data, x_user_id=x_user_id)
        print("The response of UserApi->user_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**User**](User.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**User**](User.md)

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

# **user_delete**
> user_delete(id)



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
    api_instance = pp_sdk.UserApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.user_delete(id)
    except Exception as e:
        print("Exception when calling UserApi->user_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_list**
> List[User] user_list(page=page, search=search, domain=domain, limit=limit, sort=sort)



Retrieve one or more users

### Example


```python
import pp_sdk
from pp_sdk.models.user import User
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
    api_instance = pp_sdk.UserApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    search = 'search_example' # str | Search term for filtering users by email, last name, or first name (optional)
    domain = 'domain_example' # str | Search term for filtering users by the domain of the organzation (optional)
    limit = 56 # int | Maximum number of results to return (optional)
    sort = 'sort_example' # str | Field to sort the results by (optional)

    try:
        api_response = api_instance.user_list(page=page, search=search, domain=domain, limit=limit, sort=sort)
        print("The response of UserApi->user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **search** | **str**| Search term for filtering users by email, last name, or first name | [optional] 
 **domain** | **str**| Search term for filtering users by the domain of the organzation | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 
 **sort** | **str**| Field to sort the results by | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_partial_update**
> User user_partial_update(id, data)



### Example


```python
import pp_sdk
from pp_sdk.models.user import User
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
    api_instance = pp_sdk.UserApi(api_client)
    id = 'id_example' # str | 
    data = pp_sdk.User() # User | 

    try:
        api_response = api_instance.user_partial_update(id, data)
        print("The response of UserApi->user_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

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

# **user_picker_list**
> List[User] user_picker_list(search=search, sort=sort, limit=limit)



Retrieve list of users matching none or all of search parameters.

### Example


```python
import pp_sdk
from pp_sdk.models.user import User
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
    api_instance = pp_sdk.UserApi(api_client)
    search = 'search_example' # str | Search term for filtering users by email, last name, or first name (optional)
    sort = 'sort_example' # str | Field to sort the results by (optional)
    limit = 56 # int | Maximum number of results to return (optional)

    try:
        api_response = api_instance.user_picker_list(search=search, sort=sort, limit=limit)
        print("The response of UserApi->user_picker_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_picker_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term for filtering users by email, last name, or first name | [optional] 
 **sort** | **str**| Field to sort the results by | [optional] 
 **limit** | **int**| Maximum number of results to return | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_read**
> List[User] user_read(id, x_user_id=x_user_id)



Get a list of all PRDs for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.user import User
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
    api_instance = pp_sdk.UserApi(api_client)
    id = 'id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.user_read(id, x_user_id=x_user_id)
        print("The response of UserApi->user_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[User]**](User.md)

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

# **user_update**
> User user_update(id, data, x_user_id=x_user_id)



Update a specific user's details

### Example


```python
import pp_sdk
from pp_sdk.models.user import User
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
    api_instance = pp_sdk.UserApi(api_client)
    id = 'id_example' # str | UUID of the user to update
    data = pp_sdk.User() # User | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.user_update(id, data, x_user_id=x_user_id)
        print("The response of UserApi->user_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->user_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID of the user to update | 
 **data** | [**User**](User.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

