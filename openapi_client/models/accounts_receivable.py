# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AccountsReceivable(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'outstanding': 'float',
        'overdue': 'float'
    }

    attribute_map = {
        'outstanding': 'Outstanding',
        'overdue': 'Overdue'
    }

    def __init__(self, outstanding=None, overdue=None):  # noqa: E501
        """AccountsReceivable - a model defined in OpenAPI"""  # noqa: E501

        self._outstanding = None
        self._overdue = None
        self.discriminator = None

        if outstanding is not None:
            self.outstanding = outstanding
        if overdue is not None:
            self.overdue = overdue

    @property
    def outstanding(self):
        """Gets the outstanding of this AccountsReceivable.  # noqa: E501


        :return: The outstanding of this AccountsReceivable.  # noqa: E501
        :rtype: float
        """
        return self._outstanding

    @outstanding.setter
    def outstanding(self, outstanding):
        """Sets the outstanding of this AccountsReceivable.


        :param outstanding: The outstanding of this AccountsReceivable.  # noqa: E501
        :type: float
        """

        self._outstanding = outstanding

    @property
    def overdue(self):
        """Gets the overdue of this AccountsReceivable.  # noqa: E501


        :return: The overdue of this AccountsReceivable.  # noqa: E501
        :rtype: float
        """
        return self._overdue

    @overdue.setter
    def overdue(self, overdue):
        """Sets the overdue of this AccountsReceivable.


        :param overdue: The overdue of this AccountsReceivable.  # noqa: E501
        :type: float
        """

        self._overdue = overdue

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountsReceivable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
