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


class QuestionnaireRiskWaiver(object):
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
        'active_at': 'datetime',
        'approved_by': 'str',
        'created_by': 'str',
        'expires_at': 'datetime',
        'justification': 'str'
    }

    attribute_map = {
        'active_at': 'active_at',
        'approved_by': 'approved_by',
        'created_by': 'created_by',
        'expires_at': 'expires_at',
        'justification': 'justification'
    }

    def __init__(self, active_at=None, approved_by=None, created_by=None, expires_at=None, justification=None, _configuration=None):  # noqa: E501
        """QuestionnaireRiskWaiver - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_at = None
        self._approved_by = None
        self._created_by = None
        self._expires_at = None
        self._justification = None
        self.discriminator = None

        if active_at is not None:
            self.active_at = active_at
        if approved_by is not None:
            self.approved_by = approved_by
        if created_by is not None:
            self.created_by = created_by
        if expires_at is not None:
            self.expires_at = expires_at
        if justification is not None:
            self.justification = justification

    @property
    def active_at(self):
        """Gets the active_at of this QuestionnaireRiskWaiver.  # noqa: E501


        :return: The active_at of this QuestionnaireRiskWaiver.  # noqa: E501
        :rtype: datetime
        """
        return self._active_at

    @active_at.setter
    def active_at(self, active_at):
        """Sets the active_at of this QuestionnaireRiskWaiver.


        :param active_at: The active_at of this QuestionnaireRiskWaiver.  # noqa: E501
        :type: datetime
        """

        self._active_at = active_at

    @property
    def approved_by(self):
        """Gets the approved_by of this QuestionnaireRiskWaiver.  # noqa: E501


        :return: The approved_by of this QuestionnaireRiskWaiver.  # noqa: E501
        :rtype: str
        """
        return self._approved_by

    @approved_by.setter
    def approved_by(self, approved_by):
        """Sets the approved_by of this QuestionnaireRiskWaiver.


        :param approved_by: The approved_by of this QuestionnaireRiskWaiver.  # noqa: E501
        :type: str
        """

        self._approved_by = approved_by

    @property
    def created_by(self):
        """Gets the created_by of this QuestionnaireRiskWaiver.  # noqa: E501


        :return: The created_by of this QuestionnaireRiskWaiver.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this QuestionnaireRiskWaiver.


        :param created_by: The created_by of this QuestionnaireRiskWaiver.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def expires_at(self):
        """Gets the expires_at of this QuestionnaireRiskWaiver.  # noqa: E501


        :return: The expires_at of this QuestionnaireRiskWaiver.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this QuestionnaireRiskWaiver.


        :param expires_at: The expires_at of this QuestionnaireRiskWaiver.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def justification(self):
        """Gets the justification of this QuestionnaireRiskWaiver.  # noqa: E501


        :return: The justification of this QuestionnaireRiskWaiver.  # noqa: E501
        :rtype: str
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """Sets the justification of this QuestionnaireRiskWaiver.


        :param justification: The justification of this QuestionnaireRiskWaiver.  # noqa: E501
        :type: str
        """

        self._justification = justification

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
        if issubclass(QuestionnaireRiskWaiver, dict):
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
        if not isinstance(other, QuestionnaireRiskWaiver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuestionnaireRiskWaiver):
            return True

        return self.to_dict() != other.to_dict()