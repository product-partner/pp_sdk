# coding: utf-8

"""
    Product Partner API

    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

    The version of the OpenAPI document: v1
    Contact: chris@productpartner.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.user_create import UserCreate

class TestUserCreate(unittest.TestCase):
    """UserCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserCreate:
        """Test UserCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCreate`
        """
        model = UserCreate()
        if include_optional:
            return UserCreate(
                email = '0',
                first_name = '',
                last_name = '',
                password = '0'
            )
        else:
            return UserCreate(
                email = '0',
                password = '0',
        )
        """

    def testUserCreate(self):
        """Test UserCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
