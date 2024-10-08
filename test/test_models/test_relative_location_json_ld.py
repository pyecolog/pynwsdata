
import unittest

from pynwsdata.models.relative_location_json_ld import RelativeLocationJsonLd

class TestRelativeLocationJsonLd(unittest.TestCase):
    """RelativeLocationJsonLd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RelativeLocationJsonLd:
        """Test RelativeLocationJsonLd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RelativeLocationJsonLd`
        """
        model = RelativeLocationJsonLd()
        if include_optional:
            return RelativeLocationJsonLd(
                city = '',
                state = '',
                distance = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                bearing = pynwsdata.models.quantitative_value.QuantitativeValue(
                    value = 1.337, 
                    max_value = 1.337, 
                    min_value = 1.337, 
                    unit_code = 'nwsUnit:R,rZ#UM/?R,Fp^l6$ARjbhJk C>i H'qT\\{<?'es#)#iK.YM{Rag2/!KB!k@5oXh.:', 
                    quality_control = 'Z', ),
                geometry = ''
            )
        else:
            return RelativeLocationJsonLd(
                geometry = '',
        )
        """

    def testRelativeLocationJsonLd(self):
        """Test RelativeLocationJsonLd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
