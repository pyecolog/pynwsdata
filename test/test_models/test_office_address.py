
import unittest

from pynwsdata.models.office_address import OfficeAddress

class TestOfficeAddress(unittest.TestCase):
    """OfficeAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OfficeAddress:
        """Test OfficeAddress
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfficeAddress`
        """
        model = OfficeAddress()
        if include_optional:
            return OfficeAddress(
                type = 'PostalAddress',
                street_address = '',
                address_locality = '',
                address_region = '',
                postal_code = ''
            )
        else:
            return OfficeAddress(
        )
        """

    def testOfficeAddress(self):
        """Test OfficeAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
