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

from pp_sdk.models.chat_history200_response import ChatHistory200Response

class TestChatHistory200Response(unittest.TestCase):
    """ChatHistory200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChatHistory200Response:
        """Test ChatHistory200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChatHistory200Response`
        """
        model = ChatHistory200Response()
        if include_optional:
            return ChatHistory200Response(
                chat_history = [
                    None
                    ],
                has_next = True,
                has_previous = True,
                first_date = '',
                last_date = '',
                sort_order = '',
                start_index = 56,
                page = 56,
                items_per_page = 56
            )
        else:
            return ChatHistory200Response(
        )
        """

    def testChatHistory200Response(self):
        """Test ChatHistory200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
