
import unittest

from pynwsdata.models.observation import Observation

class TestObservation(unittest.TestCase):
    """Observation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Observation:
        """Test Observation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Observation`
        """
        model = Observation()
        if include_optional:
            return Observation(
                context = None,
                geometry = '',
                id = '',
                type = 'wx:ObservationStation',
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
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                dewpoint = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                wind_direction = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                wind_speed = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                wind_gust = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                barometric_pressure = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                sea_level_pressure = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                visibility = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                max_temperature_last24_hours = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                min_temperature_last24_hours = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                precipitation_last_hour = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                precipitation_last3_hours = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                precipitation_last6_hours = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                relative_humidity = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                wind_chill = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                heat_index = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                cloud_layers = [
                    pynwsdata.models.observation_cloud_layers_inner.Observation_cloudLayers_inner(
                        base = pynwsdata.models.quantitative_value.QuantitativeValue(
                            value = 1.337, 
                            max_value = 1.337, 
                            min_value = 1.337, 
                            unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                            quality_control = 'Z', ), 
                        amount = 'OVC', )
                    ]
            )
        else:
            return Observation(
        )
        """

    def testObservation(self):
        """Test Observation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
