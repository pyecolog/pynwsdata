
import unittest

from pynwsdata.models.geo_json_geometry import GeoJsonGeometry

class TestGeoJsonGeometry(unittest.TestCase):
    """GeoJsonGeometry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeoJsonGeometry:
        """Test GeoJsonGeometry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeoJsonGeometry`
        """
        model = GeoJsonGeometry()
        if include_optional:
            return GeoJsonGeometry(
                type = 'Point',
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
            return GeoJsonGeometry(
                type = 'Point',
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

    def testGeoJsonGeometry(self):
        """Test GeoJsonGeometry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
