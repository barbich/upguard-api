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


class BulkHostname(object):
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
        'active': 'bool',
        'automated_score': 'int',
        'hostname': 'str',
        'labels': 'list[str]',
        'last_scanned_at': 'datetime',
        'risks': 'list[BulkRisk]',
        'vendor': 'BulkVendor'
    }

    attribute_map = {
        'active': 'active',
        'automated_score': 'automated_score',
        'hostname': 'hostname',
        'labels': 'labels',
        'last_scanned_at': 'last_scanned_at',
        'risks': 'risks',
        'vendor': 'vendor'
    }

    def __init__(self, active=None, automated_score=None, hostname=None, labels=None, last_scanned_at=None, risks=None, vendor=None, _configuration=None):  # noqa: E501
        """BulkHostname - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._automated_score = None
        self._hostname = None
        self._labels = None
        self._last_scanned_at = None
        self._risks = None
        self._vendor = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if automated_score is not None:
            self.automated_score = automated_score
        if hostname is not None:
            self.hostname = hostname
        if labels is not None:
            self.labels = labels
        if last_scanned_at is not None:
            self.last_scanned_at = last_scanned_at
        if risks is not None:
            self.risks = risks
        if vendor is not None:
            self.vendor = vendor

    @property
    def active(self):
        """Gets the active of this BulkHostname.  # noqa: E501

        The active state of the hostname. These will be omitted if the omit_scan_info query parameter is true.  # noqa: E501

        :return: The active of this BulkHostname.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this BulkHostname.

        The active state of the hostname. These will be omitted if the omit_scan_info query parameter is true.  # noqa: E501

        :param active: The active of this BulkHostname.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def automated_score(self):
        """Gets the automated_score of this BulkHostname.  # noqa: E501

        The automated score of the hostname. This will be omitted if the omit_scan_info query parameter is true.  # noqa: E501

        :return: The automated_score of this BulkHostname.  # noqa: E501
        :rtype: int
        """
        return self._automated_score

    @automated_score.setter
    def automated_score(self, automated_score):
        """Sets the automated_score of this BulkHostname.

        The automated score of the hostname. This will be omitted if the omit_scan_info query parameter is true.  # noqa: E501

        :param automated_score: The automated_score of this BulkHostname.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                automated_score is not None and automated_score > 950):  # noqa: E501
            raise ValueError("Invalid value for `automated_score`, must be a value less than or equal to `950`")  # noqa: E501
        if (self._configuration.client_side_validation and
                automated_score is not None and automated_score < 0):  # noqa: E501
            raise ValueError("Invalid value for `automated_score`, must be a value greater than or equal to `0`")  # noqa: E501

        self._automated_score = automated_score

    @property
    def hostname(self):
        """Gets the hostname of this BulkHostname.  # noqa: E501

        The name of the hostname.  # noqa: E501

        :return: The hostname of this BulkHostname.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this BulkHostname.

        The name of the hostname.  # noqa: E501

        :param hostname: The hostname of this BulkHostname.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def labels(self):
        """Gets the labels of this BulkHostname.  # noqa: E501

        The list of labels associated with the hostname. This will be omitted if the omit_labels query parameter is true.  # noqa: E501

        :return: The labels of this BulkHostname.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this BulkHostname.

        The list of labels associated with the hostname. This will be omitted if the omit_labels query parameter is true.  # noqa: E501

        :param labels: The labels of this BulkHostname.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def last_scanned_at(self):
        """Gets the last_scanned_at of this BulkHostname.  # noqa: E501

        The timestamp this hostname was last scanned at.  # noqa: E501

        :return: The last_scanned_at of this BulkHostname.  # noqa: E501
        :rtype: datetime
        """
        return self._last_scanned_at

    @last_scanned_at.setter
    def last_scanned_at(self, last_scanned_at):
        """Sets the last_scanned_at of this BulkHostname.

        The timestamp this hostname was last scanned at.  # noqa: E501

        :param last_scanned_at: The last_scanned_at of this BulkHostname.  # noqa: E501
        :type: datetime
        """

        self._last_scanned_at = last_scanned_at

    @property
    def risks(self):
        """Gets the risks of this BulkHostname.  # noqa: E501

        The list of risks associated with the hostname. These will be omitted if the omit_scan_info query parameter is true.  # noqa: E501

        :return: The risks of this BulkHostname.  # noqa: E501
        :rtype: list[BulkRisk]
        """
        return self._risks

    @risks.setter
    def risks(self, risks):
        """Sets the risks of this BulkHostname.

        The list of risks associated with the hostname. These will be omitted if the omit_scan_info query parameter is true.  # noqa: E501

        :param risks: The risks of this BulkHostname.  # noqa: E501
        :type: list[BulkRisk]
        """

        self._risks = risks

    @property
    def vendor(self):
        """Gets the vendor of this BulkHostname.  # noqa: E501


        :return: The vendor of this BulkHostname.  # noqa: E501
        :rtype: BulkVendor
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this BulkHostname.


        :param vendor: The vendor of this BulkHostname.  # noqa: E501
        :type: BulkVendor
        """

        self._vendor = vendor

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
        if issubclass(BulkHostname, dict):
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
        if not isinstance(other, BulkHostname):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkHostname):
            return True

        return self.to_dict() != other.to_dict()
