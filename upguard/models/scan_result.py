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


class ScanResult(object):
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
        '_date': 'datetime',
        'meta_value': 'str',
        'status': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'meta_value': 'metaValue',
        'status': 'status'
    }

    def __init__(self, _date=None, meta_value=None, status=None, _configuration=None):  # noqa: E501
        """ScanResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__date = None
        self._meta_value = None
        self._status = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if meta_value is not None:
            self.meta_value = meta_value
        if status is not None:
            self.status = status

    @property
    def _date(self):
        """Gets the _date of this ScanResult.  # noqa: E501

        The date of the scan (RFC 3339 format)  # noqa: E501

        :return: The _date of this ScanResult.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ScanResult.

        The date of the scan (RFC 3339 format)  # noqa: E501

        :param _date: The _date of this ScanResult.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def meta_value(self):
        """Gets the meta_value of this ScanResult.  # noqa: E501

        Metadata for the result of the check  # noqa: E501

        :return: The meta_value of this ScanResult.  # noqa: E501
        :rtype: str
        """
        return self._meta_value

    @meta_value.setter
    def meta_value(self, meta_value):
        """Sets the meta_value of this ScanResult.

        Metadata for the result of the check  # noqa: E501

        :param meta_value: The meta_value of this ScanResult.  # noqa: E501
        :type: str
        """

        self._meta_value = meta_value

    @property
    def status(self):
        """Gets the status of this ScanResult.  # noqa: E501

        The check status after the automated scan  # noqa: E501

        :return: The status of this ScanResult.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScanResult.

        The check status after the automated scan  # noqa: E501

        :param status: The status of this ScanResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASS", "FAIL", "UNKNOWN", "WAIVED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(ScanResult, dict):
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
        if not isinstance(other, ScanResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScanResult):
            return True

        return self.to_dict() != other.to_dict()