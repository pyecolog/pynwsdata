
import unittest

from pynwsdata.models.pagination_info import PaginationInfo

class TestPaginationInfo(unittest.TestCase):
    """PaginationInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaginationInfo:
        """Test PaginationInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaginationInfo`
        """
        model = PaginationInfo()
        if include_optional:
            return PaginationInfo(
                next = ''
            )
        else:
            return PaginationInfo(
                next = '',
        )
        """

    def testPaginationInfo(self):
        """Test PaginationInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
