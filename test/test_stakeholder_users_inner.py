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

from pp_sdk.models.stakeholder_users_inner import StakeholderUsersInner

class TestStakeholderUsersInner(unittest.TestCase):
    """StakeholderUsersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StakeholderUsersInner:
        """Test StakeholderUsersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StakeholderUsersInner`
        """
        model = StakeholderUsersInner()
        if include_optional:
            return StakeholderUsersInner(
                id = '',
                email = '',
                first_name = '',
                last_name = ''
            )
        else:
            return StakeholderUsersInner(
        )
        """

    def testStakeholderUsersInner(self):
        """Test StakeholderUsersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
