
import unittest

from pynwsdata.models.geo_json_multi_polygon import GeoJSONMultiPolygon

class TestGeoJSONMultiPolygon(unittest.TestCase):
    """GeoJSONMultiPolygon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoJSONMultiPolygon:
        """Test GeoJSONMultiPolygon
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoJSONMultiPolygon`
        """
        model = GeoJSONMultiPolygon()
        if include_optional:
            return GeoJSONMultiPolygon(
                type = 'MultiPolygon',
                coordinates = [
                    [
                        [
                            [
                                1.337
                                ]
                            ]
                        ]
                    ],
                bbox = [
                    1.337
                    ]
            )
        else:
            return GeoJSONMultiPolygon(
                type = 'MultiPolygon',
                coordinates = [
                    [
                        [
                            [
                                1.337
                                ]
                            ]
                        ]
                    ],
        )
        """

    def testGeoJSONMultiPolygon(self):
        """Test GeoJSONMultiPolygon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
