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

from pp_sdk.models.commit import Commit

class TestCommit(unittest.TestCase):
    """Commit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Commit:
        """Test Commit
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Commit`
        """
        model = Commit()
        if include_optional:
            return Commit(
                id = '',
                user = pp_sdk.models.user_field.User Field(
                    id = '', 
                    email = '', 
                    first_name = '', 
                    last_name = '', ),
                commit_hash = '0',
                repo = '',
                user_lines_changed = -2147483648,
                ai_lines_changed = -2147483648,
                user_lines_list = pp_sdk.models.user_lines_list.User lines list(),
                ai_lines_list = pp_sdk.models.ai_lines_list.Ai lines list(),
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Commit(
                commit_hash = '0',
                repo = '',
        )
        """

    def testCommit(self):
        """Test Commit"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
