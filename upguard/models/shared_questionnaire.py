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


class SharedQuestionnaire(object):
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
        'in_remediation': 'bool',
        'included_in_risk_profile': 'bool',
        'name': 'str',
        'published_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'in_remediation': 'in_remediation',
        'included_in_risk_profile': 'included_in_risk_profile',
        'name': 'name',
        'published_at': 'published_at'
    }

    def __init__(self, id=None, in_remediation=None, included_in_risk_profile=None, name=None, published_at=None, _configuration=None):  # noqa: E501
        """SharedQuestionnaire - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._in_remediation = None
        self._included_in_risk_profile = None
        self._name = None
        self._published_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if in_remediation is not None:
            self.in_remediation = in_remediation
        if included_in_risk_profile is not None:
            self.included_in_risk_profile = included_in_risk_profile
        if name is not None:
            self.name = name
        if published_at is not None:
            self.published_at = published_at

    @property
    def id(self):
        """Gets the id of this SharedQuestionnaire.  # noqa: E501

        The id of the questionnaire.  # noqa: E501

        :return: The id of this SharedQuestionnaire.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SharedQuestionnaire.

        The id of the questionnaire.  # noqa: E501

        :param id: The id of this SharedQuestionnaire.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def in_remediation(self):
        """Gets the in_remediation of this SharedQuestionnaire.  # noqa: E501

        Flag indicating whether there are risks under remediation in this questionnaire  # noqa: E501

        :return: The in_remediation of this SharedQuestionnaire.  # noqa: E501
        :rtype: bool
        """
        return self._in_remediation

    @in_remediation.setter
    def in_remediation(self, in_remediation):
        """Sets the in_remediation of this SharedQuestionnaire.

        Flag indicating whether there are risks under remediation in this questionnaire  # noqa: E501

        :param in_remediation: The in_remediation of this SharedQuestionnaire.  # noqa: E501
        :type: bool
        """

        self._in_remediation = in_remediation

    @property
    def included_in_risk_profile(self):
        """Gets the included_in_risk_profile of this SharedQuestionnaire.  # noqa: E501

        Flag indicating whether the questionnaire is included in the risk profile and vendor scoring  # noqa: E501

        :return: The included_in_risk_profile of this SharedQuestionnaire.  # noqa: E501
        :rtype: bool
        """
        return self._included_in_risk_profile

    @included_in_risk_profile.setter
    def included_in_risk_profile(self, included_in_risk_profile):
        """Sets the included_in_risk_profile of this SharedQuestionnaire.

        Flag indicating whether the questionnaire is included in the risk profile and vendor scoring  # noqa: E501

        :param included_in_risk_profile: The included_in_risk_profile of this SharedQuestionnaire.  # noqa: E501
        :type: bool
        """

        self._included_in_risk_profile = included_in_risk_profile

    @property
    def name(self):
        """Gets the name of this SharedQuestionnaire.  # noqa: E501

        The name of the questionnaire.  # noqa: E501

        :return: The name of this SharedQuestionnaire.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SharedQuestionnaire.

        The name of the questionnaire.  # noqa: E501

        :param name: The name of this SharedQuestionnaire.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def published_at(self):
        """Gets the published_at of this SharedQuestionnaire.  # noqa: E501

        The datetime that the questionnaire was published.  # noqa: E501

        :return: The published_at of this SharedQuestionnaire.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this SharedQuestionnaire.

        The datetime that the questionnaire was published.  # noqa: E501

        :param published_at: The published_at of this SharedQuestionnaire.  # noqa: E501
        :type: datetime
        """

        self._published_at = published_at

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
        if issubclass(SharedQuestionnaire, dict):
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
        if not isinstance(other, SharedQuestionnaire):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedQuestionnaire):
            return True

        return self.to_dict() != other.to_dict()
