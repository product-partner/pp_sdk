# pp_sdk.ChatApi

All URIs are relative to *http://0.0.0.0:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat**](ChatApi.md#chat) | **GET** /chat/ | 
[**chat_history**](ChatApi.md#chat_history) | **GET** /chat/history/ | 
[**chat_read**](ChatApi.md#chat_read) | **GET** /chat/{thread_id}/ | 
[**chat_upload_file**](ChatApi.md#chat_upload_file) | **POST** /chat/upload/ | 


# **chat**
> object chat(page=page, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id, msg=msg, doc_ids=doc_ids, action=action, stream=stream, response_format=response_format)



Process chat message

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
    api_instance = pp_sdk.ChatApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    x_caller_id = 'x_caller_id_example' # str | Optional ID of the application calling the ID, used in conjunction with the caller_thread_id (optional)
    x_caller_thread_id = 'x_caller_thread_id_example' # str | Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. (optional)
    msg = 'msg_example' # str | Chat message (optional)
    doc_ids = 'doc_ids_example' # str | Document IDs to reference (optional)
    action = 'action_example' # str | Action (optional)
    stream = True # bool | Stream the response (optional)
    response_format = 'response_format_example' # str | Response format (html or text) (optional)

    try:
        api_response = api_instance.chat(page=page, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id, msg=msg, doc_ids=doc_ids, action=action, stream=stream, response_format=response_format)
        print("The response of ChatApi->chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **x_caller_id** | **str**| Optional ID of the application calling the ID, used in conjunction with the caller_thread_id | [optional] 
 **x_caller_thread_id** | **str**| Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. | [optional] 
 **msg** | **str**| Chat message | [optional] 
 **doc_ids** | **str**| Document IDs to reference | [optional] 
 **action** | **str**| Action | [optional] 
 **stream** | **bool**| Stream the response | [optional] 
 **response_format** | **str**| Response format (html or text) | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat response |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_history**
> ChatHistory200Response chat_history(page=page, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id, last_created_date=last_created_date, sort_order=sort_order)



Get chat history

### Example


```python
import pp_sdk
from pp_sdk.models.chat_history200_response import ChatHistory200Response
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
    api_instance = pp_sdk.ChatApi(api_client)
    page = 56 # int | Page number (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    x_caller_id = 'x_caller_id_example' # str | Optional ID of the application calling the ID, used in conjunction with the caller_thread_id (optional)
    x_caller_thread_id = 'x_caller_thread_id_example' # str | Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. (optional)
    last_created_date = 'last_created_date_example' # str | Last created date (optional)
    sort_order = 'sort_order_example' # str | Sort order (asc/desc) (optional)

    try:
        api_response = api_instance.chat_history(page=page, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id, last_created_date=last_created_date, sort_order=sort_order)
        print("The response of ChatApi->chat_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->chat_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **x_caller_id** | **str**| Optional ID of the application calling the ID, used in conjunction with the caller_thread_id | [optional] 
 **x_caller_thread_id** | **str**| Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. | [optional] 
 **last_created_date** | **str**| Last created date | [optional] 
 **sort_order** | **str**| Sort order (asc/desc) | [optional] 

### Return type

[**ChatHistory200Response**](ChatHistory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat history retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_read**
> ChatRead200Response chat_read(thread_id, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id)



Get a specific chat thread

### Example


```python
import pp_sdk
from pp_sdk.models.chat_read200_response import ChatRead200Response
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
    api_instance = pp_sdk.ChatApi(api_client)
    thread_id = 'thread_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    x_caller_id = 'x_caller_id_example' # str | Optional ID of the application calling the ID, used in conjunction with the caller_thread_id (optional)
    x_caller_thread_id = 'x_caller_thread_id_example' # str | Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. (optional)

    try:
        api_response = api_instance.chat_read(thread_id, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id)
        print("The response of ChatApi->chat_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->chat_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **x_caller_id** | **str**| Optional ID of the application calling the ID, used in conjunction with the caller_thread_id | [optional] 
 **x_caller_thread_id** | **str**| Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. | [optional] 

### Return type

[**ChatRead200Response**](ChatRead200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chat thread retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_upload_file**
> ChatUploadFile200Response chat_upload_file(file, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id, filename=filename, content_type=content_type)



Upload a file

### Example


```python
import pp_sdk
from pp_sdk.models.chat_upload_file200_response import ChatUploadFile200Response
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
    api_instance = pp_sdk.ChatApi(api_client)
    file = None # bytearray | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    x_caller_id = 'x_caller_id_example' # str | Optional ID of the application calling the ID, used in conjunction with the caller_thread_id (optional)
    x_caller_thread_id = 'x_caller_thread_id_example' # str | Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. (optional)
    filename = 'filename_example' # str |  (optional)
    content_type = 'content_type_example' # str |  (optional)

    try:
        api_response = api_instance.chat_upload_file(file, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id, filename=filename, content_type=content_type)
        print("The response of ChatApi->chat_upload_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->chat_upload_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **x_caller_id** | **str**| Optional ID of the application calling the ID, used in conjunction with the caller_thread_id | [optional] 
 **x_caller_thread_id** | **str**| Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. | [optional] 
 **filename** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

[**ChatUploadFile200Response**](ChatUploadFile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File uploaded successfully |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

