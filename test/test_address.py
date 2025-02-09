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

from pp_sdk.models.address import Address

class TestAddress(unittest.TestCase):
    """Address unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Address:
        """Test Address
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Address`
        """
        model = Address()
        if include_optional:
            return Address(
                street_address = '0',
                city = '0',
                state = '0',
                postal_code = '0',
                country = '0'
            )
        else:
            return Address(
                street_address = '0',
                city = '0',
                state = '0',
                postal_code = '0',
                country = '0',
        )
        """

    def testAddress(self):
        """Test Address"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
