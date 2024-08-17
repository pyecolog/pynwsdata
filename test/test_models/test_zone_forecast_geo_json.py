
import unittest

from pynwsdata.models.zone_forecast_geo_json import ZoneForecastGeoJson

class TestZoneForecastGeoJson(unittest.TestCase):
    """ZoneForecastGeoJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ZoneForecastGeoJson:
        """Test ZoneForecastGeoJson
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ZoneForecastGeoJson`
        """
        model = ZoneForecastGeoJson()
        if include_optional:
            return ZoneForecastGeoJson(
                context = None,
                id = '',
                type = 'Feature',
                geometry = None,
                properties = pynwsdata.models.zone_forecast.ZoneForecast(
                    @context = null, 
                    geometry = '', 
                    zone = '', 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    periods = [
                        pynwsdata.models.zone_forecast_periods_inner.ZoneForecast_periods_inner(
                            number = 56, 
                            name = 'This Afternoon', 
                            detailed_forecast = '', )
                        ], )
            )
        else:
            return ZoneForecastGeoJson(
                type = 'Feature',
                geometry = None,
                properties = pynwsdata.models.zone_forecast.ZoneForecast(
                    @context = null, 
                    geometry = '', 
                    zone = '', 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    periods = [
                        pynwsdata.models.zone_forecast_periods_inner.ZoneForecast_periods_inner(
                            number = 56, 
                            name = 'This Afternoon', 
                            detailed_forecast = '', )
                        ], ),
        )
        """

    def testZoneForecastGeoJson(self):
        """Test ZoneForecastGeoJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
