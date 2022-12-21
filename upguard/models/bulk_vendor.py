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


class BulkVendor(object):
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
        'id': 'int',
        'name': 'str',
        'primary_hostname': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'primary_hostname': 'primary_hostname'
    }

    def __init__(self, id=None, name=None, primary_hostname=None, _configuration=None):  # noqa: E501
        """BulkVendor - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._primary_hostname = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if primary_hostname is not None:
            self.primary_hostname = primary_hostname

    @property
    def id(self):
        """Gets the id of this BulkVendor.  # noqa: E501

        The ID of the vendor.  # noqa: E501

        :return: The id of this BulkVendor.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BulkVendor.

        The ID of the vendor.  # noqa: E501

        :param id: The id of this BulkVendor.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BulkVendor.  # noqa: E501

        The name of the vendor.  # noqa: E501

        :return: The name of this BulkVendor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BulkVendor.

        The name of the vendor.  # noqa: E501

        :param name: The name of this BulkVendor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def primary_hostname(self):
        """Gets the primary_hostname of this BulkVendor.  # noqa: E501

        The primary hostname of the vendor.  # noqa: E501

        :return: The primary_hostname of this BulkVendor.  # noqa: E501
        :rtype: str
        """
        return self._primary_hostname

    @primary_hostname.setter
    def primary_hostname(self, primary_hostname):
        """Sets the primary_hostname of this BulkVendor.

        The primary hostname of the vendor.  # noqa: E501

        :param primary_hostname: The primary_hostname of this BulkVendor.  # noqa: E501
        :type: str
        """

        self._primary_hostname = primary_hostname

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
        if issubclass(BulkVendor, dict):
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
        if not isinstance(other, BulkVendor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkVendor):
            return True

        return self.to_dict() != other.to_dict()