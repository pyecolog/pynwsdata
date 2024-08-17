
import unittest

from pynwsdata.models.alerts_types200_response import AlertsTypes200Response

class TestAlertsTypes200Response(unittest.TestCase):
    """AlertsTypes200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertsTypes200Response:
        """Test AlertsTypes200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertsTypes200Response`
        """
        model = AlertsTypes200Response()
        if include_optional:
            return AlertsTypes200Response(
                event_types = [
                    ''
                    ]
            )
        else:
            return AlertsTypes200Response(
        )
        """

    def testAlertsTypes200Response(self):
        """Test AlertsTypes200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
