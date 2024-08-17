
import unittest

from pynwsdata.models.office_headline_collection import OfficeHeadlineCollection

class TestOfficeHeadlineCollection(unittest.TestCase):
    """OfficeHeadlineCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OfficeHeadlineCollection:
        """Test OfficeHeadlineCollection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfficeHeadlineCollection`
        """
        model = OfficeHeadlineCollection()
        if include_optional:
            return OfficeHeadlineCollection(
                context = None,
                graph = [
                    pynwsdata.models.office_headline.OfficeHeadline(
                        @context = null, 
                        @id = '', 
                        id = '', 
                        office = '', 
                        important = True, 
                        issuance_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        link = '', 
                        name = '', 
                        title = '', 
                        summary = '', 
                        content = '', )
                    ]
            )
        else:
            return OfficeHeadlineCollection(
                context = None,
                graph = [
                    pynwsdata.models.office_headline.OfficeHeadline(
                        @context = null, 
                        @id = '', 
                        id = '', 
                        office = '', 
                        important = True, 
                        issuance_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        link = '', 
                        name = '', 
                        title = '', 
                        summary = '', 
                        content = '', )
                    ],
        )
        """

    def testOfficeHeadlineCollection(self):
        """Test OfficeHeadlineCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
