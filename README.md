# pp_sdk
Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.4.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

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
    except ApiException as e:
        print("Exception when calling ChatApi->chat: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://0.0.0.0:8000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChatApi* | [**chat**](docs/ChatApi.md#chat) | **GET** /chat/ | 
*ChatApi* | [**chat_history**](docs/ChatApi.md#chat_history) | **GET** /chat/history/ | 
*ChatApi* | [**chat_upload_file**](docs/ChatApi.md#chat_upload_file) | **POST** /chat/upload/ | 
*DocumentsApi* | [**documents_create**](docs/DocumentsApi.md#documents_create) | **POST** /documents/ | 
*DocumentsApi* | [**documents_delete**](docs/DocumentsApi.md#documents_delete) | **DELETE** /documents/{id}/ | 
*DocumentsApi* | [**documents_image_list**](docs/DocumentsApi.md#documents_image_list) | **GET** /documents/{id}/image/ | 
*DocumentsApi* | [**documents_list**](docs/DocumentsApi.md#documents_list) | **GET** /documents/ | 
*DocumentsApi* | [**documents_partial_update**](docs/DocumentsApi.md#documents_partial_update) | **PATCH** /documents/{id}/ | 
*DocumentsApi* | [**documents_picker_list**](docs/DocumentsApi.md#documents_picker_list) | **GET** /documents/picker/ | 
*DocumentsApi* | [**documents_read**](docs/DocumentsApi.md#documents_read) | **GET** /documents/{id}/ | 
*DocumentsApi* | [**documents_update**](docs/DocumentsApi.md#documents_update) | **PUT** /documents/{id}/ | 
*GoalsApi* | [**goals_create**](docs/GoalsApi.md#goals_create) | **POST** /goals/ | 
*GoalsApi* | [**goals_delete**](docs/GoalsApi.md#goals_delete) | **DELETE** /goals/{goal_id}/ | 
*GoalsApi* | [**goals_list**](docs/GoalsApi.md#goals_list) | **GET** /goals/ | 
*GoalsApi* | [**goals_partial_update**](docs/GoalsApi.md#goals_partial_update) | **PATCH** /goals/{goal_id}/ | 
*GoalsApi* | [**goals_picker_list**](docs/GoalsApi.md#goals_picker_list) | **GET** /goals/picker/ | 
*GoalsApi* | [**goals_read**](docs/GoalsApi.md#goals_read) | **GET** /goals/{goal_id}/ | 
*GoalsApi* | [**goals_update**](docs/GoalsApi.md#goals_update) | **PUT** /goals/{goal_id}/ | 
*ProgramsApi* | [**programs_create**](docs/ProgramsApi.md#programs_create) | **POST** /programs/ | 
*ProgramsApi* | [**programs_delete**](docs/ProgramsApi.md#programs_delete) | **DELETE** /programs/{program_id}/ | 
*ProgramsApi* | [**programs_list**](docs/ProgramsApi.md#programs_list) | **GET** /programs/ | 
*ProgramsApi* | [**programs_partial_update**](docs/ProgramsApi.md#programs_partial_update) | **PATCH** /programs/{program_id}/ | 
*ProgramsApi* | [**programs_picker_list**](docs/ProgramsApi.md#programs_picker_list) | **GET** /programs/picker/ | 
*ProgramsApi* | [**programs_read**](docs/ProgramsApi.md#programs_read) | **GET** /programs/{program_id}/ | 
*ProgramsApi* | [**programs_update**](docs/ProgramsApi.md#programs_update) | **PUT** /programs/{program_id}/ | 
*StatusApi* | [**status_create**](docs/StatusApi.md#status_create) | **POST** /status/ | 
*StatusApi* | [**status_delete**](docs/StatusApi.md#status_delete) | **DELETE** /status/{status_id}/ | 
*StatusApi* | [**status_list**](docs/StatusApi.md#status_list) | **GET** /status/ | 
*StatusApi* | [**status_partial_update**](docs/StatusApi.md#status_partial_update) | **PATCH** /status/{status_id}/ | 
*StatusApi* | [**status_read**](docs/StatusApi.md#status_read) | **GET** /status/{status_id}/ | 
*StatusApi* | [**status_update**](docs/StatusApi.md#status_update) | **PUT** /status/{status_id}/ | 
*TagsApi* | [**tags_create**](docs/TagsApi.md#tags_create) | **POST** /tags/ | 
*TagsApi* | [**tags_delete**](docs/TagsApi.md#tags_delete) | **DELETE** /tags/{tag_id}/ | 
*TagsApi* | [**tags_list**](docs/TagsApi.md#tags_list) | **GET** /tags/ | 
*TagsApi* | [**tags_partial_update**](docs/TagsApi.md#tags_partial_update) | **PATCH** /tags/{tag_id}/ | 
*TagsApi* | [**tags_read**](docs/TagsApi.md#tags_read) | **GET** /tags/{tag_id}/ | 
*TagsApi* | [**tags_update**](docs/TagsApi.md#tags_update) | **PUT** /tags/{tag_id}/ | 
*UsersApi* | [**users_create**](docs/UsersApi.md#users_create) | **POST** /users/ | 
*UsersApi* | [**users_delete**](docs/UsersApi.md#users_delete) | **DELETE** /users/{id}/ | 
*UsersApi* | [**users_list**](docs/UsersApi.md#users_list) | **GET** /users/ | 
*UsersApi* | [**users_partial_update**](docs/UsersApi.md#users_partial_update) | **PATCH** /users/{id}/ | 
*UsersApi* | [**users_picker_list**](docs/UsersApi.md#users_picker_list) | **GET** /users/picker/ | 
*UsersApi* | [**users_read**](docs/UsersApi.md#users_read) | **GET** /users/{id}/ | 
*UsersApi* | [**users_update**](docs/UsersApi.md#users_update) | **PUT** /users/{id}/ | 
*UserstoriesApi* | [**userstories_create**](docs/UserstoriesApi.md#userstories_create) | **POST** /userstories/ | 
*UserstoriesApi* | [**userstories_delete**](docs/UserstoriesApi.md#userstories_delete) | **DELETE** /userstories/{userstory_id}/ | 
*UserstoriesApi* | [**userstories_list**](docs/UserstoriesApi.md#userstories_list) | **GET** /userstories/ | 
*UserstoriesApi* | [**userstories_partial_update**](docs/UserstoriesApi.md#userstories_partial_update) | **PATCH** /userstories/{userstory_id}/ | 
*UserstoriesApi* | [**userstories_read**](docs/UserstoriesApi.md#userstories_read) | **GET** /userstories/{userstory_id}/ | 
*UserstoriesApi* | [**userstories_update**](docs/UserstoriesApi.md#userstories_update) | **PUT** /userstories/{userstory_id}/ | 


## Documentation For Models

 - [Address](docs/Address.md)
 - [ChatHistory200Response](docs/ChatHistory200Response.md)
 - [ChatUploadFile200Response](docs/ChatUploadFile200Response.md)
 - [Document](docs/Document.md)
 - [DocumentListFieldInner](docs/DocumentListFieldInner.md)
 - [DocumentPicker](docs/DocumentPicker.md)
 - [DocumentsCreateRequest](docs/DocumentsCreateRequest.md)
 - [Goal](docs/Goal.md)
 - [GoalBase](docs/GoalBase.md)
 - [GoalPicker](docs/GoalPicker.md)
 - [Organization](docs/Organization.md)
 - [Program](docs/Program.md)
 - [ProgramPicker](docs/ProgramPicker.md)
 - [ProgramsListInner](docs/ProgramsListInner.md)
 - [Status](docs/Status.md)
 - [Status1](docs/Status1.md)
 - [StatusCreateRequest](docs/StatusCreateRequest.md)
 - [Tag](docs/Tag.md)
 - [TagsInner](docs/TagsInner.md)
 - [User](docs/User.md)
 - [UserField](docs/UserField.md)
 - [UserListOfUserFieldsInner](docs/UserListOfUserFieldsInner.md)
 - [UserStory](docs/UserStory.md)
 - [UserstoriesCreateRequest](docs/UserstoriesCreateRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

chris@productpartner.ai


