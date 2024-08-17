
import unittest

from pynwsdata.models.gridpoint_forecast_period_temperature import GridpointForecastPeriodTemperature

class TestGridpointForecastPeriodTemperature(unittest.TestCase):
    """GridpointForecastPeriodTemperature unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointForecastPeriodTemperature:
        """Test GridpointForecastPeriodTemperature
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointForecastPeriodTemperature`
        """
        model = GridpointForecastPeriodTemperature()
        if include_optional:
            return GridpointForecastPeriodTemperature(
                value = 1.337,
                max_value = 1.337,
                min_value = 1.337,
                unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:',
                quality_control = 'Z'
            )
        else:
            return GridpointForecastPeriodTemperature(
        )
        """

    def testGridpointForecastPeriodTemperature(self):
        """Test GridpointForecastPeriodTemperature"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
