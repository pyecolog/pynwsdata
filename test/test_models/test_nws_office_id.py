
import unittest

from pynwsdata.models.nws_office_id import NWSOfficeId

class TestNWSOfficeId(unittest.TestCase):
    """NWSOfficeId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NWSOfficeId:
        """Test NWSOfficeId
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NWSOfficeId`
        """
        model = NWSOfficeId()
        if include_optional:
            return NWSOfficeId(
            )
        else:
            return NWSOfficeId(
        )
        """

    def testNWSOfficeId(self):
        """Test NWSOfficeId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
