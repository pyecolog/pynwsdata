
import unittest

from pynwsdata.models.center_weather_advisory_geo_json import CenterWeatherAdvisoryGeoJson

class TestCenterWeatherAdvisoryGeoJson(unittest.TestCase):
    """CenterWeatherAdvisoryGeoJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CenterWeatherAdvisoryGeoJson:
        """Test CenterWeatherAdvisoryGeoJson
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CenterWeatherAdvisoryGeoJson`
        """
        model = CenterWeatherAdvisoryGeoJson()
        if include_optional:
            return CenterWeatherAdvisoryGeoJson(
                context = None,
                id = '',
                type = 'Feature',
                geometry = None,
                properties = pynwsdata.models.center_weather_advisory.CenterWeatherAdvisory(
                    id = '', 
                    issue_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    cwsu = 'ZAB', 
                    sequence = 101, 
                    start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    observed_property = '', 
                    text = '', )
            )
        else:
            return CenterWeatherAdvisoryGeoJson(
                type = 'Feature',
                geometry = None,
                properties = pynwsdata.models.center_weather_advisory.CenterWeatherAdvisory(
                    id = '', 
                    issue_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    cwsu = 'ZAB', 
                    sequence = 101, 
                    start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    observed_property = '', 
                    text = '', ),
        )
        """

    def testCenterWeatherAdvisoryGeoJson(self):
        """Test CenterWeatherAdvisoryGeoJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
