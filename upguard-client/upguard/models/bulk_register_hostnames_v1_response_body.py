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


class BulkRegisterHostnamesV1ResponseBody(object):
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
        'registered': 'int',
        'remaining': 'int'
    }

    attribute_map = {
        'registered': 'registered',
        'remaining': 'remaining'
    }

    def __init__(self, registered=None, remaining=None, _configuration=None):  # noqa: E501
        """BulkRegisterHostnamesV1ResponseBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._registered = None
        self._remaining = None
        self.discriminator = None

        if registered is not None:
            self.registered = registered
        if remaining is not None:
            self.remaining = remaining

    @property
    def registered(self):
        """Gets the registered of this BulkRegisterHostnamesV1ResponseBody.  # noqa: E501

        The number of newly registered hostnames.  # noqa: E501

        :return: The registered of this BulkRegisterHostnamesV1ResponseBody.  # noqa: E501
        :rtype: int
        """
        return self._registered

    @registered.setter
    def registered(self, registered):
        """Sets the registered of this BulkRegisterHostnamesV1ResponseBody.

        The number of newly registered hostnames.  # noqa: E501

        :param registered: The registered of this BulkRegisterHostnamesV1ResponseBody.  # noqa: E501
        :type: int
        """

        self._registered = registered

    @property
    def remaining(self):
        """Gets the remaining of this BulkRegisterHostnamesV1ResponseBody.  # noqa: E501

        The number of remaining slots.  # noqa: E501

        :return: The remaining of this BulkRegisterHostnamesV1ResponseBody.  # noqa: E501
        :rtype: int
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """Sets the remaining of this BulkRegisterHostnamesV1ResponseBody.

        The number of remaining slots.  # noqa: E501

        :param remaining: The remaining of this BulkRegisterHostnamesV1ResponseBody.  # noqa: E501
        :type: int
        """

        self._remaining = remaining

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
        if issubclass(BulkRegisterHostnamesV1ResponseBody, dict):
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
        if not isinstance(other, BulkRegisterHostnamesV1ResponseBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BulkRegisterHostnamesV1ResponseBody):
            return True

        return self.to_dict() != other.to_dict()
