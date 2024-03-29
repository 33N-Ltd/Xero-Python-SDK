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


class ContactGroup(object):
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
        'name': 'str',
        'status': 'str',
        'contact_group_id': 'str',
        'contacts': 'list[Contact]'
    }

    attribute_map = {
        'name': 'Name',
        'status': 'Status',
        'contact_group_id': 'ContactGroupID',
        'contacts': 'Contacts'
    }

    def __init__(self, name=None, status=None, contact_group_id=None, contacts=None):  # noqa: E501
        """ContactGroup - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._status = None
        self._contact_group_id = None
        self._contacts = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if contact_group_id is not None:
            self.contact_group_id = contact_group_id
        if contacts is not None:
            self.contacts = contacts

    @property
    def name(self):
        """Gets the name of this ContactGroup.  # noqa: E501

        The Name of the contact group. Required when creating a new contact  group  # noqa: E501

        :return: The name of this ContactGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContactGroup.

        The Name of the contact group. Required when creating a new contact  group  # noqa: E501

        :param name: The name of this ContactGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this ContactGroup.  # noqa: E501

        The Status of a contact group. To delete a contact group update the status to DELETED. Only contact groups with a status of ACTIVE are returned on GETs.  # noqa: E501

        :return: The status of this ContactGroup.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ContactGroup.

        The Status of a contact group. To delete a contact group update the status to DELETED. Only contact groups with a status of ACTIVE are returned on GETs.  # noqa: E501

        :param status: The status of this ContactGroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def contact_group_id(self):
        """Gets the contact_group_id of this ContactGroup.  # noqa: E501

        The Xero identifier for an contact group – specified as a string following the endpoint name. e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :return: The contact_group_id of this ContactGroup.  # noqa: E501
        :rtype: str
        """
        return self._contact_group_id

    @contact_group_id.setter
    def contact_group_id(self, contact_group_id):
        """Sets the contact_group_id of this ContactGroup.

        The Xero identifier for an contact group – specified as a string following the endpoint name. e.g. /297c2dc5-cc47-4afd-8ec8-74990b8761e9  # noqa: E501

        :param contact_group_id: The contact_group_id of this ContactGroup.  # noqa: E501
        :type: str
        """

        self._contact_group_id = contact_group_id

    @property
    def contacts(self):
        """Gets the contacts of this ContactGroup.  # noqa: E501

        The ContactID and Name of Contacts in a contact group. Returned on GETs when the ContactGroupID is supplied in the URL.  # noqa: E501

        :return: The contacts of this ContactGroup.  # noqa: E501
        :rtype: list[Contact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this ContactGroup.

        The ContactID and Name of Contacts in a contact group. Returned on GETs when the ContactGroupID is supplied in the URL.  # noqa: E501

        :param contacts: The contacts of this ContactGroup.  # noqa: E501
        :type: list[Contact]
        """

        self._contacts = contacts

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
        if not isinstance(other, ContactGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
