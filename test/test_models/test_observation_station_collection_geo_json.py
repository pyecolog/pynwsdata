
import unittest

from pynwsdata.models.observation_station_collection_geo_json import ObservationStationCollectionGeoJson

class TestObservationStationCollectionGeoJson(unittest.TestCase):
    """ObservationStationCollectionGeoJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationStationCollectionGeoJson:
        """Test ObservationStationCollectionGeoJson
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationStationCollectionGeoJson`
        """
        model = ObservationStationCollectionGeoJson()
        if include_optional:
            return ObservationStationCollectionGeoJson(
                context = None,
                type = 'FeatureCollection',
                features = [
                    pynwsdata.models.observation_station_collection_geo_json_all_of_features.ObservationStationCollectionGeoJson_allOf_features(
                        properties = pynwsdata.models.observation_station.ObservationStation(
                            @context = null, 
                            geometry = '', 
                            @id = '', 
                            @type = 'wx:ObservationStation', 
                            elevation = pynwsdata.models.quantitative_value.QuantitativeValue(
                                value = 1.337, 
                                max_value = 1.337, 
                                min_value = 1.337, 
                                unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                                quality_control = 'Z', ), 
                            station_identifier = '', 
                            name = '', 
                            time_zone = '', 
                            forecast = '', 
                            county = '', 
                            fire_weather_zone = '', ), )
                    ],
                observation_stations = [
                    ''
                    ],
                pagination = pynwsdata.models.pagination_info.PaginationInfo(
                    next = '', )
            )
        else:
            return ObservationStationCollectionGeoJson(
                type = 'FeatureCollection',
                features = [
                    pynwsdata.models.observation_station_collection_geo_json_all_of_features.ObservationStationCollectionGeoJson_allOf_features(
                        properties = pynwsdata.models.observation_station.ObservationStation(
                            @context = null, 
                            geometry = '', 
                            @id = '', 
                            @type = 'wx:ObservationStation', 
                            elevation = pynwsdata.models.quantitative_value.QuantitativeValue(
                                value = 1.337, 
                                max_value = 1.337, 
                                min_value = 1.337, 
                                unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                                quality_control = 'Z', ), 
                            station_identifier = '', 
                            name = '', 
                            time_zone = '', 
                            forecast = '', 
                            county = '', 
                            fire_weather_zone = '', ), )
                    ],
        )
        """

    def testObservationStationCollectionGeoJson(self):
        """Test ObservationStationCollectionGeoJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
