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
from upguard.api.risks_api import RisksApi  # noqa: E501
from upguard.rest import ApiException


class TestRisksApi(unittest.TestCase):
    """RisksApi unit test stubs"""

    def setUp(self):
        self.api = upguard.api.risks_api.RisksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_available_risks(self):
        """Test case for available_risks

        Get a list of available risks in the platform  # noqa: E501
        """
        pass

    def test_available_risks_v2(self):
        """Test case for available_risks_v2

        Get a list of available risks in the platform  # noqa: E501
        """
        pass

    def test_org_risks_diff(self):
        """Test case for org_risks_diff

        Get a list of risk changes for your account  # noqa: E501
        """
        pass

    def test_risk(self):
        """Test case for risk

        Get details for a risk in the platform  # noqa: E501
        """
        pass

    def test_risks(self):
        """Test case for risks

        Get a list of active risks for your account  # noqa: E501
        """
        pass

    def test_vendor_questionnaire_risks(self):
        """Test case for vendor_questionnaire_risks

        Get a list of questionnaire risks for one or more watched vendors or a specific questionnaire  # noqa: E501
        """
        pass

    def test_vendor_questionnaire_risks_v2(self):
        """Test case for vendor_questionnaire_risks_v2

        (V2) Get a list of questionnaire risks for one or more watched vendors or a specific questionnaire  # noqa: E501
        """
        pass

    def test_vendor_risks(self):
        """Test case for vendor_risks

        Get a list of active risks for a vendor  # noqa: E501
        """
        pass

    def test_vendor_risks_diff(self):
        """Test case for vendor_risks_diff

        Get a list of risk changes for a vendor  # noqa: E501
        """
        pass

    def test_vendors_risks_diff(self):
        """Test case for vendors_risks_diff

        Get a list of risk changes for monitored vendors  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
