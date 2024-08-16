# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pynwsdata.models.text_product import TextProduct

class TestTextProduct(unittest.TestCase):
    """TextProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextProduct:
        """Test TextProduct
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextProduct`
        """
        model = TextProduct()
        if include_optional:
            return TextProduct(
                context = None,
                id = '',
                id = '',
                wmo_collective_id = '',
                issuing_office = '',
                issuance_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                product_code = '',
                product_name = '',
                product_text = ''
            )
        else:
            return TextProduct(
        )
        """

    def testTextProduct(self):
        """Test TextProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
