
import unittest

from pynwsdata.models.alert_atom_feed import AlertAtomFeed

class TestAlertAtomFeed(unittest.TestCase):
    """AlertAtomFeed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertAtomFeed:
        """Test AlertAtomFeed
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertAtomFeed`
        """
        model = AlertAtomFeed()
        if include_optional:
            return AlertAtomFeed(
                id = '',
                generator = '',
                updated = '',
                author = pynwsdata.models.alert_atom_feed_author.AlertAtomFeed_author(
                    name = '', ),
                title = '',
                entry = [
                    pynwsdata.models.alert_atom_entry.AlertAtomEntry(
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
                            ], )
                    ]
            )
        else:
            return AlertAtomFeed(
        )
        """

    def testAlertAtomFeed(self):
        """Test AlertAtomFeed"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
