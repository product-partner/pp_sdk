# pp_sdk.GoalsApi

All URIs are relative to *http://localhost:8000/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**goals_create**](GoalsApi.md#goals_create) | **POST** /goals/ | 
[**goals_delete**](GoalsApi.md#goals_delete) | **DELETE** /goals/{goal_id}/ | 
[**goals_list**](GoalsApi.md#goals_list) | **GET** /goals/ | 
[**goals_partial_update**](GoalsApi.md#goals_partial_update) | **PATCH** /goals/{goal_id}/ | 
[**goals_picker_list**](GoalsApi.md#goals_picker_list) | **GET** /goals/picker/ | 
[**goals_read**](GoalsApi.md#goals_read) | **GET** /goals/{goal_id}/ | 
[**goals_update**](GoalsApi.md#goals_update) | **PUT** /goals/{goal_id}/ | 


# **goals_create**
> Goal goals_create(data)



Create a new goal.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.GoalsApi(api_client)
    data = pp_sdk.Goal() # Goal | 

    try:
        api_response = api_instance.goals_create(data)
        print("The response of GoalsApi->goals_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->goals_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Goal**](Goal.md)|  | 

### Return type

[**Goal**](Goal.md)

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

# **goals_delete**
> goals_delete(goal_id)



Delete a specific goal.

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
    api_instance = pp_sdk.GoalsApi(api_client)
    goal_id = 'goal_id_example' # str | 

    try:
        api_instance.goals_delete(goal_id)
    except Exception as e:
        print("Exception when calling GoalsApi->goals_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **goals_list**
> List[Goal] goals_list(search=search, stakeholder_users=stakeholder_users, status=status, sort=sort, limit=limit, tags=tags, program=program, created_by=created_by, x_user_id=x_user_id)



List or Search for Goals

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.GoalsApi(api_client)
    search = 'search_example' # str | Search term for goal name, language, or description (optional)
    stakeholder_users = 'stakeholder_users_example' # str | Comma-separated list of stakeholder IDs (optional)
    status = 'status_example' # str | Filter by status (optional)
    sort = 'sort_example' # str | Sort field (prefix with '-' for descending order) (optional)
    limit = 56 # int | Limit the number of results (optional)
    tags = 'tags_example' # str | Filter by tags, one or more (optional)
    program = 'program_example' # str | Filter by program UUID or name (optional)
    created_by = 'created_by_example' # str | Filter to the objects created by this user (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.goals_list(search=search, stakeholder_users=stakeholder_users, status=status, sort=sort, limit=limit, tags=tags, program=program, created_by=created_by, x_user_id=x_user_id)
        print("The response of GoalsApi->goals_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->goals_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term for goal name, language, or description | [optional] 
 **stakeholder_users** | **str**| Comma-separated list of stakeholder IDs | [optional] 
 **status** | **str**| Filter by status | [optional] 
 **sort** | **str**| Sort field (prefix with &#39;-&#39; for descending order) | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **tags** | **str**| Filter by tags, one or more | [optional] 
 **program** | **str**| Filter by program UUID or name | [optional] 
 **created_by** | **str**| Filter to the objects created by this user | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Goal]**](Goal.md)

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

# **goals_partial_update**
> Goal goals_partial_update(goal_id, data)



Partially update a specific goal.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.GoalsApi(api_client)
    goal_id = 'goal_id_example' # str | 
    data = pp_sdk.Goal() # Goal | 

    try:
        api_response = api_instance.goals_partial_update(goal_id, data)
        print("The response of GoalsApi->goals_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->goals_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 
 **data** | [**Goal**](Goal.md)|  | 

### Return type

[**Goal**](Goal.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **goals_picker_list**
> List[GoalPicker] goals_picker_list(status=status, search=search, x_user_id=x_user_id)



List or Search for Goals in picker, a reduced set of functions and returned values but lighter weight and faster.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.goal_picker import GoalPicker
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
    api_instance = pp_sdk.GoalsApi(api_client)
    status = 'status_example' # str | Optional filter to include all goals, pass 'all' or another status. (optional)
    search = 'search_example' # str | Search term for goal name, language, or description (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.goals_picker_list(status=status, search=search, x_user_id=x_user_id)
        print("The response of GoalsApi->goals_picker_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->goals_picker_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Optional filter to include all goals, pass &#39;all&#39; or another status. | [optional] 
 **search** | **str**| Search term for goal name, language, or description | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[GoalPicker]**](GoalPicker.md)

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

# **goals_read**
> Goal goals_read(goal_id)



Get details of a specific goal.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.GoalsApi(api_client)
    goal_id = 'goal_id_example' # str | 

    try:
        api_response = api_instance.goals_read(goal_id)
        print("The response of GoalsApi->goals_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->goals_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 

### Return type

[**Goal**](Goal.md)

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

# **goals_update**
> Goal goals_update(goal_id, data)



Update a specific goal.

### Example

* Api Key Authentication (UserIdAuth):
* Api Key Authentication (ApiKeyAuth):

```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.GoalsApi(api_client)
    goal_id = 'goal_id_example' # str | 
    data = pp_sdk.Goal() # Goal | 

    try:
        api_response = api_instance.goals_update(goal_id, data)
        print("The response of GoalsApi->goals_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->goals_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 
 **data** | [**Goal**](Goal.md)|  | 

### Return type

[**Goal**](Goal.md)

### Authorization

[UserIdAuth](../README.md#UserIdAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

