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

from pp_sdk.models.document import Document

class TestDocument(unittest.TestCase):
    """Document unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Document:
        """Test Document
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Document`
        """
        model = Document()
        if include_optional:
            return Document(
                id = '',
                type = 'PRD',
                title = '0',
                body = '0',
                created_by = pp_sdk.models.created_by.Created by(
                    id = '', 
                    email = '', 
                    first_name = '', 
                    last_name = '', ),
                created_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reviewed_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                document_covering_period_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                document_covering_period_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                publishing_state = 'PENDING_REVIEW',
                programs = [
                    pp_sdk.models.programs_inner.Programs_inner(
                        id = '', 
                        name = '', )
                    ],
                tags = [
                    pp_sdk.models.tags_inner.Tags_inner(
                        id = '', 
                        tag = '', )
                    ],
                stakeholder_users = [
                    pp_sdk.models.stakeholder_users_inner.Stakeholder_users_inner(
                        id = '', 
                        email = '', 
                        first_name = '', 
                        last_name = '', )
                    ],
                version = 56,
                version_summary = '',
                image_url = '',
                original_filename = '0',
                blob_id = '0'
            )
        else:
            return Document(
                title = '0',
        )
        """

    def testDocument(self):
        """Test Document"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
