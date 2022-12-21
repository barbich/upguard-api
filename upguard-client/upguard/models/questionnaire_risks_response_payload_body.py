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


class QuestionnaireRisksResponsePayloadBody(object):
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
        'next_page_token': 'str',
        'risks': 'list[QuestionnaireRisk]',
        'total_results': 'int'
    }

    attribute_map = {
        'next_page_token': 'next_page_token',
        'risks': 'risks',
        'total_results': 'total_results'
    }

    def __init__(self, next_page_token=None, risks=None, total_results=None, _configuration=None):  # noqa: E501
        """QuestionnaireRisksResponsePayloadBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._next_page_token = None
        self._risks = None
        self._total_results = None
        self.discriminator = None

        if next_page_token is not None:
            self.next_page_token = next_page_token
        if risks is not None:
            self.risks = risks
        if total_results is not None:
            self.total_results = total_results

    @property
    def next_page_token(self):
        """Gets the next_page_token of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501

        The token to be used to retrieve the next page of results. Will not be returned if there are no more results.  # noqa: E501

        :return: The next_page_token of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this QuestionnaireRisksResponsePayloadBody.

        The token to be used to retrieve the next page of results. Will not be returned if there are no more results.  # noqa: E501

        :param next_page_token: The next_page_token of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def risks(self):
        """Gets the risks of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501

        The list of questionnaire risks  # noqa: E501

        :return: The risks of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501
        :rtype: list[QuestionnaireRisk]
        """
        return self._risks

    @risks.setter
    def risks(self, risks):
        """Sets the risks of this QuestionnaireRisksResponsePayloadBody.

        The list of questionnaire risks  # noqa: E501

        :param risks: The risks of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501
        :type: list[QuestionnaireRisk]
        """

        self._risks = risks

    @property
    def total_results(self):
        """Gets the total_results of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501

        The total number of risks found.  # noqa: E501

        :return: The total_results of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this QuestionnaireRisksResponsePayloadBody.

        The total number of risks found.  # noqa: E501

        :param total_results: The total_results of this QuestionnaireRisksResponsePayloadBody.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

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
        if issubclass(QuestionnaireRisksResponsePayloadBody, dict):
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
        if not isinstance(other, QuestionnaireRisksResponsePayloadBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuestionnaireRisksResponsePayloadBody):
            return True

        return self.to_dict() != other.to_dict()