
import unittest

from pynwsdata.models.gridpoint_quantitative_value_layer_values_inner import GridpointQuantitativeValueLayerValuesInner

class TestGridpointQuantitativeValueLayerValuesInner(unittest.TestCase):
    """GridpointQuantitativeValueLayerValuesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointQuantitativeValueLayerValuesInner:
        """Test GridpointQuantitativeValueLayerValuesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointQuantitativeValueLayerValuesInner`
        """
        model = GridpointQuantitativeValueLayerValuesInner()
        if include_optional:
            return GridpointQuantitativeValueLayerValuesInner(
                valid_time = None,
                value = 1.337
            )
        else:
            return GridpointQuantitativeValueLayerValuesInner(
                valid_time = None,
                value = 1.337,
        )
        """

    def testGridpointQuantitativeValueLayerValuesInner(self):
        """Test GridpointQuantitativeValueLayerValuesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
