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


class Domain(object):
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
        'primary_domain': 'bool',
        'scanned_at': 'datetime'
    }

    attribute_map = {
        'active': 'active',
        'automated_score': 'automated_score',
        'hostname': 'hostname',
        'labels': 'labels',
        'primary_domain': 'primary_domain',
        'scanned_at': 'scanned_at'
    }

    def __init__(self, active=None, automated_score=None, hostname=None, labels=None, primary_domain=None, scanned_at=None, _configuration=None):  # noqa: E501
        """Domain - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._automated_score = None
        self._hostname = None
        self._labels = None
        self._primary_domain = None
        self._scanned_at = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if automated_score is not None:
            self.automated_score = automated_score
        if hostname is not None:
            self.hostname = hostname
        if labels is not None:
            self.labels = labels
        if primary_domain is not None:
            self.primary_domain = primary_domain
        if scanned_at is not None:
            self.scanned_at = scanned_at

    @property
    def active(self):
        """Gets the active of this Domain.  # noqa: E501

        The status of the domain  # noqa: E501

        :return: The active of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Domain.

        The status of the domain  # noqa: E501

        :param active: The active of this Domain.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def automated_score(self):
        """Gets the automated_score of this Domain.  # noqa: E501

        The score of the domain. If the domain is active or hasn't been scanned yet this field will be absent  # noqa: E501

        :return: The automated_score of this Domain.  # noqa: E501
        :rtype: int
        """
        return self._automated_score

    @automated_score.setter
    def automated_score(self, automated_score):
        """Sets the automated_score of this Domain.

        The score of the domain. If the domain is active or hasn't been scanned yet this field will be absent  # noqa: E501

        :param automated_score: The automated_score of this Domain.  # noqa: E501
        :type: int
        """

        self._automated_score = automated_score

    @property
    def hostname(self):
        """Gets the hostname of this Domain.  # noqa: E501

        The hostname  # noqa: E501

        :return: The hostname of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Domain.

        The hostname  # noqa: E501

        :param hostname: The hostname of this Domain.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def labels(self):
        """Gets the labels of this Domain.  # noqa: E501

        The labels associated with the domain  # noqa: E501

        :return: The labels of this Domain.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Domain.

        The labels associated with the domain  # noqa: E501

        :param labels: The labels of this Domain.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def primary_domain(self):
        """Gets the primary_domain of this Domain.  # noqa: E501

        Flag indicating the primary domain for the account  # noqa: E501

        :return: The primary_domain of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._primary_domain

    @primary_domain.setter
    def primary_domain(self, primary_domain):
        """Sets the primary_domain of this Domain.

        Flag indicating the primary domain for the account  # noqa: E501

        :param primary_domain: The primary_domain of this Domain.  # noqa: E501
        :type: bool
        """

        self._primary_domain = primary_domain

    @property
    def scanned_at(self):
        """Gets the scanned_at of this Domain.  # noqa: E501

        The time the domain was scanned. If the domain is inactive or hasn't been scanned yet this field will be absent  # noqa: E501

        :return: The scanned_at of this Domain.  # noqa: E501
        :rtype: datetime
        """
        return self._scanned_at

    @scanned_at.setter
    def scanned_at(self, scanned_at):
        """Sets the scanned_at of this Domain.

        The time the domain was scanned. If the domain is inactive or hasn't been scanned yet this field will be absent  # noqa: E501

        :param scanned_at: The scanned_at of this Domain.  # noqa: E501
        :type: datetime
        """

        self._scanned_at = scanned_at

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
        if issubclass(Domain, dict):
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
        if not isinstance(other, Domain):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Domain):
            return True

        return self.to_dict() != other.to_dict()