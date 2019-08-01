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


class Overpayments(object):
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
        'overpayments': 'list[Overpayment]'
    }

    attribute_map = {
        'overpayments': 'Overpayments'
    }

    def __init__(self, overpayments=None):  # noqa: E501
        """Overpayments - a model defined in OpenAPI"""  # noqa: E501

        self._overpayments = None
        self.discriminator = None

        if overpayments is not None:
            self.overpayments = overpayments

    @property
    def overpayments(self):
        """Gets the overpayments of this Overpayments.  # noqa: E501


        :return: The overpayments of this Overpayments.  # noqa: E501
        :rtype: list[Overpayment]
        """
        return self._overpayments

    @overpayments.setter
    def overpayments(self, overpayments):
        """Sets the overpayments of this Overpayments.


        :param overpayments: The overpayments of this Overpayments.  # noqa: E501
        :type: list[Overpayment]
        """

        self._overpayments = overpayments

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
        if not isinstance(other, Overpayments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other