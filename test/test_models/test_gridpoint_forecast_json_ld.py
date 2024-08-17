
import unittest

from pynwsdata.models.gridpoint_forecast_json_ld import GridpointForecastJsonLd

class TestGridpointForecastJsonLd(unittest.TestCase):
    """GridpointForecastJsonLd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GridpointForecastJsonLd:
        """Test GridpointForecastJsonLd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GridpointForecastJsonLd`
        """
        model = GridpointForecastJsonLd()
        if include_optional:
            return GridpointForecastJsonLd(
                context = None,
                geometry = '',
                units = 'us',
                forecast_generator = '',
                generated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                valid_times = None,
                elevation = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                periods = [
                    pynwsdata.models.gridpoint_forecast_period.GridpointForecastPeriod(
                        number = 1, 
                        name = 'Tuesday Night', 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        is_daytime = True, 
                        temperature = null, 
                        temperature_unit = 'F', 
                        temperature_trend = 'rising', 
                        probability_of_precipitation = pynwsdata.models.quantitative_value.QuantitativeValue(
                            value = 1.337, 
                            max_value = 1.337, 
                            min_value = 1.337, 
                            unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                            quality_control = 'Z', ), 
                        dewpoint = pynwsdata.models.quantitative_value.QuantitativeValue(
                            value = 1.337, 
                            max_value = 1.337, 
                            min_value = 1.337, 
                            quality_control = 'Z', ), 
                        relative_humidity = , 
                        wind_speed = null, 
                        wind_gust = null, 
                        wind_direction = 'N', 
                        icon = '', 
                        short_forecast = '', 
                        detailed_forecast = '', )
                    ]
            )
        else:
            return GridpointForecastJsonLd(
                context = None,
                geometry = '',
        )
        """

    def testGridpointForecastJsonLd(self):
        """Test GridpointForecastJsonLd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
