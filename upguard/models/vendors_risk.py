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


class VendorsRisk(object):
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
        'description': 'str',
        'finding': 'str',
        'id': 'str',
        'risk_subtype': 'str',
        'risk_type': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'finding': 'finding',
        'id': 'id',
        'risk_subtype': 'riskSubtype',
        'risk_type': 'riskType',
        'severity': 'severity'
    }

    def __init__(self, category=None, description=None, finding=None, id=None, risk_subtype=None, risk_type=None, severity=None, _configuration=None):  # noqa: E501
        """VendorsRisk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._category = None
        self._description = None
        self._finding = None
        self._id = None
        self._risk_subtype = None
        self._risk_type = None
        self._severity = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if finding is not None:
            self.finding = finding
        if id is not None:
            self.id = id
        if risk_subtype is not None:
            self.risk_subtype = risk_subtype
        if risk_type is not None:
            self.risk_type = risk_type
        if severity is not None:
            self.severity = severity

    @property
    def category(self):
        """Gets the category of this VendorsRisk.  # noqa: E501

        The risk category identifier  # noqa: E501

        :return: The category of this VendorsRisk.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this VendorsRisk.

        The risk category identifier  # noqa: E501

        :param category: The category of this VendorsRisk.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this VendorsRisk.  # noqa: E501

        Description of the risk  # noqa: E501

        :return: The description of this VendorsRisk.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VendorsRisk.

        Description of the risk  # noqa: E501

        :param description: The description of this VendorsRisk.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def finding(self):
        """Gets the finding of this VendorsRisk.  # noqa: E501

        A short description of the finding  # noqa: E501

        :return: The finding of this VendorsRisk.  # noqa: E501
        :rtype: str
        """
        return self._finding

    @finding.setter
    def finding(self, finding):
        """Sets the finding of this VendorsRisk.

        A short description of the finding  # noqa: E501

        :param finding: The finding of this VendorsRisk.  # noqa: E501
        :type: str
        """

        self._finding = finding

    @property
    def id(self):
        """Gets the id of this VendorsRisk.  # noqa: E501

        The risk identifier  # noqa: E501

        :return: The id of this VendorsRisk.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VendorsRisk.

        The risk identifier  # noqa: E501

        :param id: The id of this VendorsRisk.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def risk_subtype(self):
        """Gets the risk_subtype of this VendorsRisk.  # noqa: E501

        The subtype of the risk, e.g. the subtype of the verified_vuln:CVE-2021-34473 is CVE-2021-34473. This field will be empty if the risk has no subtype, e.g. for wp_version_exposed, or for generic risks like verified_vuln:* where the subtype is only determined when the full risk is specified.  # noqa: E501

        :return: The risk_subtype of this VendorsRisk.  # noqa: E501
        :rtype: str
        """
        return self._risk_subtype

    @risk_subtype.setter
    def risk_subtype(self, risk_subtype):
        """Sets the risk_subtype of this VendorsRisk.

        The subtype of the risk, e.g. the subtype of the verified_vuln:CVE-2021-34473 is CVE-2021-34473. This field will be empty if the risk has no subtype, e.g. for wp_version_exposed, or for generic risks like verified_vuln:* where the subtype is only determined when the full risk is specified.  # noqa: E501

        :param risk_subtype: The risk_subtype of this VendorsRisk.  # noqa: E501
        :type: str
        """

        self._risk_subtype = risk_subtype

    @property
    def risk_type(self):
        """Gets the risk_type of this VendorsRisk.  # noqa: E501

        The type of the risk, e.g. the type of the verified_vuln:CVE-2021-34473 is verified_vuln  # noqa: E501

        :return: The risk_type of this VendorsRisk.  # noqa: E501
        :rtype: str
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        """Sets the risk_type of this VendorsRisk.

        The type of the risk, e.g. the type of the verified_vuln:CVE-2021-34473 is verified_vuln  # noqa: E501

        :param risk_type: The risk_type of this VendorsRisk.  # noqa: E501
        :type: str
        """

        self._risk_type = risk_type

    @property
    def severity(self):
        """Gets the severity of this VendorsRisk.  # noqa: E501

        The risk severity  # noqa: E501

        :return: The severity of this VendorsRisk.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this VendorsRisk.

        The risk severity  # noqa: E501

        :param severity: The severity of this VendorsRisk.  # noqa: E501
        :type: str
        """

        self._severity = severity

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
        if issubclass(VendorsRisk, dict):
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
        if not isinstance(other, VendorsRisk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VendorsRisk):
            return True

        return self.to_dict() != other.to_dict()
