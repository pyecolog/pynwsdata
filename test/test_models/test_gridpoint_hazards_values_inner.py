
import unittest

from pynwsdata.models.gridpoint_hazards_values_inner import GridpointHazardsValuesInner

class TestGridpointHazardsValuesInner(unittest.TestCase):
    """GridpointHazardsValuesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointHazardsValuesInner:
        """Test GridpointHazardsValuesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointHazardsValuesInner`
        """
        model = GridpointHazardsValuesInner()
        if include_optional:
            return GridpointHazardsValuesInner(
                valid_time = None,
                value = [
                    pynwsdata.models.gridpoint_hazards_values_inner_value_inner.Gridpoint_hazards_values_inner_value_inner(
                        phenomenon = 'eH', 
                        significance = 'e', 
                        event_number = 56, )
                    ]
            )
        else:
            return GridpointHazardsValuesInner(
                valid_time = None,
                value = [
                    pynwsdata.models.gridpoint_hazards_values_inner_value_inner.Gridpoint_hazards_values_inner_value_inner(
                        phenomenon = 'eH', 
                        significance = 'e', 
                        event_number = 56, )
                    ],
        )
        """

    def testGridpointHazardsValuesInner(self):
        """Test GridpointHazardsValuesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
