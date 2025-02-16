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

from pp_sdk.models.userstories_create_request import UserstoriesCreateRequest

class TestUserstoriesCreateRequest(unittest.TestCase):
    """UserstoriesCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserstoriesCreateRequest:
        """Test UserstoriesCreateRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserstoriesCreateRequest`
        """
        model = UserstoriesCreateRequest()
        if include_optional:
            return UserstoriesCreateRequest(
                prd = '',
                as_a = '',
                i_want_to = '',
                so_that = '',
                freetext_override = '',
                acceptance_criteria = '',
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'RED',
                priority = '',
                tags = [
                    ''
                    ]
            )
        else:
            return UserstoriesCreateRequest(
                prd = '',
        )
        """

    def testUserstoriesCreateRequest(self):
        """Test UserstoriesCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
