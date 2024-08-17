
import unittest

from pynwsdata.models.zone_state import ZoneState

class TestZoneState(unittest.TestCase):
    """ZoneState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ZoneState:
        """Test ZoneState
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ZoneState`
        """
        model = ZoneState()
        if include_optional:
            return ZoneState(
            )
        else:
            return ZoneState(
        )
        """

    def testZoneState(self):
        """Test ZoneState"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
