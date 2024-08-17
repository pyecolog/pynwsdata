
import unittest

from pynwsdata.models.observation_collection_json_ld import ObservationCollectionJsonLd

class TestObservationCollectionJsonLd(unittest.TestCase):
    """ObservationCollectionJsonLd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationCollectionJsonLd:
        """Test ObservationCollectionJsonLd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationCollectionJsonLd`
        """
        model = ObservationCollectionJsonLd()
        if include_optional:
            return ObservationCollectionJsonLd(
                context = None,
                graph = [
                    pynwsdata.models.observation.Observation(
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
                        station = '', 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        raw_message = '', 
                        text_description = '', 
                        icon = '', 
                        present_weather = [
                            pynwsdata.models.metar_phenomenon.MetarPhenomenon(
                                intensity = 'light', 
                                modifier = 'patches', 
                                weather = 'fog_mist', 
                                raw_string = '', 
                                in_vicinity = True, )
                            ], 
                        temperature = pynwsdata.models.quantitative_value.QuantitativeValue(
                            value = 1.337, 
                            max_value = 1.337, 
                            min_value = 1.337, 
                            quality_control = 'Z', ), 
                        dewpoint = , 
                        wind_direction = , 
                        wind_speed = , 
                        wind_gust = , 
                        barometric_pressure = , 
                        sea_level_pressure = , 
                        visibility = , 
                        max_temperature_last24_hours = , 
                        min_temperature_last24_hours = , 
                        precipitation_last_hour = , 
                        precipitation_last3_hours = , 
                        precipitation_last6_hours = , 
                        relative_humidity = , 
                        wind_chill = , 
                        heat_index = , 
                        cloud_layers = [
                            pynwsdata.models.observation_cloud_layers_inner.Observation_cloudLayers_inner(
                                base = , 
                                amount = 'OVC', )
                            ], )
                    ]
            )
        else:
            return ObservationCollectionJsonLd(
        )
        """

    def testObservationCollectionJsonLd(self):
        """Test ObservationCollectionJsonLd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
