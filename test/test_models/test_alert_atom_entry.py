
import unittest

from pynwsdata.models.alert_atom_entry import AlertAtomEntry

class TestAlertAtomEntry(unittest.TestCase):
    """AlertAtomEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertAtomEntry:
        """Test AlertAtomEntry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertAtomEntry`
        """
        model = AlertAtomEntry()
        if include_optional:
            return AlertAtomEntry(
                id = '',
                updated = '',
                published = '',
                author = pynwsdata.models.alert_atom_entry_author.AlertAtomEntry_author(
                    name = '', ),
                summary = '',
                event = '',
                sent = '',
                effective = '',
                expires = '',
                status = '',
                msg_type = '',
                category = '',
                urgency = '',
                severity = '',
                certainty = '',
                area_desc = '',
                polygon = '',
                geocode = [
                    pynwsdata.models.alert_xml_parameter.AlertXMLParameter(
                        value_name = '', 
                        value = '', )
                    ],
                parameter = [
                    pynwsdata.models.alert_xml_parameter.AlertXMLParameter(
                        value_name = '', 
                        value = '', )
                    ]
            )
        else:
            return AlertAtomEntry(
        )
        """

    def testAlertAtomEntry(self):
        """Test AlertAtomEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
