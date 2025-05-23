# coding: utf-8

"""
    Product Partner API

    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

    The version of the OpenAPI document: v1
    Contact: info@productpartner.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pp_sdk.models.goal import Goal

class TestGoal(unittest.TestCase):
    """Goal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Goal:
        """Test Goal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Goal`
        """
        model = Goal()
        if include_optional:
            return Goal(
                id = '',
                name = '0',
                goal_language = '',
                description = '',
                why_it_matters = '',
                prd = [doc_id1, doc_id2],
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                original_due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                current_due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                owner_users = [user_id1, user_id2],
                programs = [program_id1, program_id2],
                stakeholder_users = [user_id1, user_id2],
                tags = [
                    pp_sdk.models.tags_inner.Tags_inner(
                        id = '', 
                        tag = '', )
                    ],
                version = -2147483648,
                version_summary = '',
                created_by = pp_sdk.models.user_field.User Field(
                    id = '', 
                    email = '', 
                    first_name = '', 
                    last_name = '', ),
                status = pp_sdk.models.status.Status(
                    id = '', 
                    status = '', 
                    status_display = '', 
                    date = '', )
            )
        else:
            return Goal(
                name = '0',
        )
        """

    def testGoal(self):
        """Test Goal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
