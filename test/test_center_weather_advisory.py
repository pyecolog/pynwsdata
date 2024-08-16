# coding: utf-8

"""
    weather.gov API

    weather.gov API

    The version of the OpenAPI document: 1.13.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pynwsdata.models.center_weather_advisory import CenterWeatherAdvisory

class TestCenterWeatherAdvisory(unittest.TestCase):
    """CenterWeatherAdvisory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CenterWeatherAdvisory:
        """Test CenterWeatherAdvisory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CenterWeatherAdvisory`
        """
        model = CenterWeatherAdvisory()
        if include_optional:
            return CenterWeatherAdvisory(
                id = '',
                issue_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                cwsu = 'ZAB',
                sequence = 101,
                start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                observed_property = '',
                text = ''
            )
        else:
            return CenterWeatherAdvisory(
        )
        """

    def testCenterWeatherAdvisory(self):
        """Test CenterWeatherAdvisory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
