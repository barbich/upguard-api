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


class IP(object):
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
        'as_name': 'str',
        'asn': 'int',
        'automated_score': 'int',
        'country': 'str',
        'ip': 'str',
        'labels': 'list[str]',
        'owner': 'str',
        'services': 'list[str]',
        'sources': 'list[IPSource]'
    }

    attribute_map = {
        'as_name': 'as_name',
        'asn': 'asn',
        'automated_score': 'automated_score',
        'country': 'country',
        'ip': 'ip',
        'labels': 'labels',
        'owner': 'owner',
        'services': 'services',
        'sources': 'sources'
    }

    def __init__(self, as_name=None, asn=None, automated_score=None, country=None, ip=None, labels=None, owner=None, services=None, sources=None, _configuration=None):  # noqa: E501
        """IP - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._as_name = None
        self._asn = None
        self._automated_score = None
        self._country = None
        self._ip = None
        self._labels = None
        self._owner = None
        self._services = None
        self._sources = None
        self.discriminator = None

        if as_name is not None:
            self.as_name = as_name
        if asn is not None:
            self.asn = asn
        if automated_score is not None:
            self.automated_score = automated_score
        if country is not None:
            self.country = country
        if ip is not None:
            self.ip = ip
        if labels is not None:
            self.labels = labels
        if owner is not None:
            self.owner = owner
        if services is not None:
            self.services = services
        if sources is not None:
            self.sources = sources

    @property
    def as_name(self):
        """Gets the as_name of this IP.  # noqa: E501

        The name of the AS the IP belongs to. If no AS is available for an IP this field will be omitted.  # noqa: E501

        :return: The as_name of this IP.  # noqa: E501
        :rtype: str
        """
        return self._as_name

    @as_name.setter
    def as_name(self, as_name):
        """Sets the as_name of this IP.

        The name of the AS the IP belongs to. If no AS is available for an IP this field will be omitted.  # noqa: E501

        :param as_name: The as_name of this IP.  # noqa: E501
        :type: str
        """

        self._as_name = as_name

    @property
    def asn(self):
        """Gets the asn of this IP.  # noqa: E501

        The ASN the IP belongs to. If no ASN is available for an IP this field will be omitted.  # noqa: E501

        :return: The asn of this IP.  # noqa: E501
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this IP.

        The ASN the IP belongs to. If no ASN is available for an IP this field will be omitted.  # noqa: E501

        :param asn: The asn of this IP.  # noqa: E501
        :type: int
        """

        self._asn = asn

    @property
    def automated_score(self):
        """Gets the automated_score of this IP.  # noqa: E501

        The score of the ip. If the ip is inactive or hasn't been scanned yet this field will be absent  # noqa: E501

        :return: The automated_score of this IP.  # noqa: E501
        :rtype: int
        """
        return self._automated_score

    @automated_score.setter
    def automated_score(self, automated_score):
        """Sets the automated_score of this IP.

        The score of the ip. If the ip is inactive or hasn't been scanned yet this field will be absent  # noqa: E501

        :param automated_score: The automated_score of this IP.  # noqa: E501
        :type: int
        """

        self._automated_score = automated_score

    @property
    def country(self):
        """Gets the country of this IP.  # noqa: E501

        The country the IP belongs to. If no country is available for an IP this field will be omitted.  # noqa: E501

        :return: The country of this IP.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this IP.

        The country the IP belongs to. If no country is available for an IP this field will be omitted.  # noqa: E501

        :param country: The country of this IP.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def ip(self):
        """Gets the ip of this IP.  # noqa: E501

        The IP.  # noqa: E501

        :return: The ip of this IP.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IP.

        The IP.  # noqa: E501

        :param ip: The ip of this IP.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def labels(self):
        """Gets the labels of this IP.  # noqa: E501

        The labels associated with the IP.  # noqa: E501

        :return: The labels of this IP.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this IP.

        The labels associated with the IP.  # noqa: E501

        :param labels: The labels of this IP.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def owner(self):
        """Gets the owner of this IP.  # noqa: E501

        The owner of the IP.  # noqa: E501

        :return: The owner of this IP.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this IP.

        The owner of the IP.  # noqa: E501

        :param owner: The owner of this IP.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def services(self):
        """Gets the services of this IP.  # noqa: E501

        The list of discovered services IP. If no services were detected for the IP this field will be omitted.  # noqa: E501

        :return: The services of this IP.  # noqa: E501
        :rtype: list[str]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this IP.

        The list of discovered services IP. If no services were detected for the IP this field will be omitted.  # noqa: E501

        :param services: The services of this IP.  # noqa: E501
        :type: list[str]
        """

        self._services = services

    @property
    def sources(self):
        """Gets the sources of this IP.  # noqa: E501

        The sources of the IP.  # noqa: E501

        :return: The sources of this IP.  # noqa: E501
        :rtype: list[IPSource]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this IP.

        The sources of the IP.  # noqa: E501

        :param sources: The sources of this IP.  # noqa: E501
        :type: list[IPSource]
        """

        self._sources = sources

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
        if issubclass(IP, dict):
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
        if not isinstance(other, IP):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IP):
            return True

        return self.to_dict() != other.to_dict()
