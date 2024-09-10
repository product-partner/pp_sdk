# pp_sdk.ApiApi

All URIs are relative to *http://0.0.0.0:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_goals_create**](ApiApi.md#api_goals_create) | **POST** /api/goals/ | 
[**api_goals_delete**](ApiApi.md#api_goals_delete) | **DELETE** /api/goals/{goal_id}/ | 
[**api_goals_list**](ApiApi.md#api_goals_list) | **GET** /api/goals/ | 
[**api_goals_partial_update**](ApiApi.md#api_goals_partial_update) | **PATCH** /api/goals/{goal_id}/ | 
[**api_goals_read**](ApiApi.md#api_goals_read) | **GET** /api/goals/{goal_id}/ | 
[**api_goals_search_list**](ApiApi.md#api_goals_search_list) | **GET** /api/goals/search/ | 
[**api_goals_update**](ApiApi.md#api_goals_update) | **PUT** /api/goals/{goal_id}/ | 
[**api_prds_create**](ApiApi.md#api_prds_create) | **POST** /api/prds/ | 
[**api_prds_delete**](ApiApi.md#api_prds_delete) | **DELETE** /api/prds/{id}/ | 
[**api_prds_list**](ApiApi.md#api_prds_list) | **GET** /api/prds/ | 
[**api_prds_partial_update**](ApiApi.md#api_prds_partial_update) | **PATCH** /api/prds/{id}/ | 
[**api_prds_read**](ApiApi.md#api_prds_read) | **GET** /api/prds/{id}/ | 
[**api_prds_search_list**](ApiApi.md#api_prds_search_list) | **GET** /api/prds/search/ | 
[**api_prds_update**](ApiApi.md#api_prds_update) | **PUT** /api/prds/{id}/ | 
[**api_programs_create**](ApiApi.md#api_programs_create) | **POST** /api/programs/ | 
[**api_programs_delete**](ApiApi.md#api_programs_delete) | **DELETE** /api/programs/{program_id}/ | 
[**api_programs_list**](ApiApi.md#api_programs_list) | **GET** /api/programs/ | 
[**api_programs_partial_update**](ApiApi.md#api_programs_partial_update) | **PATCH** /api/programs/{program_id}/ | 
[**api_programs_read**](ApiApi.md#api_programs_read) | **GET** /api/programs/{program_id}/ | 
[**api_programs_search_list**](ApiApi.md#api_programs_search_list) | **GET** /api/programs/search | 
[**api_programs_update**](ApiApi.md#api_programs_update) | **PUT** /api/programs/{program_id}/ | 
[**api_status_create**](ApiApi.md#api_status_create) | **POST** /api/status/ | 
[**api_status_delete**](ApiApi.md#api_status_delete) | **DELETE** /api/status/{status_id}/ | 
[**api_status_list**](ApiApi.md#api_status_list) | **GET** /api/status/ | 
[**api_status_partial_update**](ApiApi.md#api_status_partial_update) | **PATCH** /api/status/{status_id}/ | 
[**api_status_read**](ApiApi.md#api_status_read) | **GET** /api/status/{status_id}/ | 
[**api_status_update**](ApiApi.md#api_status_update) | **PUT** /api/status/{status_id}/ | 
[**api_user_create_create**](ApiApi.md#api_user_create_create) | **POST** /api/user/create/ | 
[**api_user_read**](ApiApi.md#api_user_read) | **GET** /api/user/ | 
[**api_user_search_list**](ApiApi.md#api_user_search_list) | **GET** /api/user/search/ | 
[**api_user_update_partial_update**](ApiApi.md#api_user_update_partial_update) | **PATCH** /api/user/update/ | 
[**api_user_update_update**](ApiApi.md#api_user_update_update) | **PUT** /api/user/update/ | 
[**api_userstories_create**](ApiApi.md#api_userstories_create) | **POST** /api/userstories/ | 
[**api_userstories_delete**](ApiApi.md#api_userstories_delete) | **DELETE** /api/userstories/{id}/ | 
[**api_userstories_list**](ApiApi.md#api_userstories_list) | **GET** /api/userstories/ | 
[**api_userstories_partial_update**](ApiApi.md#api_userstories_partial_update) | **PATCH** /api/userstories/{id}/ | 
[**api_userstories_read**](ApiApi.md#api_userstories_read) | **GET** /api/userstories/{id}/ | 
[**api_userstories_search_list**](ApiApi.md#api_userstories_search_list) | **GET** /api/userstories/search | 
[**api_userstories_update**](ApiApi.md#api_userstories_update) | **PUT** /api/userstories/{id}/ | 


# **api_goals_create**
> Goal api_goals_create(data)



Create a new goal.

### Example


```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.ApiApi(api_client)
    data = pp_sdk.Goal() # Goal | 

    try:
        api_response = api_instance.api_goals_create(data)
        print("The response of ApiApi->api_goals_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Goal**](Goal.md)|  | 

### Return type

[**Goal**](Goal.md)

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

# **api_goals_delete**
> api_goals_delete(goal_id)



Delete a specific goal.

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
    api_instance = pp_sdk.ApiApi(api_client)
    goal_id = 'goal_id_example' # str | 

    try:
        api_instance.api_goals_delete(goal_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 

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

# **api_goals_list**
> List[Goal] api_goals_list(x_user_id=x_user_id)



Get a list of all goals for the authenticated user.

### Example


```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.ApiApi(api_client)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_goals_list(x_user_id=x_user_id)
        print("The response of ApiApi->api_goals_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Goal]**](Goal.md)

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

# **api_goals_partial_update**
> Goal api_goals_partial_update(goal_id, data)



Partially update a specific goal.

### Example


```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.ApiApi(api_client)
    goal_id = 'goal_id_example' # str | 
    data = pp_sdk.Goal() # Goal | 

    try:
        api_response = api_instance.api_goals_partial_update(goal_id, data)
        print("The response of ApiApi->api_goals_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 
 **data** | [**Goal**](Goal.md)|  | 

### Return type

[**Goal**](Goal.md)

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

# **api_goals_read**
> Goal api_goals_read(goal_id)



Get details of a specific goal.

### Example


```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.ApiApi(api_client)
    goal_id = 'goal_id_example' # str | 

    try:
        api_response = api_instance.api_goals_read(goal_id)
        print("The response of ApiApi->api_goals_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 

### Return type

[**Goal**](Goal.md)

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

# **api_goals_search_list**
> List[Goal] api_goals_search_list(search=search, stakeholders_users=stakeholders_users, status=status, sort=sort, limit=limit, x_user_id=x_user_id)



Search for PRDs

### Example


```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.ApiApi(api_client)
    search = 'search_example' # str | Search term for goal name, language, or description (optional)
    stakeholders_users = 'stakeholders_users_example' # str | Comma-separated list of stakeholder IDs (optional)
    status = 'status_example' # str | Filter by status (optional)
    sort = 'sort_example' # str | Sort field (prefix with '-' for descending order) (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_goals_search_list(search=search, stakeholders_users=stakeholders_users, status=status, sort=sort, limit=limit, x_user_id=x_user_id)
        print("The response of ApiApi->api_goals_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term for goal name, language, or description | [optional] 
 **stakeholders_users** | **str**| Comma-separated list of stakeholder IDs | [optional] 
 **status** | **str**| Filter by status | [optional] 
 **sort** | **str**| Sort field (prefix with &#39;-&#39; for descending order) | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Goal]**](Goal.md)

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

# **api_goals_update**
> Goal api_goals_update(goal_id, data)



Update a specific goal.

### Example


```python
import pp_sdk
from pp_sdk.models.goal import Goal
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
    api_instance = pp_sdk.ApiApi(api_client)
    goal_id = 'goal_id_example' # str | 
    data = pp_sdk.Goal() # Goal | 

    try:
        api_response = api_instance.api_goals_update(goal_id, data)
        print("The response of ApiApi->api_goals_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_id** | **str**|  | 
 **data** | [**Goal**](Goal.md)|  | 

### Return type

[**Goal**](Goal.md)

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

# **api_prds_create**
> PRD api_prds_create(data, x_user_id=x_user_id)



Create a new PRD for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.prd import PRD
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
    api_instance = pp_sdk.ApiApi(api_client)
    data = pp_sdk.PRD() # PRD | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_create(data, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PRD**](PRD.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRD**](PRD.md)

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

# **api_prds_delete**
> api_prds_delete(id, x_user_id=x_user_id)



Delete a specific PRD.

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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.api_prds_delete(id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_delete: %s\n" % e)
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

# **api_prds_list**
> List[PRD] api_prds_list(page=page, x_user_id=x_user_id)



Get a list of all PRDs for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.prd import PRD
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
    api_instance = pp_sdk.ApiApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_list(page=page, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[PRD]**](PRD.md)

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

# **api_prds_partial_update**
> PRDDetail api_prds_partial_update(id, data, x_user_id=x_user_id)



Partially update a specific PRD.

### Example


```python
import pp_sdk
from pp_sdk.models.prd_detail import PRDDetail
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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | 
    data = pp_sdk.PRDDetail() # PRDDetail | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_partial_update(id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**PRDDetail**](PRDDetail.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRDDetail**](PRDDetail.md)

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

# **api_prds_read**
> PRDDetail api_prds_read(id, x_user_id=x_user_id)



Get details of a specific PRD.

### Example


```python
import pp_sdk
from pp_sdk.models.prd_detail import PRDDetail
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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_read(id, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRDDetail**](PRDDetail.md)

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

# **api_prds_search_list**
> List[PRD] api_prds_search_list(q=q, x_user_id=x_user_id)



Search for PRDs

### Example


```python
import pp_sdk
from pp_sdk.models.prd import PRD
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
    api_instance = pp_sdk.ApiApi(api_client)
    q = 'q_example' # str | query string, to search across name or description (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_search_list(q=q, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| query string, to search across name or description | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[PRD]**](PRD.md)

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

# **api_prds_update**
> PRDDetail api_prds_update(id, data, x_user_id=x_user_id)



Update a specific PRD.

### Example


```python
import pp_sdk
from pp_sdk.models.prd_detail import PRDDetail
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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | 
    data = pp_sdk.PRDDetail() # PRDDetail | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_update(id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**PRDDetail**](PRDDetail.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRDDetail**](PRDDetail.md)

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

# **api_programs_create**
> Program api_programs_create(data)



### Example


```python
import pp_sdk
from pp_sdk.models.program import Program
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
    api_instance = pp_sdk.ApiApi(api_client)
    data = pp_sdk.Program() # Program | 

    try:
        api_response = api_instance.api_programs_create(data)
        print("The response of ApiApi->api_programs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Program**](Program.md)|  | 

### Return type

[**Program**](Program.md)

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

# **api_programs_delete**
> api_programs_delete(program_id, x_user_id=x_user_id)



Delete a specific program.

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
    api_instance = pp_sdk.ApiApi(api_client)
    program_id = 'program_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.api_programs_delete(program_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**|  | 
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

# **api_programs_list**
> ApiProgramsList200Response api_programs_list(page=page)



### Example


```python
import pp_sdk
from pp_sdk.models.api_programs_list200_response import ApiProgramsList200Response
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
    api_instance = pp_sdk.ApiApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.api_programs_list(page=page)
        print("The response of ApiApi->api_programs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**ApiProgramsList200Response**](ApiProgramsList200Response.md)

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

# **api_programs_partial_update**
> Program api_programs_partial_update(program_id, data, x_user_id=x_user_id)



Partially update a specific program.

### Example


```python
import pp_sdk
from pp_sdk.models.program import Program
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
    api_instance = pp_sdk.ApiApi(api_client)
    program_id = 'program_id_example' # str | 
    data = pp_sdk.Program() # Program | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_programs_partial_update(program_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_programs_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**|  | 
 **data** | [**Program**](Program.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Program**](Program.md)

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

# **api_programs_read**
> Program api_programs_read(program_id, x_user_id=x_user_id)



Get details of a specific program.

### Example


```python
import pp_sdk
from pp_sdk.models.program import Program
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
    api_instance = pp_sdk.ApiApi(api_client)
    program_id = 'program_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_programs_read(program_id, x_user_id=x_user_id)
        print("The response of ApiApi->api_programs_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Program**](Program.md)

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

# **api_programs_search_list**
> List[Program] api_programs_search_list(tags=tags, search=search, sort=sort, limit=limit, x_user_id=x_user_id)



Search for programs

### Example


```python
import pp_sdk
from pp_sdk.models.program import Program
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
    api_instance = pp_sdk.ApiApi(api_client)
    tags = 'tags_example' # str | Comma-separated list of tags (optional)
    search = 'search_example' # str | Search term for name and description (optional)
    sort = 'sort_example' # str | Sort field (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_programs_search_list(tags=tags, search=search, sort=sort, limit=limit, x_user_id=x_user_id)
        print("The response of ApiApi->api_programs_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| Comma-separated list of tags | [optional] 
 **search** | **str**| Search term for name and description | [optional] 
 **sort** | **str**| Sort field | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Program]**](Program.md)

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

# **api_programs_update**
> Program api_programs_update(program_id, data, x_user_id=x_user_id)



Update a specific program.

### Example


```python
import pp_sdk
from pp_sdk.models.program import Program
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
    api_instance = pp_sdk.ApiApi(api_client)
    program_id = 'program_id_example' # str | 
    data = pp_sdk.Program() # Program | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_programs_update(program_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_programs_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**|  | 
 **data** | [**Program**](Program.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Program**](Program.md)

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

# **api_status_create**
> Status api_status_create(data, x_user_id=x_user_id)



Create a new status for the authenticated user.

### Example


```python
import pp_sdk
from pp_sdk.models.status import Status
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
    api_instance = pp_sdk.ApiApi(api_client)
    data = pp_sdk.Status() # Status | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_status_create(data, x_user_id=x_user_id)
        print("The response of ApiApi->api_status_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_status_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Status**](Status.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Status**](Status.md)

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

# **api_status_delete**
> api_status_delete(status_id, x_user_id=x_user_id)



Delete a specific status.

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
    api_instance = pp_sdk.ApiApi(api_client)
    status_id = 'status_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.api_status_delete(status_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_status_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**|  | 
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

# **api_status_list**
> List[Status] api_status_list(page=page, x_user_id=x_user_id)



Get a list of all statuses for the authenticated user.

### Example


```python
import pp_sdk
from pp_sdk.models.status import Status
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
    api_instance = pp_sdk.ApiApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_status_list(page=page, x_user_id=x_user_id)
        print("The response of ApiApi->api_status_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_status_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Status]**](Status.md)

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

# **api_status_partial_update**
> Status api_status_partial_update(status_id, data, x_user_id=x_user_id)



Partially update a specific status.

### Example


```python
import pp_sdk
from pp_sdk.models.status import Status
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
    api_instance = pp_sdk.ApiApi(api_client)
    status_id = 'status_id_example' # str | 
    data = pp_sdk.Status() # Status | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_status_partial_update(status_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_status_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_status_partial_update: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_status_read**
> Status api_status_read(status_id, x_user_id=x_user_id)



Get details of a specific status.

### Example


```python
import pp_sdk
from pp_sdk.models.status import Status
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
    api_instance = pp_sdk.ApiApi(api_client)
    status_id = 'status_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_status_read(status_id, x_user_id=x_user_id)
        print("The response of ApiApi->api_status_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_status_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Status**](Status.md)

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

# **api_status_update**
> Status api_status_update(status_id, data, x_user_id=x_user_id)



Update a specific status.

### Example


```python
import pp_sdk
from pp_sdk.models.status import Status
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
    api_instance = pp_sdk.ApiApi(api_client)
    status_id = 'status_id_example' # str | 
    data = pp_sdk.Status() # Status | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_status_update(status_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_status_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_status_update: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_create_create**
> UserCreate api_user_create_create(data)



### Example


```python
import pp_sdk
from pp_sdk.models.user_create import UserCreate
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
    api_instance = pp_sdk.ApiApi(api_client)
    data = pp_sdk.UserCreate() # UserCreate | 

    try:
        api_response = api_instance.api_user_create_create(data)
        print("The response of ApiApi->api_user_create_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_create_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserCreate**](UserCreate.md)

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

# **api_user_read**
> User api_user_read(id)



Retrieve details of a specific user

### Example


```python
import pp_sdk
from pp_sdk.models.user import User
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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | UUID of the user to retrieve

    try:
        api_response = api_instance.api_user_read(id)
        print("The response of ApiApi->api_user_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID of the user to retrieve | 

### Return type

[**User**](User.md)

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

# **api_user_search_list**
> ApiUserSearchList200Response api_user_search_list(domain, page=page, search=search)



Search for users

### Example


```python
import pp_sdk
from pp_sdk.models.api_user_search_list200_response import ApiUserSearchList200Response
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
    api_instance = pp_sdk.ApiApi(api_client)
    domain = 'domain_example' # str | Domain to filter users
    page = 56 # int | A page number within the paginated result set. (optional)
    search = 'search_example' # str | Search term for user's email, first name, or last name (optional)

    try:
        api_response = api_instance.api_user_search_list(domain, page=page, search=search)
        print("The response of ApiApi->api_user_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain to filter users | 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **search** | **str**| Search term for user&#39;s email, first name, or last name | [optional] 

### Return type

[**ApiUserSearchList200Response**](ApiUserSearchList200Response.md)

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

# **api_user_update_partial_update**
> UserUpdate api_user_update_partial_update(data)



### Example


```python
import pp_sdk
from pp_sdk.models.user_update import UserUpdate
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
    api_instance = pp_sdk.ApiApi(api_client)
    data = pp_sdk.UserUpdate() # UserUpdate | 

    try:
        api_response = api_instance.api_user_update_partial_update(data)
        print("The response of ApiApi->api_user_update_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_update_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**UserUpdate**](UserUpdate.md)

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

# **api_user_update_update**
> UserUpdate api_user_update_update(id, data)



Update a specific user's details

### Example


```python
import pp_sdk
from pp_sdk.models.user_update import UserUpdate
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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | UUID of the user to update
    data = pp_sdk.UserUpdate() # UserUpdate | 

    try:
        api_response = api_instance.api_user_update_update(id, data)
        print("The response of ApiApi->api_user_update_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_update_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID of the user to update | 
 **data** | [**UserUpdate**](UserUpdate.md)|  | 

### Return type

[**UserUpdate**](UserUpdate.md)

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

# **api_userstories_create**
> UserStory api_userstories_create(data, x_user_id=x_user_id)



Create a new user story for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
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
    api_instance = pp_sdk.ApiApi(api_client)
    data = pp_sdk.UserStory() # UserStory | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_create(data, x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_userstories_delete**
> api_userstories_delete(id, x_user_id=x_user_id)



Delete a specific user story.

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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.api_userstories_delete(id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_delete: %s\n" % e)
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

# **api_userstories_list**
> List[UserStory] api_userstories_list(x_user_id=x_user_id)



Get a list of all user stories for the authenticated user's organization.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
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
    api_instance = pp_sdk.ApiApi(api_client)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_list(x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

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

# **api_userstories_partial_update**
> UserStory api_userstories_partial_update(id, data, x_user_id=x_user_id)



Partially update a specific user story.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | 
    data = pp_sdk.UserStory() # UserStory | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_partial_update(id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **api_userstories_read**
> UserStory api_userstories_read(id, x_user_id=x_user_id)



Get details of a specific user story.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_read(id, x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

# **api_userstories_search_list**
> List[UserStory] api_userstories_search_list(status=status, search=search, sort=sort, limit=limit, x_user_id=x_user_id)



Search and filter UserStory data

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
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
    api_instance = pp_sdk.ApiApi(api_client)
    status = 'status_example' # str | Filter by status (optional)
    search = 'search_example' # str | Search string for as_a, i_want_to, so_that, or freetext_override fields (optional)
    sort = 'sort_example' # str | Sort field (created_at, updated_at, due_date, priority, status). Use '-' prefix for descending order (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_search_list(status=status, search=search, sort=sort, limit=limit, x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_search_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_search_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by status | [optional] 
 **search** | **str**| Search string for as_a, i_want_to, so_that, or freetext_override fields | [optional] 
 **sort** | **str**| Sort field (created_at, updated_at, due_date, priority, status). Use &#39;-&#39; prefix for descending order | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

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

# **api_userstories_update**
> UserStory api_userstories_update(id, data, x_user_id=x_user_id)



Update a specific user story.

### Example


```python
import pp_sdk
from pp_sdk.models.user_story import UserStory
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
    api_instance = pp_sdk.ApiApi(api_client)
    id = 'id_example' # str | 
    data = pp_sdk.UserStory() # UserStory | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_update(id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

