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
from upguard.api.vulnerabilities_api import VulnerabilitiesApi  # noqa: E501
from upguard.rest import ApiException


class TestVulnerabilitiesApi(unittest.TestCase):
    """VulnerabilitiesApi unit test stubs"""

    def setUp(self):
        self.api = upguard.api.vulnerabilities_api.VulnerabilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_org_vulnerabilities(self):
        """Test case for org_vulnerabilities

        List potential vulnerabilities of your domains & IPs  # noqa: E501
        """
        pass

    def test_vendor_vulnerabilities(self):
        """Test case for vendor_vulnerabilities

        List potential vulnerabilities of a vendor  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
