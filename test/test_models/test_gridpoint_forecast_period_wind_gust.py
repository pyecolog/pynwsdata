
import unittest

from pynwsdata.models.gridpoint_forecast_period_wind_gust import GridpointForecastPeriodWindGust

class TestGridpointForecastPeriodWindGust(unittest.TestCase):
    """GridpointForecastPeriodWindGust unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointForecastPeriodWindGust:
        """Test GridpointForecastPeriodWindGust
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointForecastPeriodWindGust`
        """
        model = GridpointForecastPeriodWindGust()
        if include_optional:
            return GridpointForecastPeriodWindGust(
                value = 1.337,
                max_value = 1.337,
                min_value = 1.337,
                unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:',
                quality_control = 'Z'
            )
        else:
            return GridpointForecastPeriodWindGust(
        )
        """

    def testGridpointForecastPeriodWindGust(self):
        """Test GridpointForecastPeriodWindGust"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
