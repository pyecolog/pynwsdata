
import unittest

from pynwsdata.models.problem_detail import ProblemDetail

class TestProblemDetail(unittest.TestCase):
    """ProblemDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProblemDetail:
        """Test ProblemDetail
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProblemDetail`
        """
        model = ProblemDetail()
        if include_optional:
            return ProblemDetail(
                type = 'about:blank',
                title = 'Unexpected Problem',
                status = 500,
                detail = 'An unexpected problem has occurred.',
                instance = 'urn:noaa:nws:api:request:493c3a1d-f87e-407f-ae2c-24483f5aab63',
                correlation_id = '493c3a1d-f87e-407f-ae2c-24483f5aab63'
            )
        else:
            return ProblemDetail(
                type = 'about:blank',
                title = 'Unexpected Problem',
                status = 500,
                detail = 'An unexpected problem has occurred.',
                instance = 'urn:noaa:nws:api:request:493c3a1d-f87e-407f-ae2c-24483f5aab63',
                correlation_id = '493c3a1d-f87e-407f-ae2c-24483f5aab63',
        )
        """

    def testProblemDetail(self):
        """Test ProblemDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
