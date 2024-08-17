
import unittest

from pynwsdata.models.area_code import AreaCode

class TestAreaCode(unittest.TestCase):
    """AreaCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AreaCode:
        """Test AreaCode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AreaCode`
        """
        model = AreaCode()
        if include_optional:
            return AreaCode(
            )
        else:
            return AreaCode(
        )
        """

    def testAreaCode(self):
        """Test AreaCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
