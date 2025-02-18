# coding: utf-8

"""
    Product Partner API

    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

    The version of the OpenAPI document: v1
    Contact: info@productpartner.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pp_sdk.models.address import Address
from pp_sdk.models.organization import Organization
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    id: Optional[StrictStr] = None
    email: Annotated[str, Field(min_length=1, strict=True, max_length=254)]
    first_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    last_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    is_active: Optional[StrictBool] = None
    is_staff: Optional[StrictBool] = None
    date_joined: Optional[datetime] = None
    last_login: Optional[datetime] = None
    organization: Optional[Organization] = None
    address: Optional[Address] = None
    user_facts: Optional[Dict[str, Any]] = None
    walkthrough_status: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["id", "email", "first_name", "last_name", "is_active", "is_staff", "date_joined", "last_login", "organization", "address", "user_facts", "walkthrough_status"]

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
        """Create an instance of User from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "date_joined",
            "last_login",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "is_active": obj.get("is_active"),
            "is_staff": obj.get("is_staff"),
            "date_joined": obj.get("date_joined"),
            "last_login": obj.get("last_login"),
            "organization": Organization.from_dict(obj["organization"]) if obj.get("organization") is not None else None,
            "address": Address.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "user_facts": obj.get("user_facts"),
            "walkthrough_status": obj.get("walkthrough_status")
        })
        return _obj


