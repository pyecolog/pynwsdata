
import unittest

from pynwsdata.models.gridpoint_hazards_values_inner_value_inner import GridpointHazardsValuesInnerValueInner

class TestGridpointHazardsValuesInnerValueInner(unittest.TestCase):
    """GridpointHazardsValuesInnerValueInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointHazardsValuesInnerValueInner:
        """Test GridpointHazardsValuesInnerValueInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointHazardsValuesInnerValueInner`
        """
        model = GridpointHazardsValuesInnerValueInner()
        if include_optional:
            return GridpointHazardsValuesInnerValueInner(
                phenomenon = 'eH',
                significance = 'e',
                event_number = 56
            )
        else:
            return GridpointHazardsValuesInnerValueInner(
                phenomenon = 'eH',
                significance = 'e',
                event_number = 56,
        )
        """

    def testGridpointHazardsValuesInnerValueInner(self):
        """Test GridpointHazardsValuesInnerValueInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
