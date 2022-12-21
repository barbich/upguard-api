# coding: utf-8

"""
    UpGuard CyberRisk API

    Access information from the CyberRisk platform programmatically using this API.  You can find or generate an API key to access this API in your CyberRisk Account Settings. Please authorize all requests by setting the \"Authorization\" header to your api key.  The base url for all public endpoints is https://cyber-risk.upguard.com/api/public  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import upguard
from upguard.models.webhook import Webhook  # noqa: E501
from upguard.rest import ApiException


class TestWebhook(unittest.TestCase):
    """Webhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWebhook(self):
        """Test Webhook"""
        # FIXME: construct object with mandatory attributes with example values
        # model = upguard.models.webhook.Webhook()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
