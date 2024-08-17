
import unittest

from pynwsdata.models.observation_station_collection_json_ld import ObservationStationCollectionJsonLd

class TestObservationStationCollectionJsonLd(unittest.TestCase):
    """ObservationStationCollectionJsonLd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationStationCollectionJsonLd:
        """Test ObservationStationCollectionJsonLd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationStationCollectionJsonLd`
        """
        model = ObservationStationCollectionJsonLd()
        if include_optional:
            return ObservationStationCollectionJsonLd(
                context = None,
                graph = [
                    pynwsdata.models.observation_station.ObservationStation(
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
                        fire_weather_zone = '', )
                    ],
                observation_stations = [
                    ''
                    ],
                pagination = pynwsdata.models.pagination_info.PaginationInfo(
                    next = '', )
            )
        else:
            return ObservationStationCollectionJsonLd(
        )
        """

    def testObservationStationCollectionJsonLd(self):
        """Test ObservationStationCollectionJsonLd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
