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
from pydantic import BaseModel, StrictStr, constr

class GoalPicker(BaseModel):
    """
    GoalPicker
    """
    id: Optional[StrictStr] = None
    name: Optional[constr(strict=True, min_length=1)] = None
    goal_language: Optional[constr(strict=True, min_length=1)] = None
    __properties = ["id", "name", "goal_language"]

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
    def from_json(cls, json_str: str) -> GoalPicker:
        """Create an instance of GoalPicker from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "name",
                            "goal_language",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GoalPicker:
        """Create an instance of GoalPicker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GoalPicker.parse_obj(obj)

        _obj = GoalPicker.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "goal_language": obj.get("goal_language")
        })
        return _obj


