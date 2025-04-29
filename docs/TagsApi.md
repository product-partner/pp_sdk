# pp_sdk.TagsApi

All URIs are relative to *https://0.0.0.0:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_create**](TagsApi.md#tags_create) | **POST** /tags/ | 
[**tags_delete**](TagsApi.md#tags_delete) | **DELETE** /tags/{tag_id}/ | 
[**tags_list**](TagsApi.md#tags_list) | **GET** /tags/ | 
[**tags_partial_update**](TagsApi.md#tags_partial_update) | **PATCH** /tags/{tag_id}/ | 
[**tags_read**](TagsApi.md#tags_read) | **GET** /tags/{tag_id}/ | 
[**tags_update**](TagsApi.md#tags_update) | **PUT** /tags/{tag_id}/ | 


# **tags_create**
> Tag tags_create(data, x_user_id=x_user_id)

Create a new tag for the authenticated user.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.tag import Tag
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
    api_instance = pp_sdk.TagsApi(api_client)
    data = pp_sdk.Tag() # Tag | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.tags_create(data, x_user_id=x_user_id)
        print("The response of TagsApi->tags_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Tag**](Tag.md)

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

# **tags_delete**
> tags_delete(tag_id, x_user_id=x_user_id)

Delete a specific tag.

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
    api_instance = pp_sdk.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.tags_delete(tag_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling TagsApi->tags_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 
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

# **tags_list**
> List[Tag] tags_list(page=page, x_user_id=x_user_id, search=search)

Get a list of all tags for the authenticated user.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.tag import Tag
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
    api_instance = pp_sdk.TagsApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    search = 'search_example' # str | Search tags by name (optional)

    try:
        api_response = api_instance.tags_list(page=page, x_user_id=x_user_id, search=search)
        print("The response of TagsApi->tags_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **search** | **str**| Search tags by name | [optional] 

### Return type

[**List[Tag]**](Tag.md)

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

# **tags_partial_update**
> Tag tags_partial_update(tag_id, data, x_user_id=x_user_id)

Partially update a specific tag.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.tag import Tag
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
    api_instance = pp_sdk.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | 
    data = pp_sdk.Tag() # Tag | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.tags_partial_update(tag_id, data, x_user_id=x_user_id)
        print("The response of TagsApi->tags_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 
 **data** | [**Tag**](Tag.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Tag**](Tag.md)

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

# **tags_read**
> Tag tags_read(tag_id, x_user_id=x_user_id)

Get details of a specific tag.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.tag import Tag
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
    api_instance = pp_sdk.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.tags_read(tag_id, x_user_id=x_user_id)
        print("The response of TagsApi->tags_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Tag**](Tag.md)

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

# **tags_update**
> Tag tags_update(tag_id, data, x_user_id=x_user_id)

Update a specific tag.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.tag import Tag
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
    api_instance = pp_sdk.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | 
    data = pp_sdk.Tag() # Tag | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.tags_update(tag_id, data, x_user_id=x_user_id)
        print("The response of TagsApi->tags_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 
 **data** | [**Tag**](Tag.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Tag**](Tag.md)

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

