# pp_sdk.DocumentsApi

All URIs are relative to *http://0.0.0.0:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_create**](DocumentsApi.md#documents_create) | **POST** /documents/ | 
[**documents_delete**](DocumentsApi.md#documents_delete) | **DELETE** /documents/{id}/ | 
[**documents_image_list**](DocumentsApi.md#documents_image_list) | **GET** /documents/{id}/image/ | 
[**documents_list**](DocumentsApi.md#documents_list) | **GET** /documents/ | 
[**documents_partial_update**](DocumentsApi.md#documents_partial_update) | **PATCH** /documents/{id}/ | 
[**documents_picker_list**](DocumentsApi.md#documents_picker_list) | **GET** /documents/picker/ | 
[**documents_read**](DocumentsApi.md#documents_read) | **GET** /documents/{id}/ | 
[**documents_update**](DocumentsApi.md#documents_update) | **PUT** /documents/{id}/ | 


# **documents_create**
> Document documents_create(data, x_user_id=x_user_id)



Create a new Document for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.document import Document
from pp_sdk.models.documents_create_request import DocumentsCreateRequest
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
    api_instance = pp_sdk.DocumentsApi(api_client)
    data = pp_sdk.DocumentsCreateRequest() # DocumentsCreateRequest | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.documents_create(data, x_user_id=x_user_id)
        print("The response of DocumentsApi->documents_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DocumentsCreateRequest**](DocumentsCreateRequest.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Document**](Document.md)

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

# **documents_delete**
> documents_delete(id, x_user_id=x_user_id)



Delete a specific document.

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
    api_instance = pp_sdk.DocumentsApi(api_client)
    id = 'id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.documents_delete(id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **documents_image_list**
> documents_image_list(id, page=page, x_user_id=x_user_id)



Retrieve document image

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
    api_instance = pp_sdk.DocumentsApi(api_client)
    id = 'id_example' # str | 
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.documents_image_list(id, page=page, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_image_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
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
**200** | Returns the image file with appropriate content-type |  -  |
**400** | Error when document is not an image or has invalid data |  -  |
**404** | Image not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_list**
> List[Document] documents_list(x_user_id=x_user_id, stakeholders=stakeholders, publishing_state=publishing_state, search=search, sort=sort, limit=limit, tags=tags, created_by=created_by, type=type)



Get a list of all Documents for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.document import Document
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
    api_instance = pp_sdk.DocumentsApi(api_client)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    stakeholders = 'stakeholders_example' # str | Comma-separated list of stakeholder user IDs to filter by (optional)
    publishing_state = 'publishing_state_example' # str | Publishing state to filter by (optional)
    search = 'search_example' # str | Search term to filter Documents by title or body (optional)
    sort = 'sort_example' # str | Field to sort by (e.g., 'title', '-created_date') (optional)
    limit = 56 # int | Limit the number of Documents returned (optional)
    tags = 'tags_example' # str | Comma-separated list of tag names to filter Documents by (optional)
    created_by = 'created_by_example' # str | Optional UUID of the user who created the Document to filter Documents by (optional)
    type = 'type_example' # str | Type of document to filter by (optional)

    try:
        api_response = api_instance.documents_list(x_user_id=x_user_id, stakeholders=stakeholders, publishing_state=publishing_state, search=search, sort=sort, limit=limit, tags=tags, created_by=created_by, type=type)
        print("The response of DocumentsApi->documents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **stakeholders** | **str**| Comma-separated list of stakeholder user IDs to filter by | [optional] 
 **publishing_state** | **str**| Publishing state to filter by | [optional] 
 **search** | **str**| Search term to filter Documents by title or body | [optional] 
 **sort** | **str**| Field to sort by (e.g., &#39;title&#39;, &#39;-created_date&#39;) | [optional] 
 **limit** | **int**| Limit the number of Documents returned | [optional] 
 **tags** | **str**| Comma-separated list of tag names to filter Documents by | [optional] 
 **created_by** | **str**| Optional UUID of the user who created the Document to filter Documents by | [optional] 
 **type** | **str**| Type of document to filter by | [optional] 

### Return type

[**List[Document]**](Document.md)

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

# **documents_partial_update**
> Document documents_partial_update(id, data, x_user_id=x_user_id)



Partially update a specific document.

### Example


```python
import pp_sdk
from pp_sdk.models.document import Document
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
    api_instance = pp_sdk.DocumentsApi(api_client)
    id = 'id_example' # str | 
    data = pp_sdk.Document() # Document | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.documents_partial_update(id, data, x_user_id=x_user_id)
        print("The response of DocumentsApi->documents_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Document**](Document.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Document**](Document.md)

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

# **documents_picker_list**
> List[DocumentPicker] documents_picker_list()



### Example


```python
import pp_sdk
from pp_sdk.models.document_picker import DocumentPicker
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
    api_instance = pp_sdk.DocumentsApi(api_client)

    try:
        api_response = api_instance.documents_picker_list()
        print("The response of DocumentsApi->documents_picker_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_picker_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DocumentPicker]**](DocumentPicker.md)

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

# **documents_read**
> Document documents_read(id, x_user_id=x_user_id, output_format=output_format)



Get details of a specific document.

### Example


```python
import pp_sdk
from pp_sdk.models.document import Document
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
    api_instance = pp_sdk.DocumentsApi(api_client)
    id = 'id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    output_format = 'output_format_example' # str | Response format (json, text, html, docx, pdf) (optional)

    try:
        api_response = api_instance.documents_read(id, x_user_id=x_user_id, output_format=output_format)
        print("The response of DocumentsApi->documents_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **output_format** | **str**| Response format (json, text, html, docx, pdf) | [optional] 

### Return type

[**Document**](Document.md)

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

# **documents_update**
> Document documents_update(id, data, x_user_id=x_user_id)



Update a specific document.

### Example


```python
import pp_sdk
from pp_sdk.models.document import Document
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
    api_instance = pp_sdk.DocumentsApi(api_client)
    id = 'id_example' # str | 
    data = pp_sdk.Document() # Document | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.documents_update(id, data, x_user_id=x_user_id)
        print("The response of DocumentsApi->documents_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**Document**](Document.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Document**](Document.md)

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

