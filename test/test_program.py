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

from pp_sdk.models.program import Program

class TestProgram(unittest.TestCase):
    """Program unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Program:
        """Test Program
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Program`
        """
        model = Program()
        if include_optional:
            return Program(
                id = '',
                name = '0',
                description = '',
                mission = '',
                charter = '',
                principal_users = [user_id1, user_id2],
                stakeholder_users = [user_id1, user_id2],
                parent = '',
                tags = [
                    pp_sdk.models.tags_inner.Tags_inner(
                        id = '', 
                        tag = '', )
                    ],
                created_by = pp_sdk.models.user_field.User Field(
                    id = '', 
                    email = '', 
                    first_name = '', 
                    last_name = '', ),
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Program(
                name = '0',
        )
        """

    def testProgram(self):
        """Test Program"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
