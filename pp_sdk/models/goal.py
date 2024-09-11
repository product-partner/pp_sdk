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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conint, conlist, constr
from pp_sdk.models.prd import PRD
from pp_sdk.models.program import Program
from pp_sdk.models.tag import Tag
from pp_sdk.models.user import User

class Goal(BaseModel):
    """
    Goal
    """
    id: Optional[StrictStr] = None
    name: constr(strict=True, max_length=255, min_length=1) = Field(...)
    goal_language: constr(strict=True, min_length=1) = Field(...)
    description: Optional[StrictStr] = None
    why_it_matters: Optional[StrictStr] = None
    created_date: Optional[datetime] = None
    modified_date: Optional[datetime] = None
    original_due_date: Optional[datetime] = None
    current_due_date: Optional[datetime] = None
    prd: Optional[conlist(PRD)] = None
    owner_users: Optional[constr(strict=True, max_length=255)] = None
    program: Optional[constr(strict=True, max_length=255)] = None
    program_dependent_goals: Optional[conlist(Program)] = None
    stakeholders_users: Optional[conlist(User)] = None
    tags: Optional[conlist(Tag)] = None
    version: Optional[conint(strict=True, le=2147483647, ge=-2147483648)] = None
    version_summary: Optional[StrictStr] = None
    created_by: Optional[User] = None
    organization: Optional[StrictStr] = None
    __properties = ["id", "name", "goal_language", "description", "why_it_matters", "created_date", "modified_date", "original_due_date", "current_due_date", "prd", "owner_users", "program", "program_dependent_goals", "stakeholders_users", "tags", "version", "version_summary", "created_by", "organization"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Goal:
        """Create an instance of Goal from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_date",
                            "modified_date",
                            "prd",
                            "program_dependent_goals",
                            "stakeholders_users",
                            "tags",
                            "organization",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in prd (list)
        _items = []
        if self.prd:
            for _item in self.prd:
                if _item:
                    _items.append(_item.to_dict())
            _dict['prd'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in program_dependent_goals (list)
        _items = []
        if self.program_dependent_goals:
            for _item in self.program_dependent_goals:
                if _item:
                    _items.append(_item.to_dict())
            _dict['program_dependent_goals'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in stakeholders_users (list)
        _items = []
        if self.stakeholders_users:
            for _item in self.stakeholders_users:
                if _item:
                    _items.append(_item.to_dict())
            _dict['stakeholders_users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if why_it_matters (nullable) is None
        # and __fields_set__ contains the field
        if self.why_it_matters is None and "why_it_matters" in self.__fields_set__:
            _dict['why_it_matters'] = None

        # set to None if created_date (nullable) is None
        # and __fields_set__ contains the field
        if self.created_date is None and "created_date" in self.__fields_set__:
            _dict['created_date'] = None

        # set to None if modified_date (nullable) is None
        # and __fields_set__ contains the field
        if self.modified_date is None and "modified_date" in self.__fields_set__:
            _dict['modified_date'] = None

        # set to None if original_due_date (nullable) is None
        # and __fields_set__ contains the field
        if self.original_due_date is None and "original_due_date" in self.__fields_set__:
            _dict['original_due_date'] = None

        # set to None if current_due_date (nullable) is None
        # and __fields_set__ contains the field
        if self.current_due_date is None and "current_due_date" in self.__fields_set__:
            _dict['current_due_date'] = None

        # set to None if owner_users (nullable) is None
        # and __fields_set__ contains the field
        if self.owner_users is None and "owner_users" in self.__fields_set__:
            _dict['owner_users'] = None

        # set to None if program (nullable) is None
        # and __fields_set__ contains the field
        if self.program is None and "program" in self.__fields_set__:
            _dict['program'] = None

        # set to None if version (nullable) is None
        # and __fields_set__ contains the field
        if self.version is None and "version" in self.__fields_set__:
            _dict['version'] = None

        # set to None if organization (nullable) is None
        # and __fields_set__ contains the field
        if self.organization is None and "organization" in self.__fields_set__:
            _dict['organization'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Goal:
        """Create an instance of Goal from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Goal.parse_obj(obj)

        _obj = Goal.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "goal_language": obj.get("goal_language"),
            "description": obj.get("description"),
            "why_it_matters": obj.get("why_it_matters"),
            "created_date": obj.get("created_date"),
            "modified_date": obj.get("modified_date"),
            "original_due_date": obj.get("original_due_date"),
            "current_due_date": obj.get("current_due_date"),
            "prd": [PRD.from_dict(_item) for _item in obj.get("prd")] if obj.get("prd") is not None else None,
            "owner_users": obj.get("owner_users"),
            "program": obj.get("program"),
            "program_dependent_goals": [Program.from_dict(_item) for _item in obj.get("program_dependent_goals")] if obj.get("program_dependent_goals") is not None else None,
            "stakeholders_users": [User.from_dict(_item) for _item in obj.get("stakeholders_users")] if obj.get("stakeholders_users") is not None else None,
            "tags": [Tag.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "version": obj.get("version"),
            "version_summary": obj.get("version_summary"),
            "created_by": User.from_dict(obj.get("created_by")) if obj.get("created_by") is not None else None,
            "organization": obj.get("organization")
        })
        return _obj


