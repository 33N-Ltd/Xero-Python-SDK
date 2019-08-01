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


class CISSetting(object):
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
        'cis_enabled': 'bool',
        'rate': 'int'
    }

    attribute_map = {
        'cis_enabled': 'CISEnabled',
        'rate': 'Rate'
    }

    def __init__(self, cis_enabled=None, rate=None):  # noqa: E501
        """CISSetting - a model defined in OpenAPI"""  # noqa: E501

        self._cis_enabled = None
        self._rate = None
        self.discriminator = None

        if cis_enabled is not None:
            self.cis_enabled = cis_enabled
        if rate is not None:
            self.rate = rate

    @property
    def cis_enabled(self):
        """Gets the cis_enabled of this CISSetting.  # noqa: E501

        Boolean that describes if the contact is a CIS Subcontractor  # noqa: E501

        :return: The cis_enabled of this CISSetting.  # noqa: E501
        :rtype: bool
        """
        return self._cis_enabled

    @cis_enabled.setter
    def cis_enabled(self, cis_enabled):
        """Sets the cis_enabled of this CISSetting.

        Boolean that describes if the contact is a CIS Subcontractor  # noqa: E501

        :param cis_enabled: The cis_enabled of this CISSetting.  # noqa: E501
        :type: bool
        """

        self._cis_enabled = cis_enabled

    @property
    def rate(self):
        """Gets the rate of this CISSetting.  # noqa: E501

        CIS Deduction rate for the contact if he is a subcontractor. If the contact is not CISEnabled, then the rate is not returned  # noqa: E501

        :return: The rate of this CISSetting.  # noqa: E501
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this CISSetting.

        CIS Deduction rate for the contact if he is a subcontractor. If the contact is not CISEnabled, then the rate is not returned  # noqa: E501

        :param rate: The rate of this CISSetting.  # noqa: E501
        :type: int
        """

        self._rate = rate

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
        if not isinstance(other, CISSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
