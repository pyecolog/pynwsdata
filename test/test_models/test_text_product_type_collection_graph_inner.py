
import unittest

from pynwsdata.models.text_product_type_collection_graph_inner import TextProductTypeCollectionGraphInner

class TestTextProductTypeCollectionGraphInner(unittest.TestCase):
    """TextProductTypeCollectionGraphInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TextProductTypeCollectionGraphInner:
        """Test TextProductTypeCollectionGraphInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TextProductTypeCollectionGraphInner`
        """
        model = TextProductTypeCollectionGraphInner()
        if include_optional:
            return TextProductTypeCollectionGraphInner(
                product_code = '',
                product_name = ''
            )
        else:
            return TextProductTypeCollectionGraphInner(
                product_code = '',
                product_name = '',
        )
        """

    def testTextProductTypeCollectionGraphInner(self):
        """Test TextProductTypeCollectionGraphInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
