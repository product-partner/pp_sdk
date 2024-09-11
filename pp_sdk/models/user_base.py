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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr

class UserBase(BaseModel):
    """
    UserBase
    """
    id: Optional[StrictStr] = None
    email: constr(strict=True, max_length=254, min_length=1) = Field(...)
    first_name: Optional[constr(strict=True, max_length=255)] = None
    last_name: Optional[constr(strict=True, max_length=255)] = None
    __properties = ["id", "email", "first_name", "last_name"]

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
    def from_json(cls, json_str: str) -> UserBase:
        """Create an instance of UserBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserBase:
        """Create an instance of UserBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserBase.parse_obj(obj)

        _obj = UserBase.parse_obj({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name")
        })
        return _obj


