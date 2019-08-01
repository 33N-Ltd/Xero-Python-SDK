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


class Allocation(object):
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
        'invoice': 'Invoice',
        'amount': 'float',
        'date': 'date'
    }

    attribute_map = {
        'invoice': 'Invoice',
        'amount': 'Amount',
        'date': 'Date'
    }

    def __init__(self, invoice=None, amount=None, date=None):  # noqa: E501
        """Allocation - a model defined in OpenAPI"""  # noqa: E501

        self._invoice = None
        self._amount = None
        self._date = None
        self.discriminator = None

        self.invoice = invoice
        self.amount = amount
        self.date = date

    @property
    def invoice(self):
        """Gets the invoice of this Allocation.  # noqa: E501


        :return: The invoice of this Allocation.  # noqa: E501
        :rtype: Invoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this Allocation.


        :param invoice: The invoice of this Allocation.  # noqa: E501
        :type: Invoice
        """
        if invoice is None:
            raise ValueError("Invalid value for `invoice`, must not be `None`")  # noqa: E501

        self._invoice = invoice

    @property
    def amount(self):
        """Gets the amount of this Allocation.  # noqa: E501

        the amount being applied to the invoice  # noqa: E501

        :return: The amount of this Allocation.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Allocation.

        the amount being applied to the invoice  # noqa: E501

        :param amount: The amount of this Allocation.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def date(self):
        """Gets the date of this Allocation.  # noqa: E501

        the date the allocation is applied YYYY-MM-DD.  # noqa: E501

        :return: The date of this Allocation.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Allocation.

        the date the allocation is applied YYYY-MM-DD.  # noqa: E501

        :param date: The date of this Allocation.  # noqa: E501
        :type: date
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

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
        if not isinstance(other, Allocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other