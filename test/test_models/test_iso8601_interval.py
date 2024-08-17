
import unittest

from pynwsdata.models.iso8601_interval import ISO8601Interval

class TestISO8601Interval(unittest.TestCase):
    """ISO8601Interval unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ISO8601Interval:
        """Test ISO8601Interval
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ISO8601Interval`
        """
        model = ISO8601Interval()
        if include_optional:
            return ISO8601Interval(
            )
        else:
            return ISO8601Interval(
        )
        """

    def testISO8601Interval(self):
        """Test ISO8601Interval"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
