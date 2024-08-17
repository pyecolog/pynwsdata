
import unittest

from pynwsdata.models.point_json_ld import PointJsonLd

class TestPointJsonLd(unittest.TestCase):
    """PointJsonLd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PointJsonLd:
        """Test PointJsonLd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PointJsonLd`
        """
        model = PointJsonLd()
        if include_optional:
            return PointJsonLd(
                context = None,
                geometry = '',
                id = '',
                type = 'wx:Point',
                cwa = 'AKQ',
                forecast_office = '',
                grid_id = 'AKQ',
                grid_x = 0,
                grid_y = 0,
                forecast = '',
                forecast_hourly = '',
                forecast_grid_data = '',
                observation_stations = '',
                relative_location = None,
                forecast_zone = '',
                county = '',
                fire_weather_zone = '',
                time_zone = '',
                radar_station = ''
            )
        else:
            return PointJsonLd(
                context = None,
                geometry = '',
        )
        """

    def testPointJsonLd(self):
        """Test PointJsonLd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
