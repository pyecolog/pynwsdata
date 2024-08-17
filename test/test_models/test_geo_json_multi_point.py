
import unittest

from pynwsdata.models.geo_json_multi_point import GeoJSONMultiPoint

class TestGeoJSONMultiPoint(unittest.TestCase):
    """GeoJSONMultiPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoJSONMultiPoint:
        """Test GeoJSONMultiPoint
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoJSONMultiPoint`
        """
        model = GeoJSONMultiPoint()
        if include_optional:
            return GeoJSONMultiPoint(
                type = 'MultiPoint',
                coordinates = [
                    [
                        1.337
                        ]
                    ],
                bbox = [
                    1.337
                    ]
            )
        else:
            return GeoJSONMultiPoint(
                type = 'MultiPoint',
                coordinates = [
                    [
                        1.337
                        ]
                    ],
        )
        """

    def testGeoJSONMultiPoint(self):
        """Test GeoJSONMultiPoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
