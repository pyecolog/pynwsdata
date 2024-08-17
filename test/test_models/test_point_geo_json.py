
import unittest

from pynwsdata.models.point_geo_json import PointGeoJson

class TestPointGeoJson(unittest.TestCase):
    """PointGeoJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PointGeoJson:
        """Test PointGeoJson
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PointGeoJson`
        """
        model = PointGeoJson()
        if include_optional:
            return PointGeoJson(
                context = None,
                id = '',
                type = 'Feature',
                geometry = None,
                properties = pynwsdata.models.point.Point(
                    @context = null, 
                    geometry = '', 
                    @id = '', 
                    @type = 'wx:Point', 
                    cwa = 'AKQ', 
                    forecast_office = '', 
                    grid_id = 'AKQ', 
                    grid_x = 0, 
                    grid_y = 0, 
                    forecast = '', 
                    forecast_hourly = '', 
                    forecast_grid_data = '', 
                    observation_stations = '', 
                    relative_location = null, 
                    forecast_zone = '', 
                    county = '', 
                    fire_weather_zone = '', 
                    time_zone = '', 
                    radar_station = '', )
            )
        else:
            return PointGeoJson(
                type = 'Feature',
                geometry = None,
                properties = pynwsdata.models.point.Point(
                    @context = null, 
                    geometry = '', 
                    @id = '', 
                    @type = 'wx:Point', 
                    cwa = 'AKQ', 
                    forecast_office = '', 
                    grid_id = 'AKQ', 
                    grid_x = 0, 
                    grid_y = 0, 
                    forecast = '', 
                    forecast_hourly = '', 
                    forecast_grid_data = '', 
                    observation_stations = '', 
                    relative_location = null, 
                    forecast_zone = '', 
                    county = '', 
                    fire_weather_zone = '', 
                    time_zone = '', 
                    radar_station = '', ),
        )
        """

    def testPointGeoJson(self):
        """Test PointGeoJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
