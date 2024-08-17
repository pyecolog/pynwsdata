
import unittest

from pynwsdata.models.geo_json_polygon import GeoJSONPolygon

class TestGeoJSONPolygon(unittest.TestCase):
    """GeoJSONPolygon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoJSONPolygon:
        """Test GeoJSONPolygon
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoJSONPolygon`
        """
        model = GeoJSONPolygon()
        if include_optional:
            return GeoJSONPolygon(
                type = 'Polygon',
                coordinates = [
                    [
                        [
                            1.337
                            ]
                        ]
                    ],
                bbox = [
                    1.337
                    ]
            )
        else:
            return GeoJSONPolygon(
                type = 'Polygon',
                coordinates = [
                    [
                        [
                            1.337
                            ]
                        ]
                    ],
        )
        """

    def testGeoJSONPolygon(self):
        """Test GeoJSONPolygon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
