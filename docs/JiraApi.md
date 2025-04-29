# pp_sdk.JiraApi

All URIs are relative to *https://0.0.0.0:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jira_oauth_callback**](JiraApi.md#jira_oauth_callback) | **GET** /jira/oauth/callback | 
[**jira_oauth_start**](JiraApi.md#jira_oauth_start) | **GET** /jira/oauth/start | 
[**jira_oauth_toggle_sync**](JiraApi.md#jira_oauth_toggle_sync) | **POST** /jira/oauth/toggle-sync | 
[**jira_sync_documents_create**](JiraApi.md#jira_sync_documents_create) | **POST** /jira/sync/documents/{object_id}/ | 
[**jira_sync_documents_read**](JiraApi.md#jira_sync_documents_read) | **GET** /jira/sync/documents/{object_id}/ | 
[**jira_sync_programs_create**](JiraApi.md#jira_sync_programs_create) | **POST** /jira/sync/programs/{object_id}/ | 
[**jira_sync_programs_read**](JiraApi.md#jira_sync_programs_read) | **GET** /jira/sync/programs/{object_id}/ | 
[**jira_sync_status_list**](JiraApi.md#jira_sync_status_list) | **GET** /jira/sync/status/ | 
[**jira_sync_userstories_create**](JiraApi.md#jira_sync_userstories_create) | **POST** /jira/sync/userstories/{object_id}/ | 
[**jira_sync_userstories_read**](JiraApi.md#jira_sync_userstories_read) | **GET** /jira/sync/userstories/{object_id}/ | 
[**publish_doc_as_epic**](JiraApi.md#publish_doc_as_epic) | **POST** /jira/documents/{doc_id}/publish | 


# **jira_oauth_callback**
> jira_oauth_callback(code=code, state=state, error=error)

Handle the OAuth callback from Atlassian

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    code = 'code_example' # str | Authorization code from Atlassian (optional)
    state = 'state_example' # str | State token for verification (optional)
    error = 'error_example' # str | Error message if OAuth failed (optional)

    try:
        api_instance.jira_oauth_callback(code=code, state=state, error=error)
    except Exception as e:
        print("Exception when calling JiraApi->jira_oauth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Authorization code from Atlassian | [optional] 
 **state** | **str**| State token for verification | [optional] 
 **error** | **str**| Error message if OAuth failed | [optional] 

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
**200** |  |  -  |
**302** | Redirect to previous page or home |  -  |
**400** | Missing parameters, invalid state, or token exchange failed |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_oauth_start**
> jira_oauth_start()

Start the Jira OAuth flow by redirecting to Atlassian

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)

    try:
        api_instance.jira_oauth_start()
    except Exception as e:
        print("Exception when calling JiraApi->jira_oauth_start: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** |  |  -  |
**302** | Redirect to Atlassian OAuth consent screen |  -  |
**400** | Jira Client ID or Redirect URI not configured |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_oauth_toggle_sync**
> jira_oauth_toggle_sync(x_user_id=x_user_id)

Toggle Jira sync enabled status for the organization

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.jira_oauth_toggle_sync(x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->jira_oauth_toggle_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** |  |  -  |
**302** | Redirect to previous page or home |  -  |
**404** | Jira OAuth not configured for this organization |  -  |
**500** | Error toggling Jira sync |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_sync_documents_create**
> jira_sync_documents_create(object_id, data, x_user_id=x_user_id)

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.jira_sync_documents_create_request import JiraSyncDocumentsCreateRequest
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    object_id = 'object_id_example' # str | 
    data = pp_sdk.JiraSyncDocumentsCreateRequest() # JiraSyncDocumentsCreateRequest | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.jira_sync_documents_create(object_id, data, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->jira_sync_documents_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 
 **data** | [**JiraSyncDocumentsCreateRequest**](JiraSyncDocumentsCreateRequest.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_sync_documents_read**
> jira_sync_documents_read(object_id, x_user_id=x_user_id)

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    object_id = 'object_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.jira_sync_documents_read(object_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->jira_sync_documents_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_sync_programs_create**
> jira_sync_programs_create(object_id, data, x_user_id=x_user_id)

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.jira_sync_documents_create_request import JiraSyncDocumentsCreateRequest
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    object_id = 'object_id_example' # str | 
    data = pp_sdk.JiraSyncDocumentsCreateRequest() # JiraSyncDocumentsCreateRequest | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.jira_sync_programs_create(object_id, data, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->jira_sync_programs_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 
 **data** | [**JiraSyncDocumentsCreateRequest**](JiraSyncDocumentsCreateRequest.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_sync_programs_read**
> jira_sync_programs_read(object_id, x_user_id=x_user_id)

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    object_id = 'object_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.jira_sync_programs_read(object_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->jira_sync_programs_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_sync_status_list**
> jira_sync_status_list(x_user_id=x_user_id)

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.jira_sync_status_list(x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->jira_sync_status_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_sync_userstories_create**
> jira_sync_userstories_create(object_id, data, x_user_id=x_user_id)

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.jira_sync_documents_create_request import JiraSyncDocumentsCreateRequest
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    object_id = 'object_id_example' # str | 
    data = pp_sdk.JiraSyncDocumentsCreateRequest() # JiraSyncDocumentsCreateRequest | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.jira_sync_userstories_create(object_id, data, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->jira_sync_userstories_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 
 **data** | [**JiraSyncDocumentsCreateRequest**](JiraSyncDocumentsCreateRequest.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jira_sync_userstories_read**
> jira_sync_userstories_read(object_id, x_user_id=x_user_id)

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    object_id = 'object_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.jira_sync_userstories_read(object_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->jira_sync_userstories_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_doc_as_epic**
> publish_doc_as_epic(doc_id, data, x_user_id=x_user_id)

Publish or update a document as a Jira epic

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.publish_doc_as_epic_request import PublishDocAsEpicRequest
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "https://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.JiraApi(api_client)
    doc_id = 'doc_id_example' # str | 
    data = pp_sdk.PublishDocAsEpicRequest() # PublishDocAsEpicRequest | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.publish_doc_as_epic(doc_id, data, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling JiraApi->publish_doc_as_epic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  | 
 **data** | [**PublishDocAsEpicRequest**](PublishDocAsEpicRequest.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

void (empty response body)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document successfully published/updated as Jira epic |  -  |
**400** | Bad request - Document not found, wrong type, or missing program |  -  |
**401** | Unauthorized - Jira OAuth not configured |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

