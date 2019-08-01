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


class BankTransaction(object):
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
        'type': 'str',
        'contact': 'Contact',
        'lineitems': 'list[LineItem]',
        'bank_account': 'Account',
        'is_reconciled': 'bool',
        'date': 'date',
        'reference': 'str',
        'currency_code': 'CurrencyCode',
        'currency_rate': 'float',
        'url': 'str',
        'status': 'str',
        'line_amount_types': 'LineAmountTypes',
        'sub_total': 'float',
        'total_tax': 'float',
        'total': 'float',
        'bank_transaction_id': 'str',
        'prepayment_id': 'str',
        'overpayment_id': 'str',
        'updated_date_utc': 'datetime',
        'has_attachments': 'bool',
        'status_attribute_string': 'str',
        'validation_errors': 'list[ValidationError]'
    }

    attribute_map = {
        'type': 'Type',
        'contact': 'Contact',
        'lineitems': 'Lineitems',
        'bank_account': 'BankAccount',
        'is_reconciled': 'IsReconciled',
        'date': 'Date',
        'reference': 'Reference',
        'currency_code': 'CurrencyCode',
        'currency_rate': 'CurrencyRate',
        'url': 'Url',
        'status': 'Status',
        'line_amount_types': 'LineAmountTypes',
        'sub_total': 'SubTotal',
        'total_tax': 'TotalTax',
        'total': 'Total',
        'bank_transaction_id': 'BankTransactionID',
        'prepayment_id': 'PrepaymentID',
        'overpayment_id': 'OverpaymentID',
        'updated_date_utc': 'UpdatedDateUTC',
        'has_attachments': 'HasAttachments',
        'status_attribute_string': 'StatusAttributeString',
        'validation_errors': 'ValidationErrors'
    }

    def __init__(self, type=None, contact=None, lineitems=None, bank_account=None, is_reconciled=None, date=None, reference=None, currency_code=None, currency_rate=None, url=None, status=None, line_amount_types=None, sub_total=None, total_tax=None, total=None, bank_transaction_id=None, prepayment_id=None, overpayment_id=None, updated_date_utc=None, has_attachments=None, status_attribute_string=None, validation_errors=None):  # noqa: E501
        """BankTransaction - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._contact = None
        self._lineitems = None
        self._bank_account = None
        self._is_reconciled = None
        self._date = None
        self._reference = None
        self._currency_code = None
        self._currency_rate = None
        self._url = None
        self._status = None
        self._line_amount_types = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._bank_transaction_id = None
        self._prepayment_id = None
        self._overpayment_id = None
        self._updated_date_utc = None
        self._has_attachments = None
        self._status_attribute_string = None
        self._validation_errors = None
        self.discriminator = None

        self.type = type
        self.contact = contact
        self.lineitems = lineitems
        self.bank_account = bank_account
        if is_reconciled is not None:
            self.is_reconciled = is_reconciled
        if date is not None:
            self.date = date
        if reference is not None:
            self.reference = reference
        if currency_code is not None:
            self.currency_code = currency_code
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if bank_transaction_id is not None:
            self.bank_transaction_id = bank_transaction_id
        if prepayment_id is not None:
            self.prepayment_id = prepayment_id
        if overpayment_id is not None:
            self.overpayment_id = overpayment_id
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if status_attribute_string is not None:
            self.status_attribute_string = status_attribute_string
        if validation_errors is not None:
            self.validation_errors = validation_errors

    @property
    def type(self):
        """Gets the type of this BankTransaction.  # noqa: E501

        See Bank Transaction Types  # noqa: E501

        :return: The type of this BankTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BankTransaction.

        See Bank Transaction Types  # noqa: E501

        :param type: The type of this BankTransaction.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["RECEIVE", "RECEIVE-OVERPAYMENT", "RECEIVE-PREPAYMENT", "SPEND", "SPEND-OVERPAYMENT", "SPEND-PREPAYMENT", "RECEIVE-TRANSFER", "SPEND-TRANSFER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def contact(self):
        """Gets the contact of this BankTransaction.  # noqa: E501


        :return: The contact of this BankTransaction.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this BankTransaction.


        :param contact: The contact of this BankTransaction.  # noqa: E501
        :type: Contact
        """
        if contact is None:
            raise ValueError("Invalid value for `contact`, must not be `None`")  # noqa: E501

        self._contact = contact

    @property
    def lineitems(self):
        """Gets the lineitems of this BankTransaction.  # noqa: E501

        See LineItems  # noqa: E501

        :return: The lineitems of this BankTransaction.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._lineitems

    @lineitems.setter
    def lineitems(self, lineitems):
        """Sets the lineitems of this BankTransaction.

        See LineItems  # noqa: E501

        :param lineitems: The lineitems of this BankTransaction.  # noqa: E501
        :type: list[LineItem]
        """
        if lineitems is None:
            raise ValueError("Invalid value for `lineitems`, must not be `None`")  # noqa: E501

        self._lineitems = lineitems

    @property
    def bank_account(self):
        """Gets the bank_account of this BankTransaction.  # noqa: E501


        :return: The bank_account of this BankTransaction.  # noqa: E501
        :rtype: Account
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """Sets the bank_account of this BankTransaction.


        :param bank_account: The bank_account of this BankTransaction.  # noqa: E501
        :type: Account
        """
        if bank_account is None:
            raise ValueError("Invalid value for `bank_account`, must not be `None`")  # noqa: E501

        self._bank_account = bank_account

    @property
    def is_reconciled(self):
        """Gets the is_reconciled of this BankTransaction.  # noqa: E501

        Boolean to show if transaction is reconciled  # noqa: E501

        :return: The is_reconciled of this BankTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._is_reconciled

    @is_reconciled.setter
    def is_reconciled(self, is_reconciled):
        """Sets the is_reconciled of this BankTransaction.

        Boolean to show if transaction is reconciled  # noqa: E501

        :param is_reconciled: The is_reconciled of this BankTransaction.  # noqa: E501
        :type: bool
        """

        self._is_reconciled = is_reconciled

    @property
    def date(self):
        """Gets the date of this BankTransaction.  # noqa: E501

        Date of transaction – YYYY-MM-DD  # noqa: E501

        :return: The date of this BankTransaction.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BankTransaction.

        Date of transaction – YYYY-MM-DD  # noqa: E501

        :param date: The date of this BankTransaction.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def reference(self):
        """Gets the reference of this BankTransaction.  # noqa: E501

        Reference for the transaction. Only supported for SPEND and RECEIVE transactions.  # noqa: E501

        :return: The reference of this BankTransaction.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this BankTransaction.

        Reference for the transaction. Only supported for SPEND and RECEIVE transactions.  # noqa: E501

        :param reference: The reference of this BankTransaction.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def currency_code(self):
        """Gets the currency_code of this BankTransaction.  # noqa: E501


        :return: The currency_code of this BankTransaction.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this BankTransaction.


        :param currency_code: The currency_code of this BankTransaction.  # noqa: E501
        :type: CurrencyCode
        """

        self._currency_code = currency_code

    @property
    def currency_rate(self):
        """Gets the currency_rate of this BankTransaction.  # noqa: E501

        Exchange rate to base currency when money is spent or received. e.g.0.7500 Only used for bank transactions in non base currency. If this isn’t specified for non base currency accounts then either the user-defined rate (preference) or the XE.com day rate will be used. Setting currency is only supported on overpayments.  # noqa: E501

        :return: The currency_rate of this BankTransaction.  # noqa: E501
        :rtype: float
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this BankTransaction.

        Exchange rate to base currency when money is spent or received. e.g.0.7500 Only used for bank transactions in non base currency. If this isn’t specified for non base currency accounts then either the user-defined rate (preference) or the XE.com day rate will be used. Setting currency is only supported on overpayments.  # noqa: E501

        :param currency_rate: The currency_rate of this BankTransaction.  # noqa: E501
        :type: float
        """

        self._currency_rate = currency_rate

    @property
    def url(self):
        """Gets the url of this BankTransaction.  # noqa: E501

        URL link to a source document – shown as “Go to App Name”  # noqa: E501

        :return: The url of this BankTransaction.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BankTransaction.

        URL link to a source document – shown as “Go to App Name”  # noqa: E501

        :param url: The url of this BankTransaction.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def status(self):
        """Gets the status of this BankTransaction.  # noqa: E501

        See Bank Transaction Status Codes  # noqa: E501

        :return: The status of this BankTransaction.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BankTransaction.

        See Bank Transaction Status Codes  # noqa: E501

        :param status: The status of this BankTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTHORISED", "DELETED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def line_amount_types(self):
        """Gets the line_amount_types of this BankTransaction.  # noqa: E501


        :return: The line_amount_types of this BankTransaction.  # noqa: E501
        :rtype: LineAmountTypes
        """
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        """Sets the line_amount_types of this BankTransaction.


        :param line_amount_types: The line_amount_types of this BankTransaction.  # noqa: E501
        :type: LineAmountTypes
        """

        self._line_amount_types = line_amount_types

    @property
    def sub_total(self):
        """Gets the sub_total of this BankTransaction.  # noqa: E501

        Total of bank transaction excluding taxes  # noqa: E501

        :return: The sub_total of this BankTransaction.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this BankTransaction.

        Total of bank transaction excluding taxes  # noqa: E501

        :param sub_total: The sub_total of this BankTransaction.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def total_tax(self):
        """Gets the total_tax of this BankTransaction.  # noqa: E501

        Total tax on bank transaction  # noqa: E501

        :return: The total_tax of this BankTransaction.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this BankTransaction.

        Total tax on bank transaction  # noqa: E501

        :param total_tax: The total_tax of this BankTransaction.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this BankTransaction.  # noqa: E501

        Total of bank transaction tax inclusive  # noqa: E501

        :return: The total of this BankTransaction.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BankTransaction.

        Total of bank transaction tax inclusive  # noqa: E501

        :param total: The total of this BankTransaction.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def bank_transaction_id(self):
        """Gets the bank_transaction_id of this BankTransaction.  # noqa: E501

        Xero generated unique identifier for bank transaction  # noqa: E501

        :return: The bank_transaction_id of this BankTransaction.  # noqa: E501
        :rtype: str
        """
        return self._bank_transaction_id

    @bank_transaction_id.setter
    def bank_transaction_id(self, bank_transaction_id):
        """Sets the bank_transaction_id of this BankTransaction.

        Xero generated unique identifier for bank transaction  # noqa: E501

        :param bank_transaction_id: The bank_transaction_id of this BankTransaction.  # noqa: E501
        :type: str
        """

        self._bank_transaction_id = bank_transaction_id

    @property
    def prepayment_id(self):
        """Gets the prepayment_id of this BankTransaction.  # noqa: E501

        Xero generated unique identifier for a Prepayment. This will be returned on BankTransactions with a Type of SPEND-PREPAYMENT or RECEIVE-PREPAYMENT  # noqa: E501

        :return: The prepayment_id of this BankTransaction.  # noqa: E501
        :rtype: str
        """
        return self._prepayment_id

    @prepayment_id.setter
    def prepayment_id(self, prepayment_id):
        """Sets the prepayment_id of this BankTransaction.

        Xero generated unique identifier for a Prepayment. This will be returned on BankTransactions with a Type of SPEND-PREPAYMENT or RECEIVE-PREPAYMENT  # noqa: E501

        :param prepayment_id: The prepayment_id of this BankTransaction.  # noqa: E501
        :type: str
        """

        self._prepayment_id = prepayment_id

    @property
    def overpayment_id(self):
        """Gets the overpayment_id of this BankTransaction.  # noqa: E501

        Xero generated unique identifier for an Overpayment. This will be returned on BankTransactions with a Type of SPEND-OVERPAYMENT or RECEIVE-OVERPAYMENT  # noqa: E501

        :return: The overpayment_id of this BankTransaction.  # noqa: E501
        :rtype: str
        """
        return self._overpayment_id

    @overpayment_id.setter
    def overpayment_id(self, overpayment_id):
        """Sets the overpayment_id of this BankTransaction.

        Xero generated unique identifier for an Overpayment. This will be returned on BankTransactions with a Type of SPEND-OVERPAYMENT or RECEIVE-OVERPAYMENT  # noqa: E501

        :param overpayment_id: The overpayment_id of this BankTransaction.  # noqa: E501
        :type: str
        """

        self._overpayment_id = overpayment_id

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this BankTransaction.  # noqa: E501

        Last modified date UTC format  # noqa: E501

        :return: The updated_date_utc of this BankTransaction.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this BankTransaction.

        Last modified date UTC format  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this BankTransaction.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def has_attachments(self):
        """Gets the has_attachments of this BankTransaction.  # noqa: E501

        Boolean to indicate if a bank transaction has an attachment  # noqa: E501

        :return: The has_attachments of this BankTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        """Sets the has_attachments of this BankTransaction.

        Boolean to indicate if a bank transaction has an attachment  # noqa: E501

        :param has_attachments: The has_attachments of this BankTransaction.  # noqa: E501
        :type: bool
        """

        self._has_attachments = has_attachments

    @property
    def status_attribute_string(self):
        """Gets the status_attribute_string of this BankTransaction.  # noqa: E501

        A string to indicate if a invoice status  # noqa: E501

        :return: The status_attribute_string of this BankTransaction.  # noqa: E501
        :rtype: str
        """
        return self._status_attribute_string

    @status_attribute_string.setter
    def status_attribute_string(self, status_attribute_string):
        """Sets the status_attribute_string of this BankTransaction.

        A string to indicate if a invoice status  # noqa: E501

        :param status_attribute_string: The status_attribute_string of this BankTransaction.  # noqa: E501
        :type: str
        """

        self._status_attribute_string = status_attribute_string

    @property
    def validation_errors(self):
        """Gets the validation_errors of this BankTransaction.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this BankTransaction.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this BankTransaction.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this BankTransaction.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors

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
        if not isinstance(other, BankTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
