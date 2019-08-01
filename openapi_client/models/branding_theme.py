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


class BrandingTheme(object):
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
        'branding_theme_id': 'str',
        'name': 'str',
        'sort_order': 'int',
        'created_date_utc': 'datetime'
    }

    attribute_map = {
        'branding_theme_id': 'BrandingThemeID',
        'name': 'Name',
        'sort_order': 'SortOrder',
        'created_date_utc': 'CreatedDateUTC'
    }

    def __init__(self, branding_theme_id=None, name=None, sort_order=None, created_date_utc=None):  # noqa: E501
        """BrandingTheme - a model defined in OpenAPI"""  # noqa: E501

        self._branding_theme_id = None
        self._name = None
        self._sort_order = None
        self._created_date_utc = None
        self.discriminator = None

        if branding_theme_id is not None:
            self.branding_theme_id = branding_theme_id
        if name is not None:
            self.name = name
        if sort_order is not None:
            self.sort_order = sort_order
        if created_date_utc is not None:
            self.created_date_utc = created_date_utc

    @property
    def branding_theme_id(self):
        """Gets the branding_theme_id of this BrandingTheme.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The branding_theme_id of this BrandingTheme.  # noqa: E501
        :rtype: str
        """
        return self._branding_theme_id

    @branding_theme_id.setter
    def branding_theme_id(self, branding_theme_id):
        """Sets the branding_theme_id of this BrandingTheme.

        Xero identifier  # noqa: E501

        :param branding_theme_id: The branding_theme_id of this BrandingTheme.  # noqa: E501
        :type: str
        """

        self._branding_theme_id = branding_theme_id

    @property
    def name(self):
        """Gets the name of this BrandingTheme.  # noqa: E501

        Name of branding theme  # noqa: E501

        :return: The name of this BrandingTheme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BrandingTheme.

        Name of branding theme  # noqa: E501

        :param name: The name of this BrandingTheme.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sort_order(self):
        """Gets the sort_order of this BrandingTheme.  # noqa: E501

        Integer – ranked order of branding theme. The default branding theme has a value of 0  # noqa: E501

        :return: The sort_order of this BrandingTheme.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this BrandingTheme.

        Integer – ranked order of branding theme. The default branding theme has a value of 0  # noqa: E501

        :param sort_order: The sort_order of this BrandingTheme.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def created_date_utc(self):
        """Gets the created_date_utc of this BrandingTheme.  # noqa: E501

        UTC timestamp of creation date of branding theme  # noqa: E501

        :return: The created_date_utc of this BrandingTheme.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_utc

    @created_date_utc.setter
    def created_date_utc(self, created_date_utc):
        """Sets the created_date_utc of this BrandingTheme.

        UTC timestamp of creation date of branding theme  # noqa: E501

        :param created_date_utc: The created_date_utc of this BrandingTheme.  # noqa: E501
        :type: datetime
        """

        self._created_date_utc = created_date_utc

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
        if not isinstance(other, BrandingTheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
