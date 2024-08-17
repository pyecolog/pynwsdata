
import unittest

from pynwsdata.models.observation_station import ObservationStation

class TestObservationStation(unittest.TestCase):
    """ObservationStation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationStation:
        """Test ObservationStation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationStation`
        """
        model = ObservationStation()
        if include_optional:
            return ObservationStation(
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
                station_identifier = '',
                name = '',
                time_zone = '',
                forecast = '',
                county = '',
                fire_weather_zone = ''
            )
        else:
            return ObservationStation(
        )
        """

    def testObservationStation(self):
        """Test ObservationStation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
