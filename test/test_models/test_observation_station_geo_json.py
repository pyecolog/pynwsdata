
import unittest

from pynwsdata.models.observation_station_geo_json import ObservationStationGeoJson

class TestObservationStationGeoJson(unittest.TestCase):
    """ObservationStationGeoJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationStationGeoJson:
        """Test ObservationStationGeoJson
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationStationGeoJson`
        """
        model = ObservationStationGeoJson()
        if include_optional:
            return ObservationStationGeoJson(
                context = None,
                id = '',
                type = 'Feature',
                geometry = None,
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
                    fire_weather_zone = '', )
            )
        else:
            return ObservationStationGeoJson(
                type = 'Feature',
                geometry = None,
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
                    fire_weather_zone = '', ),
        )
        """

    def testObservationStationGeoJson(self):
        """Test ObservationStationGeoJson"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
