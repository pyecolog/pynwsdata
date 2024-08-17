
import unittest

from pynwsdata.models.glossary200_response_glossary_inner import Glossary200ResponseGlossaryInner

class TestGlossary200ResponseGlossaryInner(unittest.TestCase):
    """Glossary200ResponseGlossaryInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Glossary200ResponseGlossaryInner:
        """Test Glossary200ResponseGlossaryInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Glossary200ResponseGlossaryInner`
        """
        model = Glossary200ResponseGlossaryInner()
        if include_optional:
            return Glossary200ResponseGlossaryInner(
                term = '',
                definition = ''
            )
        else:
            return Glossary200ResponseGlossaryInner(
        )
        """

    def testGlossary200ResponseGlossaryInner(self):
        """Test Glossary200ResponseGlossaryInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
