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
from upguard.api.labels_api import LabelsApi  # noqa: E501
from upguard.rest import ApiException


class TestLabelsApi(unittest.TestCase):
    """LabelsApi unit test stubs"""

    def setUp(self):
        self.api = upguard.api.labels_api.LabelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_labels(self):
        """Test case for labels

        Get the list of registered labels  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
