
import unittest

from pynwsdata.models.region_code import RegionCode

class TestRegionCode(unittest.TestCase):
    """RegionCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RegionCode:
        """Test RegionCode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegionCode`
        """
        model = RegionCode()
        if include_optional:
            return RegionCode(
            )
        else:
            return RegionCode(
        )
        """

    def testRegionCode(self):
        """Test RegionCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
