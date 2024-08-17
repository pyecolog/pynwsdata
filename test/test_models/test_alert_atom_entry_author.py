
import unittest

from pynwsdata.models.alert_atom_entry_author import AlertAtomEntryAuthor

class TestAlertAtomEntryAuthor(unittest.TestCase):
    """AlertAtomEntryAuthor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertAtomEntryAuthor:
        """Test AlertAtomEntryAuthor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertAtomEntryAuthor`
        """
        model = AlertAtomEntryAuthor()
        if include_optional:
            return AlertAtomEntryAuthor(
                name = ''
            )
        else:
            return AlertAtomEntryAuthor(
        )
        """

    def testAlertAtomEntryAuthor(self):
        """Test AlertAtomEntryAuthor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
