
import unittest

from pynwsdata.models.gridpoint import Gridpoint

class TestGridpoint(unittest.TestCase):
    """Gridpoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Gridpoint:
        """Test Gridpoint
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Gridpoint`
        """
        model = Gridpoint()
        if include_optional:
            return Gridpoint(
                context = None,
                geometry = '',
                id = '',
                type = 'wx:Gridpoint',
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                valid_times = None,
                elevation = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                forecast_office = '',
                grid_id = '',
                grid_x = 0,
                grid_y = 0,
                weather = pynwsdata.models.gridpoint_weather.Gridpoint_weather(
                    values = [
                        pynwsdata.models.gridpoint_weather_values_inner.Gridpoint_weather_values_inner(
                            valid_time = null, 
                            value = [
                                pynwsdata.models.gridpoint_weather_values_inner_value_inner.Gridpoint_weather_values_inner_value_inner(
                                    coverage = 'areas', 
                                    weather = 'blowing_dust', 
                                    intensity = 'very_light', 
                                    visibility = pynwsdata.models.quantitative_value.QuantitativeValue(
                                        max_value = 1.337, 
                                        min_value = 1.337, 
                                        unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                                        quality_control = 'Z', ), 
                                    attributes = [
                                        'damaging_wind'
                                        ], )
                                ], )
                        ], ),
                hazards = pynwsdata.models.gridpoint_hazards.Gridpoint_hazards(
                    values = [
                        pynwsdata.models.gridpoint_hazards_values_inner.Gridpoint_hazards_values_inner(
                            valid_time = null, 
                            value = [
                                pynwsdata.models.gridpoint_hazards_values_inner_value_inner.Gridpoint_hazards_values_inner_value_inner(
                                    phenomenon = 'eH', 
                                    significance = 'e', 
                                    event_number = 56, )
                                ], )
                        ], )
            )
        else:
            return Gridpoint(
        )
        """

    def testGridpoint(self):
        """Test Gridpoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
