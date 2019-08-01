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


class TrackingOption(object):
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
        'tracking_option_id': 'str',
        'name': 'str',
        'status': 'str',
        'tracking_category_id': 'str'
    }

    attribute_map = {
        'tracking_option_id': 'TrackingOptionID',
        'name': 'Name',
        'status': 'Status',
        'tracking_category_id': 'TrackingCategoryID'
    }

    def __init__(self, tracking_option_id=None, name=None, status=None, tracking_category_id=None):  # noqa: E501
        """TrackingOption - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_option_id = None
        self._name = None
        self._status = None
        self._tracking_category_id = None
        self.discriminator = None

        if tracking_option_id is not None:
            self.tracking_option_id = tracking_option_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if tracking_category_id is not None:
            self.tracking_category_id = tracking_category_id

    @property
    def tracking_option_id(self):
        """Gets the tracking_option_id of this TrackingOption.  # noqa: E501

        The Xero identifier for a tracking optione.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a  # noqa: E501

        :return: The tracking_option_id of this TrackingOption.  # noqa: E501
        :rtype: str
        """
        return self._tracking_option_id

    @tracking_option_id.setter
    def tracking_option_id(self, tracking_option_id):
        """Sets the tracking_option_id of this TrackingOption.

        The Xero identifier for a tracking optione.g. ae777a87-5ef3-4fa0-a4f0-d10e1f13073a  # noqa: E501

        :param tracking_option_id: The tracking_option_id of this TrackingOption.  # noqa: E501
        :type: str
        """

        self._tracking_option_id = tracking_option_id

    @property
    def name(self):
        """Gets the name of this TrackingOption.  # noqa: E501

        The name of the tracking option e.g. Marketing, East (max length = 50)  # noqa: E501

        :return: The name of this TrackingOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrackingOption.

        The name of the tracking option e.g. Marketing, East (max length = 50)  # noqa: E501

        :param name: The name of this TrackingOption.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this TrackingOption.  # noqa: E501

        The status of a tracking option  # noqa: E501

        :return: The status of this TrackingOption.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrackingOption.

        The status of a tracking option  # noqa: E501

        :param status: The status of this TrackingOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "ARCHIVED", "DELETED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def tracking_category_id(self):
        """Gets the tracking_category_id of this TrackingOption.  # noqa: E501

        Filter by a tracking categorye.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :return: The tracking_category_id of this TrackingOption.  # noqa: E501
        :rtype: str
        """
        return self._tracking_category_id

    @tracking_category_id.setter
    def tracking_category_id(self, tracking_category_id):
        """Sets the tracking_category_id of this TrackingOption.

        Filter by a tracking categorye.g. 297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :param tracking_category_id: The tracking_category_id of this TrackingOption.  # noqa: E501
        :type: str
        """

        self._tracking_category_id = tracking_category_id

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
        if not isinstance(other, TrackingOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
