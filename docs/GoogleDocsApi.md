# pp_sdk.GoogleDocsApi

All URIs are relative to *http://0.0.0.0:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**google_docs_list**](GoogleDocsApi.md#google_docs_list) | **GET** /google/docs/ | 
[**google_docs_read**](GoogleDocsApi.md#google_docs_read) | **GET** /google/docs/{doc_id}/ | 
[**google_docs_webhook**](GoogleDocsApi.md#google_docs_webhook) | **POST** /google/docs/webhook/{user_id}/ | 
[**register_google_doc**](GoogleDocsApi.md#register_google_doc) | **POST** /google/docs/register/ | 
[**watch_google_doc**](GoogleDocsApi.md#watch_google_doc) | **POST** /google/docs/{doc_id}/watch/ | 


# **google_docs_list**
> google_docs_list(max_results=max_results)

List Google Docs for the authenticated user's organization

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.GoogleDocsApi(api_client)
    max_results = 10 # int | Maximum number of results to return (optional) (default to 10)

    try:
        api_instance.google_docs_list(max_results=max_results)
    except Exception as e:
        print("Exception when calling GoogleDocsApi->google_docs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_results** | **int**| Maximum number of results to return | [optional] [default to 10]

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
**200** | List of Google Docs |  -  |
**400** | Invalid parameters |  -  |
**401** | Authentication required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_docs_read**
> google_docs_read(doc_id)

Get the content of a specific Google Doc

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.GoogleDocsApi(api_client)
    doc_id = 'doc_id_example' # str | 

    try:
        api_instance.google_docs_read(doc_id)
    except Exception as e:
        print("Exception when calling GoogleDocsApi->google_docs_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  | 

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
**200** | Google Doc content |  -  |
**404** | Document not found or access denied |  -  |
**401** | Authentication required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_docs_webhook**
> GoogleDocsWebhook200Response google_docs_webhook(user_id, x_goog_resource_id, x_goog_channel_id, x_goog_resource_state, x_goog_changed=x_goog_changed)

Webhook endpoint for Google Docs notifications

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.google_docs_webhook200_response import GoogleDocsWebhook200Response
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.GoogleDocsApi(api_client)
    user_id = 'user_id_example' # str | 
    x_goog_resource_id = 'x_goog_resource_id_example' # str | Google resource ID
    x_goog_channel_id = 'x_goog_channel_id_example' # str | Google channel ID
    x_goog_resource_state = 'x_goog_resource_state_example' # str | Resource state (sync, change, update)
    x_goog_changed = 'x_goog_changed_example' # str | Changed fields (optional)

    try:
        api_response = api_instance.google_docs_webhook(user_id, x_goog_resource_id, x_goog_channel_id, x_goog_resource_state, x_goog_changed=x_goog_changed)
        print("The response of GoogleDocsApi->google_docs_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleDocsApi->google_docs_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **x_goog_resource_id** | **str**| Google resource ID | 
 **x_goog_channel_id** | **str**| Google channel ID | 
 **x_goog_resource_state** | **str**| Resource state (sync, change, update) | 
 **x_goog_changed** | **str**| Changed fields | [optional] 

### Return type

[**GoogleDocsWebhook200Response**](GoogleDocsWebhook200Response.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Notification processed successfully |  -  |
**404** | Not found - Organization or document not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_google_doc**
> RegisterGoogleDoc200Response register_google_doc(data, x_user_id=x_user_id)

Register a Google Doc with the system

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.register_google_doc200_response import RegisterGoogleDoc200Response
from pp_sdk.models.register_google_doc_request import RegisterGoogleDocRequest
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.GoogleDocsApi(api_client)
    data = pp_sdk.RegisterGoogleDocRequest() # RegisterGoogleDocRequest | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.register_google_doc(data, x_user_id=x_user_id)
        print("The response of GoogleDocsApi->register_google_doc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleDocsApi->register_google_doc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RegisterGoogleDocRequest**](RegisterGoogleDocRequest.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**RegisterGoogleDoc200Response**](RegisterGoogleDoc200Response.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Google Doc registered successfully |  -  |
**400** | Bad request - Missing parameters or user not associated with an organization |  -  |
**404** | Not found - Google Doc not found or access denied |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_google_doc**
> WatchGoogleDoc200Response watch_google_doc(doc_id, x_user_id=x_user_id)

Set up a watch on a Google Doc to receive notifications about changes

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.watch_google_doc200_response import WatchGoogleDoc200Response
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000/api"
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
    api_instance = pp_sdk.GoogleDocsApi(api_client)
    doc_id = 'doc_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.watch_google_doc(doc_id, x_user_id=x_user_id)
        print("The response of GoogleDocsApi->watch_google_doc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleDocsApi->watch_google_doc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**WatchGoogleDoc200Response**](WatchGoogleDoc200Response.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watch set up successfully |  -  |
**400** | Bad request - User not found or not associated with an organization |  -  |
**401** | Unauthorized - Google OAuth not configured |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

