# pp_sdk
Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.2.25
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pp_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pp_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    page = 56 # int | A page number within the paginated result set. (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)
    x_caller_id = 'x_caller_id_example' # str | Optional ID of the application calling the ID, used in conjunction with the caller_thread_id (optional)
    x_caller_thread_id = 'x_caller_thread_id_example' # str | Caller-side thread ID used in conjunction with the caller_id to identify the conversation that this message is a part of. This will be looked up against the internal thread id in Product Partner. (optional)
    msg = 'msg_example' # str | Chat message (optional)
    doc_ids = 'doc_ids_example' # str | Document IDs to reference. Content will be extracted and sent to the LLM along with your message. (optional)
    action = 'action_example' # str | Action (optional)
    stream = True # bool | Stream the response (optional)
    response_format = 'response_format_example' # str | Response format (html or text) (optional)

    try:
        api_response = api_instance.api_chat(page=page, x_user_id=x_user_id, x_caller_id=x_caller_id, x_caller_thread_id=x_caller_thread_id, msg=msg, doc_ids=doc_ids, action=action, stream=stream, response_format=response_format)
        print("The response of ApiApi->api_chat:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiApi->api_chat: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://0.0.0.0:8000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiApi* | [**api_chat**](docs/ApiApi.md#api_chat) | **GET** /api/chat/ | 
*ApiApi* | [**api_chat_history**](docs/ApiApi.md#api_chat_history) | **GET** /api/chat/history/ | 
*ApiApi* | [**api_chat_upload_file**](docs/ApiApi.md#api_chat_upload_file) | **POST** /api/chat/upload/ | 
*ApiApi* | [**api_goals_create**](docs/ApiApi.md#api_goals_create) | **POST** /api/goals/ | 
*ApiApi* | [**api_goals_delete**](docs/ApiApi.md#api_goals_delete) | **DELETE** /api/goals/{goal_id}/ | 
*ApiApi* | [**api_goals_list**](docs/ApiApi.md#api_goals_list) | **GET** /api/goals/ | 
*ApiApi* | [**api_goals_partial_update**](docs/ApiApi.md#api_goals_partial_update) | **PATCH** /api/goals/{goal_id}/ | 
*ApiApi* | [**api_goals_picker_list**](docs/ApiApi.md#api_goals_picker_list) | **GET** /api/goals/picker/ | 
*ApiApi* | [**api_goals_read**](docs/ApiApi.md#api_goals_read) | **GET** /api/goals/{goal_id}/ | 
*ApiApi* | [**api_goals_update**](docs/ApiApi.md#api_goals_update) | **PUT** /api/goals/{goal_id}/ | 
*ApiApi* | [**api_prds_create**](docs/ApiApi.md#api_prds_create) | **POST** /api/prds/ | 
*ApiApi* | [**api_prds_delete**](docs/ApiApi.md#api_prds_delete) | **DELETE** /api/prds/{prd_id}/ | 
*ApiApi* | [**api_prds_list**](docs/ApiApi.md#api_prds_list) | **GET** /api/prds/ | 
*ApiApi* | [**api_prds_partial_update**](docs/ApiApi.md#api_prds_partial_update) | **PATCH** /api/prds/{prd_id}/ | 
*ApiApi* | [**api_prds_read**](docs/ApiApi.md#api_prds_read) | **GET** /api/prds/{prd_id}/ | 
*ApiApi* | [**api_prds_update**](docs/ApiApi.md#api_prds_update) | **PUT** /api/prds/{prd_id}/ | 
*ApiApi* | [**api_programs_create**](docs/ApiApi.md#api_programs_create) | **POST** /api/programs/ | 
*ApiApi* | [**api_programs_delete**](docs/ApiApi.md#api_programs_delete) | **DELETE** /api/programs/{program_id}/ | 
*ApiApi* | [**api_programs_list**](docs/ApiApi.md#api_programs_list) | **GET** /api/programs/ | 
*ApiApi* | [**api_programs_partial_update**](docs/ApiApi.md#api_programs_partial_update) | **PATCH** /api/programs/{program_id}/ | 
*ApiApi* | [**api_programs_picker_list**](docs/ApiApi.md#api_programs_picker_list) | **GET** /api/programs/picker/ | 
*ApiApi* | [**api_programs_read**](docs/ApiApi.md#api_programs_read) | **GET** /api/programs/{program_id}/ | 
*ApiApi* | [**api_programs_update**](docs/ApiApi.md#api_programs_update) | **PUT** /api/programs/{program_id}/ | 
*ApiApi* | [**api_status_create**](docs/ApiApi.md#api_status_create) | **POST** /api/status/ | 
*ApiApi* | [**api_status_delete**](docs/ApiApi.md#api_status_delete) | **DELETE** /api/status/{status_id}/ | 
*ApiApi* | [**api_status_list**](docs/ApiApi.md#api_status_list) | **GET** /api/status/ | 
*ApiApi* | [**api_status_partial_update**](docs/ApiApi.md#api_status_partial_update) | **PATCH** /api/status/{status_id}/ | 
*ApiApi* | [**api_status_read**](docs/ApiApi.md#api_status_read) | **GET** /api/status/{status_id}/ | 
*ApiApi* | [**api_status_update**](docs/ApiApi.md#api_status_update) | **PUT** /api/status/{status_id}/ | 
*ApiApi* | [**api_tags_create**](docs/ApiApi.md#api_tags_create) | **POST** /api/tags/ | 
*ApiApi* | [**api_tags_delete**](docs/ApiApi.md#api_tags_delete) | **DELETE** /api/tags/{tag_id}/ | 
*ApiApi* | [**api_tags_list**](docs/ApiApi.md#api_tags_list) | **GET** /api/tags/ | 
*ApiApi* | [**api_tags_partial_update**](docs/ApiApi.md#api_tags_partial_update) | **PATCH** /api/tags/{tag_id}/ | 
*ApiApi* | [**api_tags_read**](docs/ApiApi.md#api_tags_read) | **GET** /api/tags/{tag_id}/ | 
*ApiApi* | [**api_tags_update**](docs/ApiApi.md#api_tags_update) | **PUT** /api/tags/{tag_id}/ | 
*ApiApi* | [**api_user_create**](docs/ApiApi.md#api_user_create) | **POST** /api/user/ | 
*ApiApi* | [**api_user_delete**](docs/ApiApi.md#api_user_delete) | **DELETE** /api/user/{id}/ | 
*ApiApi* | [**api_user_list**](docs/ApiApi.md#api_user_list) | **GET** /api/user/ | 
*ApiApi* | [**api_user_partial_update**](docs/ApiApi.md#api_user_partial_update) | **PATCH** /api/user/{id}/ | 
*ApiApi* | [**api_user_picker_list**](docs/ApiApi.md#api_user_picker_list) | **GET** /api/user/picker/ | 
*ApiApi* | [**api_user_read**](docs/ApiApi.md#api_user_read) | **GET** /api/user/{id}/ | 
*ApiApi* | [**api_user_update**](docs/ApiApi.md#api_user_update) | **PUT** /api/user/{id}/ | 
*ApiApi* | [**api_userstories_create**](docs/ApiApi.md#api_userstories_create) | **POST** /api/userstories/ | 
*ApiApi* | [**api_userstories_delete**](docs/ApiApi.md#api_userstories_delete) | **DELETE** /api/userstories/{userstory_id}/ | 
*ApiApi* | [**api_userstories_list**](docs/ApiApi.md#api_userstories_list) | **GET** /api/userstories/ | 
*ApiApi* | [**api_userstories_partial_update**](docs/ApiApi.md#api_userstories_partial_update) | **PATCH** /api/userstories/{userstory_id}/ | 
*ApiApi* | [**api_userstories_read**](docs/ApiApi.md#api_userstories_read) | **GET** /api/userstories/{userstory_id}/ | 
*ApiApi* | [**api_userstories_update**](docs/ApiApi.md#api_userstories_update) | **PUT** /api/userstories/{userstory_id}/ | 
*PrdApi* | [**prd_template_create**](docs/PrdApi.md#prd_template_create) | **POST** /prd/template/ | 
*PrdApi* | [**prd_template_delete**](docs/PrdApi.md#prd_template_delete) | **DELETE** /prd/template/{prdtemplate_id}/ | 
*PrdApi* | [**prd_template_list**](docs/PrdApi.md#prd_template_list) | **GET** /prd/template/ | 
*PrdApi* | [**prd_template_partial_update**](docs/PrdApi.md#prd_template_partial_update) | **PATCH** /prd/template/{prdtemplate_id}/ | 
*PrdApi* | [**prd_template_read**](docs/PrdApi.md#prd_template_read) | **GET** /prd/template/{prdtemplate_id}/ | 
*PrdApi* | [**prd_template_update**](docs/PrdApi.md#prd_template_update) | **PUT** /prd/template/{prdtemplate_id}/ | 


## Documentation For Models

 - [Address](docs/Address.md)
 - [ApiChat200Response](docs/ApiChat200Response.md)
 - [ApiChatUploadFile200Response](docs/ApiChatUploadFile200Response.md)
 - [ApiPrdsCreateRequest](docs/ApiPrdsCreateRequest.md)
 - [ApiPrdsPartialUpdateRequest](docs/ApiPrdsPartialUpdateRequest.md)
 - [ApiStatusCreateRequest](docs/ApiStatusCreateRequest.md)
 - [ApiUserstoriesCreateRequest](docs/ApiUserstoriesCreateRequest.md)
 - [CreatedBy](docs/CreatedBy.md)
 - [Goal](docs/Goal.md)
 - [GoalBase](docs/GoalBase.md)
 - [GoalPicker](docs/GoalPicker.md)
 - [Organization](docs/Organization.md)
 - [OwnerUsersInner](docs/OwnerUsersInner.md)
 - [PRD](docs/PRD.md)
 - [PRDReference](docs/PRDReference.md)
 - [PRDTemplate](docs/PRDTemplate.md)
 - [Program](docs/Program.md)
 - [ProgramPicker](docs/ProgramPicker.md)
 - [ProgramsInner](docs/ProgramsInner.md)
 - [Status](docs/Status.md)
 - [Status1](docs/Status1.md)
 - [Tag](docs/Tag.md)
 - [TagsInner](docs/TagsInner.md)
 - [User](docs/User.md)
 - [UserStory](docs/UserStory.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

chris@productpartner.ai


