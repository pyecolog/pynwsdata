
import unittest

from pynwsdata.models.alert_xml_parameter import AlertXMLParameter

class TestAlertXMLParameter(unittest.TestCase):
    """AlertXMLParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertXMLParameter:
        """Test AlertXMLParameter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertXMLParameter`
        """
        model = AlertXMLParameter()
        if include_optional:
            return AlertXMLParameter(
                value_name = '',
                value = ''
            )
        else:
            return AlertXMLParameter(
        )
        """

    def testAlertXMLParameter(self):
        """Test AlertXMLParameter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
