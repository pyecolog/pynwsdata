
import unittest

from pynwsdata.models.alert_atom_feed_author import AlertAtomFeedAuthor

class TestAlertAtomFeedAuthor(unittest.TestCase):
    """AlertAtomFeedAuthor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertAtomFeedAuthor:
        """Test AlertAtomFeedAuthor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertAtomFeedAuthor`
        """
        model = AlertAtomFeedAuthor()
        if include_optional:
            return AlertAtomFeedAuthor(
                name = ''
            )
        else:
            return AlertAtomFeedAuthor(
        )
        """

    def testAlertAtomFeedAuthor(self):
        """Test AlertAtomFeedAuthor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
