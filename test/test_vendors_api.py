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
from upguard.api.vendors_api import VendorsApi  # noqa: E501
from upguard.rest import ApiException


class TestVendorsApi(unittest.TestCase):
    """VendorsApi unit test stubs"""

    def setUp(self):
        self.api = upguard.api.vendors_api.VendorsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_additional_evidence(self):
        """Test case for additional_evidence

        Retrieve (one or more) vendor additional evidence documents by id  # noqa: E501
        """
        pass

    def test_additional_evidences_list(self):
        """Test case for additional_evidences_list

        List vendor additional evidence instances  # noqa: E501
        """
        pass

    def test_attachment(self):
        """Test case for attachment

        Retrieve (one or more) vendor questionnaire attachments by id  # noqa: E501
        """
        pass

    def test_attachments(self):
        """Test case for attachments

        List vendor questionnaire attachments  # noqa: E501
        """
        pass

    def test_document(self):
        """Test case for document

        Retrieve (one or more) vendor documents by id  # noqa: E501
        """
        pass

    def test_documents(self):
        """Test case for documents

        List vendor documents  # noqa: E501
        """
        pass

    def test_questionnaires(self):
        """Test case for questionnaires

        List vendor questionnaires  # noqa: E501
        """
        pass

    def test_questionnaires_v2(self):
        """Test case for questionnaires_v2

        List vendor questionnaires  # noqa: E501
        """
        pass

    def test_vendor(self):
        """Test case for vendor

        Get vendor details  # noqa: E501
        """
        pass

    def test_vendor_domain_details(self):
        """Test case for vendor_domain_details

        Retrieve details for a domain  # noqa: E501
        """
        pass

    def test_vendor_domain_update_labels(self):
        """Test case for vendor_domain_update_labels

        Assign labels to an domain  # noqa: E501
        """
        pass

    def test_vendor_domains(self):
        """Test case for vendor_domains

        List vendor domains  # noqa: E501
        """
        pass

    def test_vendor_ip_details(self):
        """Test case for vendor_ip_details

        Retrieve details for an IP address  # noqa: E501
        """
        pass

    def test_vendor_ip_update_labels(self):
        """Test case for vendor_ip_update_labels

        Assign labels to an IP  # noqa: E501
        """
        pass

    def test_vendor_ips(self):
        """Test case for vendor_ips

        List vendor ips  # noqa: E501
        """
        pass

    def test_vendor_ranges(self):
        """Test case for vendor_ranges

        List vendor ip ranges  # noqa: E501
        """
        pass

    def test_vendor_update_attributes(self):
        """Test case for vendor_update_attributes

        Assign or update the attributes for a vendor  # noqa: E501
        """
        pass

    def test_vendor_update_labels(self):
        """Test case for vendor_update_labels

        Assign labels to a vendor  # noqa: E501
        """
        pass

    def test_vendor_update_tier(self):
        """Test case for vendor_update_tier

        Assign tier to a vendor  # noqa: E501
        """
        pass

    def test_vendors(self):
        """Test case for vendors

        List monitored vendors  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
