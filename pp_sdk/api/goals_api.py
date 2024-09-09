# coding: utf-8

"""
    Product Partner API

    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

    The version of the OpenAPI document: v1
    Contact: chris@productpartner.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from pp_sdk.models.goal import Goal

from pp_sdk.api_client import ApiClient, RequestSerialized
from pp_sdk.api_response import ApiResponse
from pp_sdk.rest import RESTResponseType


class GoalsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def goals_list_list(
        self,
        stakeholders_users: Annotated[Optional[StrictStr], Field(description="Comma-separated list of stakeholder IDs")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter by status")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search term for goal name, language, or description")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort field (prefix with '-' for descending order)")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Limit the number of results")] = None,
        x_user_id: Annotated[Optional[StrictStr], Field(description="User ID (required when using API key)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[Goal]:
        """goals_list_list

        Search for PRDs

        :param stakeholders_users: Comma-separated list of stakeholder IDs
        :type stakeholders_users: str
        :param status: Filter by status
        :type status: str
        :param search: Search term for goal name, language, or description
        :type search: str
        :param sort: Sort field (prefix with '-' for descending order)
        :type sort: str
        :param limit: Limit the number of results
        :type limit: int
        :param x_user_id: User ID (required when using API key)
        :type x_user_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._goals_list_list_serialize(
            stakeholders_users=stakeholders_users,
            status=status,
            search=search,
            sort=sort,
            limit=limit,
            x_user_id=x_user_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Goal]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def goals_list_list_with_http_info(
        self,
        stakeholders_users: Annotated[Optional[StrictStr], Field(description="Comma-separated list of stakeholder IDs")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter by status")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search term for goal name, language, or description")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort field (prefix with '-' for descending order)")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Limit the number of results")] = None,
        x_user_id: Annotated[Optional[StrictStr], Field(description="User ID (required when using API key)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[Goal]]:
        """goals_list_list

        Search for PRDs

        :param stakeholders_users: Comma-separated list of stakeholder IDs
        :type stakeholders_users: str
        :param status: Filter by status
        :type status: str
        :param search: Search term for goal name, language, or description
        :type search: str
        :param sort: Sort field (prefix with '-' for descending order)
        :type sort: str
        :param limit: Limit the number of results
        :type limit: int
        :param x_user_id: User ID (required when using API key)
        :type x_user_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._goals_list_list_serialize(
            stakeholders_users=stakeholders_users,
            status=status,
            search=search,
            sort=sort,
            limit=limit,
            x_user_id=x_user_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Goal]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def goals_list_list_without_preload_content(
        self,
        stakeholders_users: Annotated[Optional[StrictStr], Field(description="Comma-separated list of stakeholder IDs")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter by status")] = None,
        search: Annotated[Optional[StrictStr], Field(description="Search term for goal name, language, or description")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Sort field (prefix with '-' for descending order)")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Limit the number of results")] = None,
        x_user_id: Annotated[Optional[StrictStr], Field(description="User ID (required when using API key)")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """goals_list_list

        Search for PRDs

        :param stakeholders_users: Comma-separated list of stakeholder IDs
        :type stakeholders_users: str
        :param status: Filter by status
        :type status: str
        :param search: Search term for goal name, language, or description
        :type search: str
        :param sort: Sort field (prefix with '-' for descending order)
        :type sort: str
        :param limit: Limit the number of results
        :type limit: int
        :param x_user_id: User ID (required when using API key)
        :type x_user_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._goals_list_list_serialize(
            stakeholders_users=stakeholders_users,
            status=status,
            search=search,
            sort=sort,
            limit=limit,
            x_user_id=x_user_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[Goal]",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _goals_list_list_serialize(
        self,
        stakeholders_users,
        status,
        search,
        sort,
        limit,
        x_user_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if stakeholders_users is not None:
            
            _query_params.append(('stakeholders_users', stakeholders_users))
            
        if status is not None:
            
            _query_params.append(('status', status))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        # process the header parameters
        if x_user_id is not None:
            _header_params['X-User-ID'] = x_user_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/goals/list/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


