# coding: utf-8

"""
    UpGuard CyberRisk API

    Access information from the CyberRisk platform programmatically using this API.  You can find or generate an API key to access this API in your CyberRisk Account Settings. Please authorize all requests by setting the \"Authorization\" header to your api key.  The base url for all public endpoints is https://cyber-risk.upguard.com/api/public  # noqa: E501

    OpenAPI spec version: 1.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from upguard.configuration import Configuration


class SummaryDiff(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'category': 'str',
        'cloudscan_diffs': 'Diffs',
        'description': 'str',
        'group': 'str',
        'id': 'str',
        'name': 'str',
        'risk_subtype': 'str',
        'risk_type': 'str',
        'severity': 'Severity',
        'severity_name': 'str',
        'vendor_diff': 'VendorDiff'
    }

    attribute_map = {
        'category': 'category',
        'cloudscan_diffs': 'cloudscanDiffs',
        'description': 'description',
        'group': 'group',
        'id': 'id',
        'name': 'name',
        'risk_subtype': 'riskSubtype',
        'risk_type': 'riskType',
        'severity': 'severity',
        'severity_name': 'severityName',
        'vendor_diff': 'vendorDiff'
    }

    def __init__(self, category=None, cloudscan_diffs=None, description=None, group=None, id=None, name=None, risk_subtype=None, risk_type=None, severity=None, severity_name=None, vendor_diff=None, _configuration=None):  # noqa: E501
        """SummaryDiff - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._category = None
        self._cloudscan_diffs = None
        self._description = None
        self._group = None
        self._id = None
        self._name = None
        self._risk_subtype = None
        self._risk_type = None
        self._severity = None
        self._severity_name = None
        self._vendor_diff = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if cloudscan_diffs is not None:
            self.cloudscan_diffs = cloudscan_diffs
        if description is not None:
            self.description = description
        if group is not None:
            self.group = group
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if risk_subtype is not None:
            self.risk_subtype = risk_subtype
        if risk_type is not None:
            self.risk_type = risk_type
        if severity is not None:
            self.severity = severity
        if severity_name is not None:
            self.severity_name = severity_name
        if vendor_diff is not None:
            self.vendor_diff = vendor_diff

    @property
    def category(self):
        """Gets the category of this SummaryDiff.  # noqa: E501

        The category of the risk group  # noqa: E501

        :return: The category of this SummaryDiff.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SummaryDiff.

        The category of the risk group  # noqa: E501

        :param category: The category of this SummaryDiff.  # noqa: E501
        :type: str
        """
        allowed_values = ["website_sec", "email_sec", "network_sec", "phishing", "brand_protect", "questionnaire_risks", "vulns", "typosquatting", "emailexposures", "dataleaks", "additional_evidence"]  # noqa: E501
        if (self._configuration.client_side_validation and
                category not in allowed_values):
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def cloudscan_diffs(self):
        """Gets the cloudscan_diffs of this SummaryDiff.  # noqa: E501


        :return: The cloudscan_diffs of this SummaryDiff.  # noqa: E501
        :rtype: Diffs
        """
        return self._cloudscan_diffs

    @cloudscan_diffs.setter
    def cloudscan_diffs(self, cloudscan_diffs):
        """Sets the cloudscan_diffs of this SummaryDiff.


        :param cloudscan_diffs: The cloudscan_diffs of this SummaryDiff.  # noqa: E501
        :type: Diffs
        """

        self._cloudscan_diffs = cloudscan_diffs

    @property
    def description(self):
        """Gets the description of this SummaryDiff.  # noqa: E501

        Description of the risk  # noqa: E501

        :return: The description of this SummaryDiff.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SummaryDiff.

        Description of the risk  # noqa: E501

        :param description: The description of this SummaryDiff.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def group(self):
        """Gets the group of this SummaryDiff.  # noqa: E501

        The ID of the risk class  # noqa: E501

        :return: The group of this SummaryDiff.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this SummaryDiff.

        The ID of the risk class  # noqa: E501

        :param group: The group of this SummaryDiff.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def id(self):
        """Gets the id of this SummaryDiff.  # noqa: E501

        The ID of risk  # noqa: E501

        :return: The id of this SummaryDiff.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SummaryDiff.

        The ID of risk  # noqa: E501

        :param id: The id of this SummaryDiff.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SummaryDiff.  # noqa: E501

        The name of the risk  # noqa: E501

        :return: The name of this SummaryDiff.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SummaryDiff.

        The name of the risk  # noqa: E501

        :param name: The name of this SummaryDiff.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def risk_subtype(self):
        """Gets the risk_subtype of this SummaryDiff.  # noqa: E501

        The subtype of the risk, e.g. the subtype of the verified_vuln:CVE-2021-34473 is CVE-2021-34473. This field will be empty if the risk has no subtype, e.g. for wp_version_exposed, or for generic risks like verified_vuln:* where the subtype is only determined when the full risk is specified.  # noqa: E501

        :return: The risk_subtype of this SummaryDiff.  # noqa: E501
        :rtype: str
        """
        return self._risk_subtype

    @risk_subtype.setter
    def risk_subtype(self, risk_subtype):
        """Sets the risk_subtype of this SummaryDiff.

        The subtype of the risk, e.g. the subtype of the verified_vuln:CVE-2021-34473 is CVE-2021-34473. This field will be empty if the risk has no subtype, e.g. for wp_version_exposed, or for generic risks like verified_vuln:* where the subtype is only determined when the full risk is specified.  # noqa: E501

        :param risk_subtype: The risk_subtype of this SummaryDiff.  # noqa: E501
        :type: str
        """

        self._risk_subtype = risk_subtype

    @property
    def risk_type(self):
        """Gets the risk_type of this SummaryDiff.  # noqa: E501

        The type of the risk, e.g. the type of the verified_vuln:CVE-2021-34473 is verified_vuln  # noqa: E501

        :return: The risk_type of this SummaryDiff.  # noqa: E501
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        """Sets the risk_type of this SummaryDiff.

        The type of the risk, e.g. the type of the verified_vuln:CVE-2021-34473 is verified_vuln  # noqa: E501

        :param risk_type: The risk_type of this SummaryDiff.  # noqa: E501
        :type: str
        """

        self._risk_type = risk_type

    @property
    def severity(self):
        """Gets the severity of this SummaryDiff.  # noqa: E501


        :return: The severity of this SummaryDiff.  # noqa: E501
        :rtype: Severity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this SummaryDiff.


        :param severity: The severity of this SummaryDiff.  # noqa: E501
        :type: Severity
        """

        self._severity = severity

    @property
    def severity_name(self):
        """Gets the severity_name of this SummaryDiff.  # noqa: E501

        The severity of the risks in human-readable form  # noqa: E501

        :return: The severity_name of this SummaryDiff.  # noqa: E501
        :rtype: str
        """
        return self._severity_name

    @severity_name.setter
    def severity_name(self, severity_name):
        """Sets the severity_name of this SummaryDiff.

        The severity of the risks in human-readable form  # noqa: E501

        :param severity_name: The severity_name of this SummaryDiff.  # noqa: E501
        :type: str
        """
        allowed_values = ["pass", "info", "low", "medium", "high", "critical"]  # noqa: E501
        if (self._configuration.client_side_validation and
                severity_name not in allowed_values):
            raise ValueError(
                "Invalid value for `severity_name` ({0}), must be one of {1}"  # noqa: E501
                .format(severity_name, allowed_values)
            )

        self._severity_name = severity_name

    @property
    def vendor_diff(self):
        """Gets the vendor_diff of this SummaryDiff.  # noqa: E501


        :return: The vendor_diff of this SummaryDiff.  # noqa: E501
        :rtype: VendorDiff
        """
        return self._vendor_diff

    @vendor_diff.setter
    def vendor_diff(self, vendor_diff):
        """Sets the vendor_diff of this SummaryDiff.


        :param vendor_diff: The vendor_diff of this SummaryDiff.  # noqa: E501
        :type: VendorDiff
        """

        self._vendor_diff = vendor_diff

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SummaryDiff, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SummaryDiff):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SummaryDiff):
            return True

        return self.to_dict() != other.to_dict()
