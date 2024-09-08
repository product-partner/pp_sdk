# coding: utf-8

"""
    Product Partner API

    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

    The version of the OpenAPI document: v1
    Contact: chris@productpartner.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.organization import Organization
from openapi_client.models.program_base import ProgramBase
from openapi_client.models.tag import Tag
from openapi_client.models.user_base import UserBase
from typing import Optional, Set
from typing_extensions import Self

class PRDDetail(BaseModel):
    """
    PRDDetail
    """ # noqa: E501
    id: Optional[StrictStr] = None
    title: Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    programs: List[ProgramBase]
    description: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    created_date: Optional[datetime] = None
    modified_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    status: Optional[StrictStr] = None
    tags: Optional[List[Tag]] = None
    owner_user: Optional[UserBase] = None
    stakeholder_users: Optional[List[UserBase]] = None
    created_by: Optional[UserBase] = None
    organization: Optional[Organization] = None
    goals: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "title", "programs", "description", "body", "created_date", "modified_date", "due_date", "status", "tags", "owner_user", "stakeholder_users", "created_by", "organization", "goals"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DRAFT', 'IN_REVIEW', 'APPROVED', 'PUBLISHED']):
            raise ValueError("must be one of enum values ('DRAFT', 'IN_REVIEW', 'APPROVED', 'PUBLISHED')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PRDDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_date",
            "modified_date",
            "tags",
            "stakeholder_users",
            "goals",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in programs (list)
        _items = []
        if self.programs:
            for _item in self.programs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['programs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of owner_user
        if self.owner_user:
            _dict['owner_user'] = self.owner_user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in stakeholder_users (list)
        _items = []
        if self.stakeholder_users:
            for _item in self.stakeholder_users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stakeholder_users'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if body (nullable) is None
        # and model_fields_set contains the field
        if self.body is None and "body" in self.model_fields_set:
            _dict['body'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['due_date'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PRDDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "programs": [ProgramBase.from_dict(_item) for _item in obj["programs"]] if obj.get("programs") is not None else None,
            "description": obj.get("description"),
            "body": obj.get("body"),
            "created_date": obj.get("created_date"),
            "modified_date": obj.get("modified_date"),
            "due_date": obj.get("due_date"),
            "status": obj.get("status"),
            "tags": [Tag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "owner_user": UserBase.from_dict(obj["owner_user"]) if obj.get("owner_user") is not None else None,
            "stakeholder_users": [UserBase.from_dict(_item) for _item in obj["stakeholder_users"]] if obj.get("stakeholder_users") is not None else None,
            "created_by": UserBase.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "organization": Organization.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "goals": obj.get("goals")
        })
        return _obj


