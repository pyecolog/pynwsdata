
import unittest

from pynwsdata.models.json_ld_context import JsonLdContext

class TestJsonLdContext(unittest.TestCase):
    """JsonLdContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonLdContext:
        """Test JsonLdContext
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonLdContext`
        """
        model = JsonLdContext()
        if include_optional:
            return JsonLdContext(
            )
        else:
            return JsonLdContext(
        )
        """

    def testJsonLdContext(self):
        """Test JsonLdContext"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
