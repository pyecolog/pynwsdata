
import unittest

from pynwsdata.models.office_headline import OfficeHeadline

class TestOfficeHeadline(unittest.TestCase):
    """OfficeHeadline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OfficeHeadline:
        """Test OfficeHeadline
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfficeHeadline`
        """
        model = OfficeHeadline()
        if include_optional:
            return OfficeHeadline(
                context = None,
                id = '',
                id = '',
                office = '',
                important = True,
                issuance_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                link = '',
                name = '',
                title = '',
                summary = '',
                content = ''
            )
        else:
            return OfficeHeadline(
        )
        """

    def testOfficeHeadline(self):
        """Test OfficeHeadline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
