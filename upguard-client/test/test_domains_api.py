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
from upguard.api.domains_api import DomainsApi  # noqa: E501
from upguard.rest import ApiException


class TestDomainsApi(unittest.TestCase):
    """DomainsApi unit test stubs"""

    def setUp(self):
        self.api = upguard.api.domains_api.DomainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_custom_domains(self):
        """Test case for add_custom_domains

        Add custom domains  # noqa: E501
        """
        pass

    def test_domain_details(self):
        """Test case for domain_details

        Retrieve details for a domain  # noqa: E501
        """
        pass

    def test_domain_update_labels(self):
        """Test case for domain_update_labels

        Assign labels to a domain  # noqa: E501
        """
        pass

    def test_domains(self):
        """Test case for domains

        Get a list of domains  # noqa: E501
        """
        pass

    def test_remove_custom_domains(self):
        """Test case for remove_custom_domains

        Remove custom domains  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()