# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class BundleTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .bundles.create(friendly_name="friendly_name", email="email")

        values = {'FriendlyName': "friendly_name", 'Email': "email", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "regulation_sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "status": "draft",
                "email": "email",
                "status_callback": "http://www.example.com",
                "date_created": "2019-07-30T22:29:24Z",
                "date_updated": "2019-07-31T01:09:00Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "item_assignments": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ItemAssignments"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .bundles.create(friendly_name="friendly_name", email="email")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .bundles.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .bundles.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [
                    {
                        "sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "regulation_sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "friendly_name",
                        "status": "draft",
                        "email": "email",
                        "status_callback": "http://www.example.com",
                        "date_created": "2019-07-30T22:29:24Z",
                        "date_updated": "2019-07-31T01:09:00Z",
                        "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "item_assignments": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ItemAssignments"
                        }
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?Status=draft&RegulationSid=RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&IsoCountry=US&FriendlyName=friendly_name&NumberType=mobile&PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles?Status=draft&RegulationSid=RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&IsoCountry=US&FriendlyName=friendly_name&NumberType=mobile&PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .bundles.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .bundles(sid="BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "regulation_sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "status": "draft",
                "email": "email",
                "status_callback": "http://www.example.com",
                "date_created": "2019-07-30T22:29:24Z",
                "date_updated": "2019-07-31T01:09:00Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "item_assignments": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ItemAssignments"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .bundles(sid="BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .bundles(sid="BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "regulation_sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "status": "draft",
                "email": "email",
                "status_callback": "http://www.example.com",
                "date_created": "2019-07-30T22:29:24Z",
                "date_updated": "2019-07-31T01:09:00Z",
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "item_assignments": "https://numbers.twilio.com/v2/RegulatoryCompliance/Bundles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ItemAssignments"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .bundles(sid="BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
