
import unittest

from pynwsdata.models.center_weather_advisory_collection_geo_json_all_of_features import CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures

class TestCenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures(unittest.TestCase):
    """CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures:
        """Test CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures`
        """
        model = CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures()
        if include_optional:
            return CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures(
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
            return CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures(
        )
        """

    def testCenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures(self):
        """Test CenterWeatherAdvisoryCollectionGeoJsonAllOfFeatures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
