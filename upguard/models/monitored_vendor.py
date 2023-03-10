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


class MonitoredVendor(object):
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
        'assessment_status': 'str',
        'attributes': 'dict(str, str)',
        'automated_score': 'int',
        'category_scores': 'CategoryScores',
        'id': 'int',
        'labels': 'list[str]',
        'last_assessed': 'datetime',
        'monitored': 'bool',
        'name': 'str',
        'overall_score': 'int',
        'primary_hostname': 'str',
        'questionnaire_score': 'int',
        'risks': 'list[VendorsRisk]',
        'score': 'int',
        'tier': 'int'
    }

    attribute_map = {
        'assessment_status': 'assessmentStatus',
        'attributes': 'attributes',
        'automated_score': 'automatedScore',
        'category_scores': 'category_scores',
        'id': 'id',
        'labels': 'labels',
        'last_assessed': 'lastAssessed',
        'monitored': 'monitored',
        'name': 'name',
        'overall_score': 'overallScore',
        'primary_hostname': 'primary_hostname',
        'questionnaire_score': 'questionnaireScore',
        'risks': 'risks',
        'score': 'score',
        'tier': 'tier'
    }

    def __init__(self, assessment_status=None, attributes=None, automated_score=None, category_scores=None, id=None, labels=None, last_assessed=None, monitored=None, name=None, overall_score=None, primary_hostname=None, questionnaire_score=None, risks=None, score=None, tier=None, _configuration=None):  # noqa: E501
        """MonitoredVendor - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assessment_status = None
        self._attributes = None
        self._automated_score = None
        self._category_scores = None
        self._id = None
        self._labels = None
        self._last_assessed = None
        self._monitored = None
        self._name = None
        self._overall_score = None
        self._primary_hostname = None
        self._questionnaire_score = None
        self._risks = None
        self._score = None
        self._tier = None
        self.discriminator = None

        if assessment_status is not None:
            self.assessment_status = assessment_status
        if attributes is not None:
            self.attributes = attributes
        if automated_score is not None:
            self.automated_score = automated_score
        if category_scores is not None:
            self.category_scores = category_scores
        if id is not None:
            self.id = id
        if labels is not None:
            self.labels = labels
        if last_assessed is not None:
            self.last_assessed = last_assessed
        if monitored is not None:
            self.monitored = monitored
        if name is not None:
            self.name = name
        if overall_score is not None:
            self.overall_score = overall_score
        if primary_hostname is not None:
            self.primary_hostname = primary_hostname
        if questionnaire_score is not None:
            self.questionnaire_score = questionnaire_score
        if risks is not None:
            self.risks = risks
        if score is not None:
            self.score = score
        if tier is not None:
            self.tier = tier

    @property
    def assessment_status(self):
        """Gets the assessment_status of this MonitoredVendor.  # noqa: E501

        Assessment status for the vendor. Possible values are Published, In progress, Not assessed. The field will be omitted for non monitored vendors.  # noqa: E501

        :return: The assessment_status of this MonitoredVendor.  # noqa: E501
        :rtype: str
        """
        return self._assessment_status

    @assessment_status.setter
    def assessment_status(self, assessment_status):
        """Sets the assessment_status of this MonitoredVendor.

        Assessment status for the vendor. Possible values are Published, In progress, Not assessed. The field will be omitted for non monitored vendors.  # noqa: E501

        :param assessment_status: The assessment_status of this MonitoredVendor.  # noqa: E501
        :type: str
        """

        self._assessment_status = assessment_status

    @property
    def attributes(self):
        """Gets the attributes of this MonitoredVendor.  # noqa: E501

        The attributes applied to the vendor. If no attributes are applied this field will be omitted  # noqa: E501

        :return: The attributes of this MonitoredVendor.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this MonitoredVendor.

        The attributes applied to the vendor. If no attributes are applied this field will be omitted  # noqa: E501

        :param attributes: The attributes of this MonitoredVendor.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def automated_score(self):
        """Gets the automated_score of this MonitoredVendor.  # noqa: E501

        The current automated score of the vendor without questionnaire. Omitted if no current scanning score.  # noqa: E501

        :return: The automated_score of this MonitoredVendor.  # noqa: E501
        :rtype: int
        """
        return self._automated_score

    @automated_score.setter
    def automated_score(self, automated_score):
        """Sets the automated_score of this MonitoredVendor.

        The current automated score of the vendor without questionnaire. Omitted if no current scanning score.  # noqa: E501

        :param automated_score: The automated_score of this MonitoredVendor.  # noqa: E501
        :type: int
        """

        self._automated_score = automated_score

    @property
    def category_scores(self):
        """Gets the category_scores of this MonitoredVendor.  # noqa: E501


        :return: The category_scores of this MonitoredVendor.  # noqa: E501
        :rtype: CategoryScores
        """
        return self._category_scores

    @category_scores.setter
    def category_scores(self, category_scores):
        """Sets the category_scores of this MonitoredVendor.


        :param category_scores: The category_scores of this MonitoredVendor.  # noqa: E501
        :type: CategoryScores
        """

        self._category_scores = category_scores

    @property
    def id(self):
        """Gets the id of this MonitoredVendor.  # noqa: E501

        The id of the vendor. Its possible for a hostname to change which vendor it belongs to for a number of reasons (eg. Company's legal entity changes, improved data quality, etc...). For this reason, do not assume a hostname will always return the same vendor id.  # noqa: E501

        :return: The id of this MonitoredVendor.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MonitoredVendor.

        The id of the vendor. Its possible for a hostname to change which vendor it belongs to for a number of reasons (eg. Company's legal entity changes, improved data quality, etc...). For this reason, do not assume a hostname will always return the same vendor id.  # noqa: E501

        :param id: The id of this MonitoredVendor.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this MonitoredVendor.  # noqa: E501

        Labels that the vendor is currently associated with.  # noqa: E501

        :return: The labels of this MonitoredVendor.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this MonitoredVendor.

        Labels that the vendor is currently associated with.  # noqa: E501

        :param labels: The labels of this MonitoredVendor.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def last_assessed(self):
        """Gets the last_assessed of this MonitoredVendor.  # noqa: E501

        Date of the last assessment for the vendor. The field will be omitted if no published assessment is present.  # noqa: E501

        :return: The last_assessed of this MonitoredVendor.  # noqa: E501
        :rtype: datetime
        """
        return self._last_assessed

    @last_assessed.setter
    def last_assessed(self, last_assessed):
        """Sets the last_assessed of this MonitoredVendor.

        Date of the last assessment for the vendor. The field will be omitted if no published assessment is present.  # noqa: E501

        :param last_assessed: The last_assessed of this MonitoredVendor.  # noqa: E501
        :type: datetime
        """

        self._last_assessed = last_assessed

    @property
    def monitored(self):
        """Gets the monitored of this MonitoredVendor.  # noqa: E501

        Indicates whether the vendor is monitored or not.  # noqa: E501

        :return: The monitored of this MonitoredVendor.  # noqa: E501
        :rtype: bool
        """
        return self._monitored

    @monitored.setter
    def monitored(self, monitored):
        """Sets the monitored of this MonitoredVendor.

        Indicates whether the vendor is monitored or not.  # noqa: E501

        :param monitored: The monitored of this MonitoredVendor.  # noqa: E501
        :type: bool
        """

        self._monitored = monitored

    @property
    def name(self):
        """Gets the name of this MonitoredVendor.  # noqa: E501

        The name of the vendor  # noqa: E501

        :return: The name of this MonitoredVendor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MonitoredVendor.

        The name of the vendor  # noqa: E501

        :param name: The name of this MonitoredVendor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def overall_score(self):
        """Gets the overall_score of this MonitoredVendor.  # noqa: E501

        The current score of the vendor including automated and questionnaire. Omitted if no current overall score.  # noqa: E501

        :return: The overall_score of this MonitoredVendor.  # noqa: E501
        :rtype: int
        """
        return self._overall_score

    @overall_score.setter
    def overall_score(self, overall_score):
        """Sets the overall_score of this MonitoredVendor.

        The current score of the vendor including automated and questionnaire. Omitted if no current overall score.  # noqa: E501

        :param overall_score: The overall_score of this MonitoredVendor.  # noqa: E501
        :type: int
        """

        self._overall_score = overall_score

    @property
    def primary_hostname(self):
        """Gets the primary_hostname of this MonitoredVendor.  # noqa: E501

        The primary hostname of the vendor  # noqa: E501

        :return: The primary_hostname of this MonitoredVendor.  # noqa: E501
        :rtype: str
        """
        return self._primary_hostname

    @primary_hostname.setter
    def primary_hostname(self, primary_hostname):
        """Sets the primary_hostname of this MonitoredVendor.

        The primary hostname of the vendor  # noqa: E501

        :param primary_hostname: The primary_hostname of this MonitoredVendor.  # noqa: E501
        :type: str
        """

        self._primary_hostname = primary_hostname

    @property
    def questionnaire_score(self):
        """Gets the questionnaire_score of this MonitoredVendor.  # noqa: E501

        The current questionnaire score of the vendor. Omitted if no current questionnaire score.  # noqa: E501

        :return: The questionnaire_score of this MonitoredVendor.  # noqa: E501
        :rtype: int
        """
        return self._questionnaire_score

    @questionnaire_score.setter
    def questionnaire_score(self, questionnaire_score):
        """Sets the questionnaire_score of this MonitoredVendor.

        The current questionnaire score of the vendor. Omitted if no current questionnaire score.  # noqa: E501

        :param questionnaire_score: The questionnaire_score of this MonitoredVendor.  # noqa: E501
        :type: int
        """

        self._questionnaire_score = questionnaire_score

    @property
    def risks(self):
        """Gets the risks of this MonitoredVendor.  # noqa: E501

        Optional list of risks for the vendor. Note that this is a summary list of risks and does not take into account risk waivers. To have a precise view of a vendor risks use the /risks/vendors endpoint.  # noqa: E501

        :return: The risks of this MonitoredVendor.  # noqa: E501
        :rtype: list[VendorsRisk]
        """
        return self._risks

    @risks.setter
    def risks(self, risks):
        """Sets the risks of this MonitoredVendor.

        Optional list of risks for the vendor. Note that this is a summary list of risks and does not take into account risk waivers. To have a precise view of a vendor risks use the /risks/vendors endpoint.  # noqa: E501

        :param risks: The risks of this MonitoredVendor.  # noqa: E501
        :type: list[VendorsRisk]
        """

        self._risks = risks

    @property
    def score(self):
        """Gets the score of this MonitoredVendor.  # noqa: E501

        NOTE: deprecated (use OverallScore). The current score of the vendor. A -1 value represents no current score for the vendor.  # noqa: E501

        :return: The score of this MonitoredVendor.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this MonitoredVendor.

        NOTE: deprecated (use OverallScore). The current score of the vendor. A -1 value represents no current score for the vendor.  # noqa: E501

        :param score: The score of this MonitoredVendor.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def tier(self):
        """Gets the tier of this MonitoredVendor.  # noqa: E501

        Tier currently assigned to the vendor. Omitted if no tier is assigned to the vendor.  # noqa: E501

        :return: The tier of this MonitoredVendor.  # noqa: E501
        :rtype: int
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this MonitoredVendor.

        Tier currently assigned to the vendor. Omitted if no tier is assigned to the vendor.  # noqa: E501

        :param tier: The tier of this MonitoredVendor.  # noqa: E501
        :type: int
        """

        self._tier = tier

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
        if issubclass(MonitoredVendor, dict):
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
        if not isinstance(other, MonitoredVendor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MonitoredVendor):
            return True

        return self.to_dict() != other.to_dict()
