
import unittest

from pynwsdata.models.gridpoint_quantitative_value_layer import GridpointQuantitativeValueLayer

class TestGridpointQuantitativeValueLayer(unittest.TestCase):
    """GridpointQuantitativeValueLayer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointQuantitativeValueLayer:
        """Test GridpointQuantitativeValueLayer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointQuantitativeValueLayer`
        """
        model = GridpointQuantitativeValueLayer()
        if include_optional:
            return GridpointQuantitativeValueLayer(
                uom = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:',
                values = [
                    pynwsdata.models.gridpoint_quantitative_value_layer_values_inner.GridpointQuantitativeValueLayer_values_inner(
                        valid_time = null, 
                        value = 1.337, )
                    ]
            )
        else:
            return GridpointQuantitativeValueLayer(
                values = [
                    pynwsdata.models.gridpoint_quantitative_value_layer_values_inner.GridpointQuantitativeValueLayer_values_inner(
                        valid_time = null, 
                        value = 1.337, )
                    ],
        )
        """

    def testGridpointQuantitativeValueLayer(self):
        """Test GridpointQuantitativeValueLayer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
