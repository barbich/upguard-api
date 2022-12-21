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


class TyposquatDomain(object):
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
        'added_at': 'datetime',
        'domain': 'str',
        'last_scanned_at': 'datetime',
        'num_registered': 'int',
        'num_unregistered': 'int',
        'primary_domain': 'bool'
    }

    attribute_map = {
        'added_at': 'added_at',
        'domain': 'domain',
        'last_scanned_at': 'last_scanned_at',
        'num_registered': 'num_registered',
        'num_unregistered': 'num_unregistered',
        'primary_domain': 'primary_domain'
    }

    def __init__(self, added_at=None, domain=None, last_scanned_at=None, num_registered=None, num_unregistered=None, primary_domain=None, _configuration=None):  # noqa: E501
        """TyposquatDomain - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._added_at = None
        self._domain = None
        self._last_scanned_at = None
        self._num_registered = None
        self._num_unregistered = None
        self._primary_domain = None
        self.discriminator = None

        if added_at is not None:
            self.added_at = added_at
        if domain is not None:
            self.domain = domain
        if last_scanned_at is not None:
            self.last_scanned_at = last_scanned_at
        if num_registered is not None:
            self.num_registered = num_registered
        if num_unregistered is not None:
            self.num_unregistered = num_unregistered
        if primary_domain is not None:
            self.primary_domain = primary_domain

    @property
    def added_at(self):
        """Gets the added_at of this TyposquatDomain.  # noqa: E501

        The date the domain was added to typosquatting in RFC3339 format.  # noqa: E501

        :return: The added_at of this TyposquatDomain.  # noqa: E501
        :rtype: datetime
        """
        return self._added_at

    @added_at.setter
    def added_at(self, added_at):
        """Sets the added_at of this TyposquatDomain.

        The date the domain was added to typosquatting in RFC3339 format.  # noqa: E501

        :param added_at: The added_at of this TyposquatDomain.  # noqa: E501
        :type: datetime
        """

        self._added_at = added_at

    @property
    def domain(self):
        """Gets the domain of this TyposquatDomain.  # noqa: E501

        The typosquat domain  # noqa: E501

        :return: The domain of this TyposquatDomain.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this TyposquatDomain.

        The typosquat domain  # noqa: E501

        :param domain: The domain of this TyposquatDomain.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def last_scanned_at(self):
        """Gets the last_scanned_at of this TyposquatDomain.  # noqa: E501

        The date of last scan for this domain in RFC3339 format. Absent if the domain has never been scanned.  # noqa: E501

        :return: The last_scanned_at of this TyposquatDomain.  # noqa: E501
        :rtype: datetime
        """
        return self._last_scanned_at

    @last_scanned_at.setter
    def last_scanned_at(self, last_scanned_at):
        """Sets the last_scanned_at of this TyposquatDomain.

        The date of last scan for this domain in RFC3339 format. Absent if the domain has never been scanned.  # noqa: E501

        :param last_scanned_at: The last_scanned_at of this TyposquatDomain.  # noqa: E501
        :type: datetime
        """

        self._last_scanned_at = last_scanned_at

    @property
    def num_registered(self):
        """Gets the num_registered of this TyposquatDomain.  # noqa: E501

        The number of registered permutations for this domain  # noqa: E501

        :return: The num_registered of this TyposquatDomain.  # noqa: E501
        :rtype: int
        """
        return self._num_registered

    @num_registered.setter
    def num_registered(self, num_registered):
        """Sets the num_registered of this TyposquatDomain.

        The number of registered permutations for this domain  # noqa: E501

        :param num_registered: The num_registered of this TyposquatDomain.  # noqa: E501
        :type: int
        """

        self._num_registered = num_registered

    @property
    def num_unregistered(self):
        """Gets the num_unregistered of this TyposquatDomain.  # noqa: E501

        The number of unregistered permutations for this domain  # noqa: E501

        :return: The num_unregistered of this TyposquatDomain.  # noqa: E501
        :rtype: int
        """
        return self._num_unregistered

    @num_unregistered.setter
    def num_unregistered(self, num_unregistered):
        """Sets the num_unregistered of this TyposquatDomain.

        The number of unregistered permutations for this domain  # noqa: E501

        :param num_unregistered: The num_unregistered of this TyposquatDomain.  # noqa: E501
        :type: int
        """

        self._num_unregistered = num_unregistered

    @property
    def primary_domain(self):
        """Gets the primary_domain of this TyposquatDomain.  # noqa: E501

        Flag indicating whether the domain is the primary domain for the account  # noqa: E501

        :return: The primary_domain of this TyposquatDomain.  # noqa: E501
        :rtype: bool
        """
        return self._primary_domain

    @primary_domain.setter
    def primary_domain(self, primary_domain):
        """Sets the primary_domain of this TyposquatDomain.

        Flag indicating whether the domain is the primary domain for the account  # noqa: E501

        :param primary_domain: The primary_domain of this TyposquatDomain.  # noqa: E501
        :type: bool
        """

        self._primary_domain = primary_domain

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
        if issubclass(TyposquatDomain, dict):
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
        if not isinstance(other, TyposquatDomain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TyposquatDomain):
            return True

        return self.to_dict() != other.to_dict()