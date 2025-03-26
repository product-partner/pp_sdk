# pp_sdk
Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.5.2
- Generator version: 7.12.0
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
    except ApiException as e:
        print("Exception when calling GoogleDocsApi->google_docs_list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://0.0.0.0:8000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GoogleDocsApi* | [**google_docs_list**](docs/GoogleDocsApi.md#google_docs_list) | **GET** /google/docs/ | 
*GoogleDocsApi* | [**google_docs_read**](docs/GoogleDocsApi.md#google_docs_read) | **GET** /google/docs/{doc_id}/ | 
*GoogleDocsApi* | [**google_docs_webhook**](docs/GoogleDocsApi.md#google_docs_webhook) | **POST** /google/docs/webhook/{user_id}/ | 
*GoogleDocsApi* | [**register_google_doc**](docs/GoogleDocsApi.md#register_google_doc) | **POST** /google/docs/register/ | 
*GoogleDocsApi* | [**watch_google_doc**](docs/GoogleDocsApi.md#watch_google_doc) | **POST** /google/docs/{doc_id}/watch/ | 
*GoogleOAuthApi* | [**oauth_google_callback**](docs/GoogleOAuthApi.md#oauth_google_callback) | **GET** /oauth/google/callback/ | 
*GoogleOAuthApi* | [**oauth_google_start**](docs/GoogleOAuthApi.md#oauth_google_start) | **GET** /oauth/google/start | 
*GoogleOAuthApi* | [**toggle_google_sync**](docs/GoogleOAuthApi.md#toggle_google_sync) | **POST** /oauth/google/toggle-sync | 
*JiraApi* | [**jira_oauth_callback**](docs/JiraApi.md#jira_oauth_callback) | **GET** /jira/oauth/callback | 
*JiraApi* | [**jira_oauth_start**](docs/JiraApi.md#jira_oauth_start) | **GET** /jira/oauth/start | 
*JiraApi* | [**jira_oauth_toggle_sync**](docs/JiraApi.md#jira_oauth_toggle_sync) | **POST** /jira/oauth/toggle-sync | 
*JiraApi* | [**jira_sync_documents_create**](docs/JiraApi.md#jira_sync_documents_create) | **POST** /jira/sync/documents/{object_id}/ | 
*JiraApi* | [**jira_sync_documents_read**](docs/JiraApi.md#jira_sync_documents_read) | **GET** /jira/sync/documents/{object_id}/ | 
*JiraApi* | [**jira_sync_programs_create**](docs/JiraApi.md#jira_sync_programs_create) | **POST** /jira/sync/programs/{object_id}/ | 
*JiraApi* | [**jira_sync_programs_read**](docs/JiraApi.md#jira_sync_programs_read) | **GET** /jira/sync/programs/{object_id}/ | 
*JiraApi* | [**jira_sync_status_list**](docs/JiraApi.md#jira_sync_status_list) | **GET** /jira/sync/status/ | 
*JiraApi* | [**jira_sync_userstories_create**](docs/JiraApi.md#jira_sync_userstories_create) | **POST** /jira/sync/userstories/{object_id}/ | 
*JiraApi* | [**jira_sync_userstories_read**](docs/JiraApi.md#jira_sync_userstories_read) | **GET** /jira/sync/userstories/{object_id}/ | 
*JiraApi* | [**publish_doc_as_epic**](docs/JiraApi.md#publish_doc_as_epic) | **POST** /jira/documents/{doc_id}/publish | 
*ChatApi* | [**chat**](docs/ChatApi.md#chat) | **GET** /chat/ | 
*ChatApi* | [**chat_history**](docs/ChatApi.md#chat_history) | **GET** /chat/history/ | 
*ChatApi* | [**chat_threads_read**](docs/ChatApi.md#chat_threads_read) | **GET** /chat/threads/{thread_id}/ | 
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
 - [Chat200Response](docs/Chat200Response.md)
 - [ChatHistory200Response](docs/ChatHistory200Response.md)
 - [ChatThreadsRead200Response](docs/ChatThreadsRead200Response.md)
 - [ChatUploadFile200Response](docs/ChatUploadFile200Response.md)
 - [Document](docs/Document.md)
 - [DocumentField](docs/DocumentField.md)
 - [DocumentListFieldInner](docs/DocumentListFieldInner.md)
 - [DocumentPicker](docs/DocumentPicker.md)
 - [DocumentsCreateRequest](docs/DocumentsCreateRequest.md)
 - [Goal](docs/Goal.md)
 - [GoalBase](docs/GoalBase.md)
 - [GoalPicker](docs/GoalPicker.md)
 - [GoogleDocsWebhook200Response](docs/GoogleDocsWebhook200Response.md)
 - [JiraSyncDocumentsCreateRequest](docs/JiraSyncDocumentsCreateRequest.md)
 - [Organization](docs/Organization.md)
 - [Program](docs/Program.md)
 - [ProgramPicker](docs/ProgramPicker.md)
 - [ProgramsListInner](docs/ProgramsListInner.md)
 - [PublishDocAsEpicRequest](docs/PublishDocAsEpicRequest.md)
 - [RegisterGoogleDoc200Response](docs/RegisterGoogleDoc200Response.md)
 - [RegisterGoogleDocRequest](docs/RegisterGoogleDocRequest.md)
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
 - [WatchGoogleDoc200Response](docs/WatchGoogleDoc200Response.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header

<a id="UserIdAuth"></a>
### UserIdAuth

- **Type**: API key
- **API key parameter name**: X-User-ID
- **Location**: HTTP header


## Author

info@productpartner.ai


