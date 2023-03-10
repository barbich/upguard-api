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


class ScanDiff(object):
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
        'expected': 'str',
        'hostname': 'str',
        '_property': 'str',
        'scan_a': 'ScanResult',
        'scan_b': 'ScanResult'
    }

    attribute_map = {
        'expected': 'expected',
        'hostname': 'hostname',
        '_property': 'property',
        'scan_a': 'scanA',
        'scan_b': 'scanB'
    }

    def __init__(self, expected=None, hostname=None, _property=None, scan_a=None, scan_b=None, _configuration=None):  # noqa: E501
        """ScanDiff - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._expected = None
        self._hostname = None
        self.__property = None
        self._scan_a = None
        self._scan_b = None
        self.discriminator = None

        if expected is not None:
            self.expected = expected
        if hostname is not None:
            self.hostname = hostname
        if _property is not None:
            self._property = _property
        if scan_a is not None:
            self.scan_a = scan_a
        if scan_b is not None:
            self.scan_b = scan_b

    @property
    def expected(self):
        """Gets the expected of this ScanDiff.  # noqa: E501

        The expected status  # noqa: E501

        :return: The expected of this ScanDiff.  # noqa: E501
        :rtype: str
        """
        return self._expected

    @expected.setter
    def expected(self, expected):
        """Sets the expected of this ScanDiff.

        The expected status  # noqa: E501

        :param expected: The expected of this ScanDiff.  # noqa: E501
        :type: str
        """

        self._expected = expected

    @property
    def hostname(self):
        """Gets the hostname of this ScanDiff.  # noqa: E501

        The domain name or IP address experiencing the risk diff  # noqa: E501

        :return: The hostname of this ScanDiff.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ScanDiff.

        The domain name or IP address experiencing the risk diff  # noqa: E501

        :param hostname: The hostname of this ScanDiff.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def _property(self):
        """Gets the _property of this ScanDiff.  # noqa: E501

        The property checked  # noqa: E501

        :return: The _property of this ScanDiff.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this ScanDiff.

        The property checked  # noqa: E501

        :param _property: The _property of this ScanDiff.  # noqa: E501
        :type: str
        """

        self.__property = _property

    @property
    def scan_a(self):
        """Gets the scan_a of this ScanDiff.  # noqa: E501


        :return: The scan_a of this ScanDiff.  # noqa: E501
        :rtype: ScanResult
        """
        return self._scan_a

    @scan_a.setter
    def scan_a(self, scan_a):
        """Sets the scan_a of this ScanDiff.


        :param scan_a: The scan_a of this ScanDiff.  # noqa: E501
        :type: ScanResult
        """

        self._scan_a = scan_a

    @property
    def scan_b(self):
        """Gets the scan_b of this ScanDiff.  # noqa: E501


        :return: The scan_b of this ScanDiff.  # noqa: E501
        :rtype: ScanResult
        """
        return self._scan_b

    @scan_b.setter
    def scan_b(self, scan_b):
        """Sets the scan_b of this ScanDiff.


        :param scan_b: The scan_b of this ScanDiff.  # noqa: E501
        :type: ScanResult
        """

        self._scan_b = scan_b

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
        if issubclass(ScanDiff, dict):
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
        if not isinstance(other, ScanDiff):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScanDiff):
            return True

        return self.to_dict() != other.to_dict()
