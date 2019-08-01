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


class LinkedTransactions(object):
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
        'linked_transactions': 'list[LinkedTransaction]'
    }

    attribute_map = {
        'linked_transactions': 'LinkedTransactions'
    }

    def __init__(self, linked_transactions=None):  # noqa: E501
        """LinkedTransactions - a model defined in OpenAPI"""  # noqa: E501

        self._linked_transactions = None
        self.discriminator = None

        if linked_transactions is not None:
            self.linked_transactions = linked_transactions

    @property
    def linked_transactions(self):
        """Gets the linked_transactions of this LinkedTransactions.  # noqa: E501


        :return: The linked_transactions of this LinkedTransactions.  # noqa: E501
        :rtype: list[LinkedTransaction]
        """
        return self._linked_transactions

    @linked_transactions.setter
    def linked_transactions(self, linked_transactions):
        """Sets the linked_transactions of this LinkedTransactions.


        :param linked_transactions: The linked_transactions of this LinkedTransactions.  # noqa: E501
        :type: list[LinkedTransaction]
        """

        self._linked_transactions = linked_transactions

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
        if not isinstance(other, LinkedTransactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other