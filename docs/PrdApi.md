# pp_sdk.PrdApi

All URIs are relative to *http://0.0.0.0:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prd_template_create**](PrdApi.md#prd_template_create) | **POST** /prd/template/ | 
[**prd_template_delete**](PrdApi.md#prd_template_delete) | **DELETE** /prd/template/{prdtemplate_id}/ | 
[**prd_template_list**](PrdApi.md#prd_template_list) | **GET** /prd/template/ | 
[**prd_template_partial_update**](PrdApi.md#prd_template_partial_update) | **PATCH** /prd/template/{prdtemplate_id}/ | 
[**prd_template_read**](PrdApi.md#prd_template_read) | **GET** /prd/template/{prdtemplate_id}/ | 
[**prd_template_update**](PrdApi.md#prd_template_update) | **PUT** /prd/template/{prdtemplate_id}/ | 


# **prd_template_create**
> PRDTemplate prd_template_create(data, x_user_id=x_user_id)



List or create PRD templates for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.prd_template import PRDTemplate
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
    data = pp_sdk.PRDTemplate() # PRDTemplate | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.prd_template_create(data, x_user_id=x_user_id)
        print("The response of PrdApi->prd_template_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrdApi->prd_template_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PRDTemplate**](PRDTemplate.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRDTemplate**](PRDTemplate.md)

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

# **prd_template_delete**
> prd_template_delete(prdtemplate_id, x_user_id=x_user_id)



Retrieve, update or delete a PRD template.

### Example


```python
import pp_sdk
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
    prdtemplate_id = 'prdtemplate_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.prd_template_delete(prdtemplate_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling PrdApi->prd_template_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prdtemplate_id** | **str**|  | 
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prd_template_list**
> List[PRDTemplate] prd_template_list(page=page, x_user_id=x_user_id, q=q)



List PRD templates for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.prd_template import PRDTemplate
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
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    q = 'q_example' # str | Search query (optional)

    try:
        api_response = api_instance.prd_template_list(page=page, x_user_id=x_user_id, q=q)
        print("The response of PrdApi->prd_template_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrdApi->prd_template_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **q** | **str**| Search query | [optional] 

### Return type

[**List[PRDTemplate]**](PRDTemplate.md)

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

# **prd_template_partial_update**
> PRDTemplate prd_template_partial_update(prdtemplate_id, data, x_user_id=x_user_id)



Retrieve, update or delete a PRD template.

### Example


```python
import pp_sdk
from pp_sdk.models.prd_template import PRDTemplate
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
    prdtemplate_id = 'prdtemplate_id_example' # str | 
    data = pp_sdk.PRDTemplate() # PRDTemplate | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.prd_template_partial_update(prdtemplate_id, data, x_user_id=x_user_id)
        print("The response of PrdApi->prd_template_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrdApi->prd_template_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prdtemplate_id** | **str**|  | 
 **data** | [**PRDTemplate**](PRDTemplate.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRDTemplate**](PRDTemplate.md)

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

# **prd_template_read**
> PRDTemplate prd_template_read(prdtemplate_id, x_user_id=x_user_id)



Get a PRD template.

### Example


```python
import pp_sdk
from pp_sdk.models.prd_template import PRDTemplate
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
    prdtemplate_id = 'prdtemplate_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.prd_template_read(prdtemplate_id, x_user_id=x_user_id)
        print("The response of PrdApi->prd_template_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrdApi->prd_template_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prdtemplate_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRDTemplate**](PRDTemplate.md)

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

# **prd_template_update**
> PRDTemplate prd_template_update(prdtemplate_id, data, x_user_id=x_user_id)



Retrieve, update or delete a PRD template.

### Example


```python
import pp_sdk
from pp_sdk.models.prd_template import PRDTemplate
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
    prdtemplate_id = 'prdtemplate_id_example' # str | 
    data = pp_sdk.PRDTemplate() # PRDTemplate | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.prd_template_update(prdtemplate_id, data, x_user_id=x_user_id)
        print("The response of PrdApi->prd_template_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrdApi->prd_template_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prdtemplate_id** | **str**|  | 
 **data** | [**PRDTemplate**](PRDTemplate.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRDTemplate**](PRDTemplate.md)

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

