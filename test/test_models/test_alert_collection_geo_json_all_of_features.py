
import unittest

from pynwsdata.models.alert_collection_geo_json_all_of_features import AlertCollectionGeoJsonAllOfFeatures

class TestAlertCollectionGeoJsonAllOfFeatures(unittest.TestCase):
    """AlertCollectionGeoJsonAllOfFeatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertCollectionGeoJsonAllOfFeatures:
        """Test AlertCollectionGeoJsonAllOfFeatures
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertCollectionGeoJsonAllOfFeatures`
        """
        model = AlertCollectionGeoJsonAllOfFeatures()
        if include_optional:
            return AlertCollectionGeoJsonAllOfFeatures(
                properties = pynwsdata.models.alert.Alert(
                    id = '', 
                    area_desc = '', 
                    geocode = pynwsdata.models.alert_geocode.Alert_geocode(
                        ugc = [
                            'UTZ807'
                            ], 
                        same = [
                            '048072'
                            ], ), 
                    affected_zones = [
                        ''
                        ], 
                    references = [
                        pynwsdata.models.alert_references_inner.Alert_references_inner(
                            @id = '', 
                            identifier = '', 
                            sender = '', 
                            sent = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    sent = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    effective = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    onset = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expires = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    ends = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    status = 'Actual', 
                    message_type = 'Alert', 
                    category = 'Met', 
                    severity = 'Extreme', 
                    certainty = 'Observed', 
                    urgency = 'Immediate', 
                    event = '', 
                    sender = '', 
                    sender_name = '', 
                    headline = '', 
                    description = '', 
                    instruction = '', 
                    response = 'Shelter', 
                    parameters = {
                        'key' : [
                            null
                            ]
                        }, )
            )
        else:
            return AlertCollectionGeoJsonAllOfFeatures(
        )
        """

    def testAlertCollectionGeoJsonAllOfFeatures(self):
        """Test AlertCollectionGeoJsonAllOfFeatures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
