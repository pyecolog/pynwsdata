
import unittest

from pynwsdata.models.zone_collection_geo_json_all_of_features import ZoneCollectionGeoJsonAllOfFeatures

class TestZoneCollectionGeoJsonAllOfFeatures(unittest.TestCase):
    """ZoneCollectionGeoJsonAllOfFeatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ZoneCollectionGeoJsonAllOfFeatures:
        """Test ZoneCollectionGeoJsonAllOfFeatures
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ZoneCollectionGeoJsonAllOfFeatures`
        """
        model = ZoneCollectionGeoJsonAllOfFeatures()
        if include_optional:
            return ZoneCollectionGeoJsonAllOfFeatures(
                properties = pynwsdata.models.zone.Zone(
                    @context = null, 
                    geometry = '', 
                    @id = '', 
                    @type = 'wx:Zone', 
                    id = 'UTZ807', 
                    type = 'land', 
                    name = '', 
                    effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expiration_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    state = null, 
                    forecast_office = '', 
                    grid_identifier = '', 
                    awips_location_identifier = '', 
                    cwa = [
                        'AKQ'
                        ], 
                    forecast_offices = [
                        ''
                        ], 
                    time_zone = [
                        ''
                        ], 
                    observation_stations = [
                        ''
                        ], 
                    radar_station = '', )
            )
        else:
            return ZoneCollectionGeoJsonAllOfFeatures(
        )
        """

    def testZoneCollectionGeoJsonAllOfFeatures(self):
        """Test ZoneCollectionGeoJsonAllOfFeatures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
