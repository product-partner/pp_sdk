# pp_sdk.ApiApi

All URIs are relative to *http://0.0.0.0:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_goals_create**](ApiApi.md#api_goals_create) | **POST** /api/goals/ | 
[**api_goals_delete**](ApiApi.md#api_goals_delete) | **DELETE** /api/goals/{goal_id}/ | 
[**api_goals_list**](ApiApi.md#api_goals_list) | **GET** /api/goals/ | 
[**api_goals_partial_update**](ApiApi.md#api_goals_partial_update) | **PATCH** /api/goals/{goal_id}/ | 
[**api_goals_picker_list**](ApiApi.md#api_goals_picker_list) | **GET** /api/goals/picker/ | 
[**api_goals_read**](ApiApi.md#api_goals_read) | **GET** /api/goals/{goal_id}/ | 
[**api_goals_update**](ApiApi.md#api_goals_update) | **PUT** /api/goals/{goal_id}/ | 
[**api_prds_create**](ApiApi.md#api_prds_create) | **POST** /api/prds/ | 
[**api_prds_delete**](ApiApi.md#api_prds_delete) | **DELETE** /api/prds/{prd_id}/ | 
[**api_prds_list**](ApiApi.md#api_prds_list) | **GET** /api/prds/ | 
[**api_prds_partial_update**](ApiApi.md#api_prds_partial_update) | **PATCH** /api/prds/{prd_id}/ | 
[**api_prds_read**](ApiApi.md#api_prds_read) | **GET** /api/prds/{prd_id}/ | 
[**api_prds_update**](ApiApi.md#api_prds_update) | **PUT** /api/prds/{prd_id}/ | 
[**api_programs_create**](ApiApi.md#api_programs_create) | **POST** /api/programs/ | 
[**api_programs_delete**](ApiApi.md#api_programs_delete) | **DELETE** /api/programs/{program_id}/ | 
[**api_programs_list**](ApiApi.md#api_programs_list) | **GET** /api/programs/ | 
[**api_programs_partial_update**](ApiApi.md#api_programs_partial_update) | **PATCH** /api/programs/{program_id}/ | 
[**api_programs_picker_list**](ApiApi.md#api_programs_picker_list) | **GET** /api/programs/picker/ | 
[**api_programs_read**](ApiApi.md#api_programs_read) | **GET** /api/programs/{program_id}/ | 
[**api_programs_update**](ApiApi.md#api_programs_update) | **PUT** /api/programs/{program_id}/ | 
[**api_status_create**](ApiApi.md#api_status_create) | **POST** /api/status/ | 
[**api_status_delete**](ApiApi.md#api_status_delete) | **DELETE** /api/status/{status_id}/ | 
[**api_status_list**](ApiApi.md#api_status_list) | **GET** /api/status/ | 
[**api_status_partial_update**](ApiApi.md#api_status_partial_update) | **PATCH** /api/status/{status_id}/ | 
[**api_status_read**](ApiApi.md#api_status_read) | **GET** /api/status/{status_id}/ | 
[**api_status_update**](ApiApi.md#api_status_update) | **PUT** /api/status/{status_id}/ | 
[**api_tags_create**](ApiApi.md#api_tags_create) | **POST** /api/tags/ | 
[**api_tags_delete**](ApiApi.md#api_tags_delete) | **DELETE** /api/tags/{tag_id}/ | 
[**api_tags_list**](ApiApi.md#api_tags_list) | **GET** /api/tags/ | 
[**api_tags_partial_update**](ApiApi.md#api_tags_partial_update) | **PATCH** /api/tags/{tag_id}/ | 
[**api_tags_read**](ApiApi.md#api_tags_read) | **GET** /api/tags/{tag_id}/ | 
[**api_tags_update**](ApiApi.md#api_tags_update) | **PUT** /api/tags/{tag_id}/ | 
[**api_user_create**](ApiApi.md#api_user_create) | **POST** /api/user/ | 
[**api_user_delete**](ApiApi.md#api_user_delete) | **DELETE** /api/user/{id}/ | 
[**api_user_list**](ApiApi.md#api_user_list) | **GET** /api/user/ | 
[**api_user_partial_update**](ApiApi.md#api_user_partial_update) | **PATCH** /api/user/{id}/ | 
[**api_user_picker_list**](ApiApi.md#api_user_picker_list) | **GET** /api/user/picker/ | 
[**api_user_read**](ApiApi.md#api_user_read) | **GET** /api/user/{id}/ | 
[**api_user_update**](ApiApi.md#api_user_update) | **PUT** /api/user/{id}/ | 
[**api_userstories_create**](ApiApi.md#api_userstories_create) | **POST** /api/userstories/ | 
[**api_userstories_delete**](ApiApi.md#api_userstories_delete) | **DELETE** /api/userstories/{userstory_id}/ | 
[**api_userstories_list**](ApiApi.md#api_userstories_list) | **GET** /api/userstories/ | 
[**api_userstories_partial_update**](ApiApi.md#api_userstories_partial_update) | **PATCH** /api/userstories/{userstory_id}/ | 
[**api_userstories_read**](ApiApi.md#api_userstories_read) | **GET** /api/userstories/{userstory_id}/ | 
[**api_userstories_update**](ApiApi.md#api_userstories_update) | **PUT** /api/userstories/{userstory_id}/ | 


# **api_goals_create**
> Goal api_goals_create(data)



Create a new goal.

### Example

```python
import time
import os
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
import time
import os
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
> List[Goal] api_goals_list(page=page, search=search, stakeholder_users=stakeholder_users, status=status, sort=sort, limit=limit, tags=tags, x_user_id=x_user_id)



List or Search for Goals

### Example

```python
import time
import os
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
    page = 56 # int | A page number within the paginated result set. (optional)
    search = 'search_example' # str | Search term for goal name, language, or description (optional)
    stakeholder_users = 'stakeholder_users_example' # str | Comma-separated list of stakeholder IDs (optional)
    status = 'status_example' # str | Filter by status (optional)
    sort = 'sort_example' # str | Sort field (prefix with '-' for descending order) (optional)
    limit = 56 # int | Limit the number of results (optional)
    tags = 'tags_example' # str | Filter by tags, one or more (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_goals_list(page=page, search=search, stakeholder_users=stakeholder_users, status=status, sort=sort, limit=limit, tags=tags, x_user_id=x_user_id)
        print("The response of ApiApi->api_goals_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **search** | **str**| Search term for goal name, language, or description | [optional] 
 **stakeholder_users** | **str**| Comma-separated list of stakeholder IDs | [optional] 
 **status** | **str**| Filter by status | [optional] 
 **sort** | **str**| Sort field (prefix with &#39;-&#39; for descending order) | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **tags** | **str**| Filter by tags, one or more | [optional] 
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
import time
import os
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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_goals_picker_list**
> ApiGoalsPickerList200Response api_goals_picker_list(page=page)



### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.api_goals_picker_list200_response import ApiGoalsPickerList200Response
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
        api_response = api_instance.api_goals_picker_list(page=page)
        print("The response of ApiApi->api_goals_picker_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_goals_picker_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**ApiGoalsPickerList200Response**](ApiGoalsPickerList200Response.md)

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

# **api_goals_read**
> Goal api_goals_read(goal_id)



Get details of a specific goal.

### Example

```python
import time
import os
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

# **api_goals_update**
> Goal api_goals_update(goal_id, data)



Update a specific goal.

### Example

```python
import time
import os
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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_prds_create**
> PRD api_prds_create(data, x_user_id=x_user_id)



Create a new PRD for the authenticated user's organization.

### Example

```python
import time
import os
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
> api_prds_delete(prd_id, x_user_id=x_user_id)



Delete a specific PRD.

### Example

```python
import time
import os
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
    prd_id = 'prd_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.api_prds_delete(prd_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prd_id** | **str**|  | 
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
> List[PRD] api_prds_list(x_user_id=x_user_id, stakeholders=stakeholders, status=status, search=search, sort=sort, limit=limit, tags=tags)



Get a list of all PRDs for the authenticated user's organization.

### Example

```python
import time
import os
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
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    stakeholders = 'stakeholders_example' # str | Comma-separated list of stakeholder user IDs to filter by (optional)
    status = 'status_example' # str | Status to filter by (optional)
    search = 'search_example' # str | Search term to filter PRDs by title, description, or body (optional)
    sort = 'sort_example' # str | Field to sort by (e.g., 'title', '-created_date') (optional)
    limit = 56 # int | Limit the number of PRDs returned (optional)
    tags = 'tags_example' # str | Comma-separated list of tag names to filter PRDs by (optional)

    try:
        api_response = api_instance.api_prds_list(x_user_id=x_user_id, stakeholders=stakeholders, status=status, search=search, sort=sort, limit=limit, tags=tags)
        print("The response of ApiApi->api_prds_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **stakeholders** | **str**| Comma-separated list of stakeholder user IDs to filter by | [optional] 
 **status** | **str**| Status to filter by | [optional] 
 **search** | **str**| Search term to filter PRDs by title, description, or body | [optional] 
 **sort** | **str**| Field to sort by (e.g., &#39;title&#39;, &#39;-created_date&#39;) | [optional] 
 **limit** | **int**| Limit the number of PRDs returned | [optional] 
 **tags** | **str**| Comma-separated list of tag names to filter PRDs by | [optional] 

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
> PRD api_prds_partial_update(prd_id, data, x_user_id=x_user_id)



Partially update a specific PRD.

### Example

```python
import time
import os
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
    prd_id = 'prd_id_example' # str | 
    data = pp_sdk.PRD() # PRD | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_partial_update(prd_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prd_id** | **str**|  | 
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_prds_read**
> PRD api_prds_read(prd_id, x_user_id=x_user_id)



Get details of a specific PRD.

### Example

```python
import time
import os
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
    prd_id = 'prd_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_read(prd_id, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prd_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**PRD**](PRD.md)

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
> PRD api_prds_update(prd_id, data, x_user_id=x_user_id)



Update a specific PRD.

### Example

```python
import time
import os
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
    prd_id = 'prd_id_example' # str | 
    data = pp_sdk.PRD() # PRD | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_prds_update(prd_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_prds_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_prds_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prd_id** | **str**|  | 
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_programs_create**
> Program api_programs_create(data, x_user_id=x_user_id)



Create a new program for the authenticated user.

### Example

```python
import time
import os
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
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_programs_create(data, x_user_id=x_user_id)
        print("The response of ApiApi->api_programs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_programs_delete**
> api_programs_delete(program_id, x_user_id=x_user_id)



Delete a specific program.

### Example

```python
import time
import os
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
> List[Program] api_programs_list(page=page, x_user_id=x_user_id, search=search, tags=tags, ordering=ordering)



Get a list of all programs for the authenticated user.

### Example

```python
import time
import os
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
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    search = 'search_example' # str | Search in name and description (optional)
    tags = 'tags_example' # str | Filter by tags (comma-separated) (optional)
    ordering = 'ordering_example' # str | Sort by field (prefix with '-' for descending) (optional)

    try:
        api_response = api_instance.api_programs_list(page=page, x_user_id=x_user_id, search=search, tags=tags, ordering=ordering)
        print("The response of ApiApi->api_programs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **search** | **str**| Search in name and description | [optional] 
 **tags** | **str**| Filter by tags (comma-separated) | [optional] 
 **ordering** | **str**| Sort by field (prefix with &#39;-&#39; for descending) | [optional] 

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

# **api_programs_partial_update**
> Program api_programs_partial_update(program_id, data, x_user_id=x_user_id)



Partially update a specific program.

### Example

```python
import time
import os
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

# **api_programs_picker_list**
> List[ProgramPicker] api_programs_picker_list()



### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.program_picker import ProgramPicker
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

    try:
        api_response = api_instance.api_programs_picker_list()
        print("The response of ApiApi->api_programs_picker_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_programs_picker_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ProgramPicker]**](ProgramPicker.md)

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

# **api_programs_read**
> Program api_programs_read(program_id, x_user_id=x_user_id)



Get details of a specific program.

### Example

```python
import time
import os
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

# **api_programs_update**
> Program api_programs_update(program_id, data, x_user_id=x_user_id)



Update a specific program.

### Example

```python
import time
import os
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
import time
import os
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
import time
import os
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
> List[Status] api_status_list(page=page, x_user_id=x_user_id, status=status, search=search, sort=sort, liimit=liimit, goal_ids=goal_ids)



Get a list of all statuses for the authenticated user.

### Example

```python
import time
import os
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
    status = 'status_example' # str | Filter by a status value (optional)
    search = 'search_example' # str | Search by keyword against status note or path to green (optional)
    sort = 'sort_example' # str | Sort by field (prefix with '-' for descending) (optional)
    liimit = 'liimit_example' # str | Sort by field (prefix with '-' for descending) (optional)
    goal_ids = 'goal_ids_example' # str | Filter on goals, using the UUID of the goal. (optional)

    try:
        api_response = api_instance.api_status_list(page=page, x_user_id=x_user_id, status=status, search=search, sort=sort, liimit=liimit, goal_ids=goal_ids)
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
 **status** | **str**| Filter by a status value | [optional] 
 **search** | **str**| Search by keyword against status note or path to green | [optional] 
 **sort** | **str**| Sort by field (prefix with &#39;-&#39; for descending) | [optional] 
 **liimit** | **str**| Sort by field (prefix with &#39;-&#39; for descending) | [optional] 
 **goal_ids** | **str**| Filter on goals, using the UUID of the goal. | [optional] 

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
import time
import os
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
import time
import os
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
import time
import os
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

# **api_tags_create**
> Tag api_tags_create(data, x_user_id=x_user_id)



Create a new tag for the authenticated user.

### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.tag import Tag
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
    data = pp_sdk.Tag() # Tag | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_tags_create(data, x_user_id=x_user_id)
        print("The response of ApiApi->api_tags_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_tags_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Tag**](Tag.md)

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

# **api_tags_delete**
> api_tags_delete(tag_id, x_user_id=x_user_id)



Delete a specific tag.

### Example

```python
import time
import os
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
    tag_id = 'tag_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.api_tags_delete(tag_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_tags_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 
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

# **api_tags_list**
> List[Tag] api_tags_list(page=page, x_user_id=x_user_id, search=search)



Get a list of all tags for the authenticated user.

### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.tag import Tag
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
    search = 'search_example' # str | Search tags by name (optional)

    try:
        api_response = api_instance.api_tags_list(page=page, x_user_id=x_user_id, search=search)
        print("The response of ApiApi->api_tags_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_tags_list: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tags_partial_update**
> Tag api_tags_partial_update(tag_id, data, x_user_id=x_user_id)



Partially update a specific tag.

### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.tag import Tag
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
    tag_id = 'tag_id_example' # str | 
    data = pp_sdk.Tag() # Tag | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_tags_partial_update(tag_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_tags_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_tags_partial_update: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tags_read**
> Tag api_tags_read(tag_id, x_user_id=x_user_id)



Get details of a specific tag.

### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.tag import Tag
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
    tag_id = 'tag_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_tags_read(tag_id, x_user_id=x_user_id)
        print("The response of ApiApi->api_tags_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_tags_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**|  | 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**Tag**](Tag.md)

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

# **api_tags_update**
> Tag api_tags_update(tag_id, data, x_user_id=x_user_id)



Update a specific tag.

### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.tag import Tag
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
    tag_id = 'tag_id_example' # str | 
    data = pp_sdk.Tag() # Tag | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_tags_update(tag_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_tags_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_tags_update: %s\n" % e)
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_user_create**
> User api_user_create(data, x_user_id=x_user_id)



Create a new user for the authenticated user's organization.

### Example

```python
import time
import os
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
    data = pp_sdk.User() # User | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_user_create(data, x_user_id=x_user_id)
        print("The response of ApiApi->api_user_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_create: %s\n" % e)
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

# **api_user_delete**
> api_user_delete(id)



### Example

```python
import time
import os
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

    try:
        api_instance.api_user_delete(id)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_delete: %s\n" % e)
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

# **api_user_list**
> User api_user_list(id, page=page)



Retrieve details of a specific user

### Example

```python
import time
import os
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
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.api_user_list(id, page=page)
        print("The response of ApiApi->api_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UUID of the user to retrieve | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

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

# **api_user_partial_update**
> User api_user_partial_update(id, data)



### Example

```python
import time
import os
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
    id = 'id_example' # str | 
    data = pp_sdk.User() # User | 

    try:
        api_response = api_instance.api_user_partial_update(id, data)
        print("The response of ApiApi->api_user_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_partial_update: %s\n" % e)
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

# **api_user_picker_list**
> List[User] api_user_picker_list(x_user_id=x_user_id, search=search, sort=sort, limit=limit)



Retrieve list of users matching none or all of search parameters.

### Example

```python
import time
import os
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
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    search = 'search_example' # str | Search term for filtering users by email, last name, or first name (optional)
    sort = 'sort_example' # str | Field to sort the results by (optional)
    limit = 56 # int | Maximum number of results to return (optional)

    try:
        api_response = api_instance.api_user_picker_list(x_user_id=x_user_id, search=search, sort=sort, limit=limit)
        print("The response of ApiApi->api_user_picker_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_picker_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
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

# **api_user_read**
> List[User] api_user_read(id, x_user_id=x_user_id)



Get a list of all PRDs for the authenticated user's organization.

### Example

```python
import time
import os
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
    id = 'id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_user_read(id, x_user_id=x_user_id)
        print("The response of ApiApi->api_user_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_read: %s\n" % e)
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

# **api_user_update**
> User api_user_update(id, data, x_user_id=x_user_id)



Update a specific user's details

### Example

```python
import time
import os
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
    id = 'id_example' # str | UUID of the user to update
    data = pp_sdk.User() # User | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_user_update(id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_user_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_user_update: %s\n" % e)
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

# **api_userstories_create**
> UserStory api_userstories_create(data)



Create a new user story.

### Example

```python
import time
import os
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

    try:
        api_response = api_instance.api_userstories_create(data)
        print("The response of ApiApi->api_userstories_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**UserStory**](UserStory.md)|  | 

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
> api_userstories_delete(userstory_id, x_user_id=x_user_id)



Delete a specific user story.

### Example

```python
import time
import os
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
    userstory_id = 'userstory_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_instance.api_userstories_delete(userstory_id, x_user_id=x_user_id)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userstory_id** | **str**|  | 
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
> List[UserStory] api_userstories_list(search=search, status=status, prd=prd, sort=sort, limit=limit, x_user_id=x_user_id, format=format)



List or Search for User Stories

### Example

```python
import time
import os
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
    search = 'search_example' # str | Search term for as_a, i_want_to, so_that, or freetext_override fields (optional)
    status = 'status_example' # str | Filter by status (optional)
    prd = 56 # int | Filter by PRD ID (optional)
    sort = 'sort_example' # str | Sort field (prefix with '-' for descending order) (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    format = 'format_example' # str | Response format (json or excel, default is json) (optional)

    try:
        api_response = api_instance.api_userstories_list(search=search, status=status, prd=prd, sort=sort, limit=limit, x_user_id=x_user_id, format=format)
        print("The response of ApiApi->api_userstories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term for as_a, i_want_to, so_that, or freetext_override fields | [optional] 
 **status** | **str**| Filter by status | [optional] 
 **prd** | **int**| Filter by PRD ID | [optional] 
 **sort** | **str**| Sort field (prefix with &#39;-&#39; for descending order) | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 
 **format** | **str**| Response format (json or excel, default is json) | [optional] 

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
> UserStory api_userstories_partial_update(userstory_id, data, x_user_id=x_user_id)



Partially update a specific user story.

### Example

```python
import time
import os
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
    userstory_id = 'userstory_id_example' # str | 
    data = pp_sdk.UserStory() # UserStory | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_partial_update(userstory_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userstory_id** | **str**|  | 
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
> UserStory api_userstories_read(userstory_id, x_user_id=x_user_id)



Get details of a specific user story.

### Example

```python
import time
import os
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
    userstory_id = 'userstory_id_example' # str | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_read(userstory_id, x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_read: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userstory_id** | **str**|  | 
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

# **api_userstories_update**
> UserStory api_userstories_update(userstory_id, data, x_user_id=x_user_id)



Update a specific user story.

### Example

```python
import time
import os
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
    userstory_id = 'userstory_id_example' # str | 
    data = pp_sdk.UserStory() # UserStory | 
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.api_userstories_update(userstory_id, data, x_user_id=x_user_id)
        print("The response of ApiApi->api_userstories_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiApi->api_userstories_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userstory_id** | **str**|  | 
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

