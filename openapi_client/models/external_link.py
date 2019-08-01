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


class ExternalLink(object):
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
        'link_type': 'str',
        'url': 'str',
        'description': 'str'
    }

    attribute_map = {
        'link_type': 'LinkType',
        'url': 'Url',
        'description': 'Description'
    }

    def __init__(self, link_type=None, url=None, description=None):  # noqa: E501
        """ExternalLink - a model defined in OpenAPI"""  # noqa: E501

        self._link_type = None
        self._url = None
        self._description = None
        self.discriminator = None

        if link_type is not None:
            self.link_type = link_type
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description

    @property
    def link_type(self):
        """Gets the link_type of this ExternalLink.  # noqa: E501

        See External link types  # noqa: E501

        :return: The link_type of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this ExternalLink.

        See External link types  # noqa: E501

        :param link_type: The link_type of this ExternalLink.  # noqa: E501
        :type: str
        """
        allowed_values = ["Facebook", "GooglePlus", "LinkedIn", "Twitter", "Website"]  # noqa: E501
        if link_type not in allowed_values:
            raise ValueError(
                "Invalid value for `link_type` ({0}), must be one of {1}"  # noqa: E501
                .format(link_type, allowed_values)
            )

        self._link_type = link_type

    @property
    def url(self):
        """Gets the url of this ExternalLink.  # noqa: E501

        URL for service e.g. http://twitter.com/xeroapi  # noqa: E501

        :return: The url of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ExternalLink.

        URL for service e.g. http://twitter.com/xeroapi  # noqa: E501

        :param url: The url of this ExternalLink.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """Gets the description of this ExternalLink.  # noqa: E501


        :return: The description of this ExternalLink.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExternalLink.


        :param description: The description of this ExternalLink.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, ExternalLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
