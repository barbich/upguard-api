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
from upguard.models.get_org_vulnerabilities_v1_resp_body import GetOrgVulnerabilitiesV1RespBody  # noqa: E501
from upguard.rest import ApiException


class TestGetOrgVulnerabilitiesV1RespBody(unittest.TestCase):
    """GetOrgVulnerabilitiesV1RespBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetOrgVulnerabilitiesV1RespBody(self):
        """Test GetOrgVulnerabilitiesV1RespBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = upguard.models.get_org_vulnerabilities_v1_resp_body.GetOrgVulnerabilitiesV1RespBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
