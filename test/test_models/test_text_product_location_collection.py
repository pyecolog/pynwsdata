
import unittest

from pynwsdata.models.text_product_location_collection import TextProductLocationCollection

class TestTextProductLocationCollection(unittest.TestCase):
    """TextProductLocationCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextProductLocationCollection:
        """Test TextProductLocationCollection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextProductLocationCollection`
        """
        model = TextProductLocationCollection()
        if include_optional:
            return TextProductLocationCollection(
                context = None,
                locations = {
                    'key' : ''
                    }
            )
        else:
            return TextProductLocationCollection(
        )
        """

    def testTextProductLocationCollection(self):
        """Test TextProductLocationCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
