# openapi_client.AccountingApi

All URIs are relative to *https://api.xero.com/api.xro/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountingApi.md#create_account) | **PUT** /Accounts | Allows you to create a new chart of accounts
[**create_account_attachment_by_file_name**](AccountingApi.md#create_account_attachment_by_file_name) | **PUT** /Accounts/{AccountID}/Attachments/{FileName} | Allows you to create Attachment on Account
[**create_bank_transaction**](AccountingApi.md#create_bank_transaction) | **PUT** /BankTransactions | Allows you to create a spend or receive money transaction
[**create_bank_transaction_attachment_by_file_name**](AccountingApi.md#create_bank_transaction_attachment_by_file_name) | **PUT** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Allows you to createa an Attachment on BankTransaction by Filename
[**create_bank_transaction_history_record**](AccountingApi.md#create_bank_transaction_history_record) | **PUT** /BankTransactions/{BankTransactionID}/History | Allows you to create history record for a bank transactions
[**create_bank_transfer**](AccountingApi.md#create_bank_transfer) | **PUT** /BankTransfers | Allows you to create a bank transfers
[**create_bank_transfer_attachment_by_file_name**](AccountingApi.md#create_bank_transfer_attachment_by_file_name) | **PUT** /BankTransfers/{BankTransferID}/Attachments/{FileName} | 
[**create_bank_transfer_history_record**](AccountingApi.md#create_bank_transfer_history_record) | **PUT** /BankTransfers/{BankTransferID}/History | 
[**create_batch_payment**](AccountingApi.md#create_batch_payment) | **PUT** /BatchPayments | Create one or many BatchPayments for invoices
[**create_batch_payment_history_record**](AccountingApi.md#create_batch_payment_history_record) | **PUT** /BatchPayments/{BatchPaymentID}/History | Allows you to create a history record for a Batch Payment
[**create_branding_theme_payment_services**](AccountingApi.md#create_branding_theme_payment_services) | **POST** /BrandingThemes/{BrandingThemeID}/PaymentServices | Allow for the creation of new custom payment service for specified Branding Theme
[**create_contact**](AccountingApi.md#create_contact) | **PUT** /Contacts | 
[**create_contact_attachment_by_file_name**](AccountingApi.md#create_contact_attachment_by_file_name) | **PUT** /Contacts/{ContactID}/Attachments/{FileName} | 
[**create_contact_group**](AccountingApi.md#create_contact_group) | **PUT** /ContactGroups | Allows you to create a contact group
[**create_contact_group_contacts**](AccountingApi.md#create_contact_group_contacts) | **PUT** /ContactGroups/{ContactGroupID}/Contacts | Allows you to add Contacts to a Contract Group
[**create_contact_history**](AccountingApi.md#create_contact_history) | **PUT** /Contacts/{ContactID}/History | Allows you to retrieve a history records of an Contact
[**create_credit_note**](AccountingApi.md#create_credit_note) | **PUT** /CreditNotes | Allows you to create a credit note
[**create_credit_note_allocation**](AccountingApi.md#create_credit_note_allocation) | **PUT** /CreditNotes/{CreditNoteID}/Allocations | Allows you to create Allocation on CreditNote
[**create_credit_note_attachment_by_file_name**](AccountingApi.md#create_credit_note_attachment_by_file_name) | **PUT** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Allows you to create Attachments on CreditNote by file name
[**create_credit_note_history**](AccountingApi.md#create_credit_note_history) | **PUT** /CreditNotes/{CreditNoteID}/History | Allows you to retrieve a history records of an CreditNote
[**create_currency**](AccountingApi.md#create_currency) | **PUT** /Currencies | 
[**create_employee**](AccountingApi.md#create_employee) | **PUT** /Employees | Allows you to create new employees used in Xero payrun
[**create_expense_claim**](AccountingApi.md#create_expense_claim) | **PUT** /ExpenseClaims | Allows you to retrieve expense claims
[**create_expense_claim_history**](AccountingApi.md#create_expense_claim_history) | **PUT** /ExpenseClaims/{ExpenseClaimID}/History | Allows you to create a history records of an ExpenseClaim
[**create_invoice**](AccountingApi.md#create_invoice) | **PUT** /Invoices | Allows you to create any sales invoices or purchase bills
[**create_invoice_attachment_by_file_name**](AccountingApi.md#create_invoice_attachment_by_file_name) | **PUT** /Invoices/{InvoiceID}/Attachments/{FileName} | Allows you to create an Attachment on invoices or purchase bills by it&#39;s filename
[**create_invoice_history**](AccountingApi.md#create_invoice_history) | **PUT** /Invoices/{InvoiceID}/History | Allows you to retrieve a history records of an invoice
[**create_item**](AccountingApi.md#create_item) | **PUT** /Items | Allows you to create an item
[**create_item_history**](AccountingApi.md#create_item_history) | **PUT** /Items/{ItemID}/History | Allows you to create a history record for items
[**create_linked_transaction**](AccountingApi.md#create_linked_transaction) | **PUT** /LinkedTransactions | Allows you to create linked transactions (billable expenses)
[**create_manual_journal**](AccountingApi.md#create_manual_journal) | **PUT** /ManualJournals | Allows you to create a manual journal
[**create_manual_journal_attachment_by_file_name**](AccountingApi.md#create_manual_journal_attachment_by_file_name) | **PUT** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Allows you to create a specified Attachment on ManualJournal by file name
[**create_overpayment_allocation**](AccountingApi.md#create_overpayment_allocation) | **PUT** /Overpayments/{OverpaymentID}/Allocations | Allows you to retrieve Allocations for overpayments
[**create_overpayment_history**](AccountingApi.md#create_overpayment_history) | **PUT** /Overpayments/{OverpaymentID}/History | Allows you to create history records of an Overpayment
[**create_payment**](AccountingApi.md#create_payment) | **PUT** /Payments | Allows you to create payments for invoices and credit notes
[**create_payment_history**](AccountingApi.md#create_payment_history) | **PUT** /Payments/{PaymentID}/History | Allows you to create a history record for a payment
[**create_payment_service**](AccountingApi.md#create_payment_service) | **PUT** /PaymentServices | Allows you to create payment services
[**create_prepayment_allocation**](AccountingApi.md#create_prepayment_allocation) | **PUT** /Prepayments/{PrepaymentID}/Allocations | Allows you to create an Allocation for prepayments
[**create_prepayment_history**](AccountingApi.md#create_prepayment_history) | **PUT** /Prepayments/{PrepaymentID}/History | Allows you to create a history record for an Prepayment
[**create_purchase_order**](AccountingApi.md#create_purchase_order) | **PUT** /PurchaseOrders | Allows you to create purchase orders
[**create_purchase_order_history**](AccountingApi.md#create_purchase_order_history) | **PUT** /PurchaseOrders/{PurchaseOrderID}/History | Allows you to create HistoryRecord for purchase orders
[**create_receipt**](AccountingApi.md#create_receipt) | **PUT** /Receipts | Allows you to create draft expense claim receipts for any user
[**create_receipt_attachment_by_file_name**](AccountingApi.md#create_receipt_attachment_by_file_name) | **PUT** /Receipts/{ReceiptID}/Attachments/{FileName} | Allows you to create Attachment on expense claim receipts by file name
[**create_receipt_history**](AccountingApi.md#create_receipt_history) | **PUT** /Receipts/{ReceiptID}/History | Allows you to retrieve a history records of an Receipt
[**create_repeating_invoice_attachment_by_file_name**](AccountingApi.md#create_repeating_invoice_attachment_by_file_name) | **PUT** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Allows you to create attachment on repeating invoices by file name
[**create_repeating_invoice_history**](AccountingApi.md#create_repeating_invoice_history) | **PUT** /RepeatingInvoices/{RepeatingInvoiceID}/History | Allows you to create history for a repeating invoice
[**create_tax_rate**](AccountingApi.md#create_tax_rate) | **PUT** /TaxRates | Allows you to create Tax Rates
[**create_tracking_category**](AccountingApi.md#create_tracking_category) | **PUT** /TrackingCategories | Allows you to create tracking categories
[**create_tracking_options**](AccountingApi.md#create_tracking_options) | **PUT** /TrackingCategories/{TrackingCategoryID}/Options | Allows you to create options for a specified tracking category
[**delete_account**](AccountingApi.md#delete_account) | **DELETE** /Accounts/{AccountID} | Allows you to delete a chart of accounts
[**delete_contact_group_contact**](AccountingApi.md#delete_contact_group_contact) | **DELETE** /ContactGroups/{ContactGroupID}/Contacts/{ContactID} | Allows you to delete a specific Contact from a Contract Group
[**delete_contact_group_contacts**](AccountingApi.md#delete_contact_group_contacts) | **DELETE** /ContactGroups/{ContactGroupID}/Contacts | Allows you to delete  all Contacts from a Contract Group
[**delete_item**](AccountingApi.md#delete_item) | **DELETE** /Items/{ItemID} | Allows you to delete a specified item
[**delete_linked_transaction**](AccountingApi.md#delete_linked_transaction) | **DELETE** /LinkedTransactions/{LinkedTransactionID} | Allows you to delete a specified linked transactions (billable expenses)
[**delete_payment**](AccountingApi.md#delete_payment) | **POST** /Payments/{PaymentID} | Allows you to update a specified payment for invoices and credit notes
[**delete_tracking_category**](AccountingApi.md#delete_tracking_category) | **DELETE** /TrackingCategories/{TrackingCategoryID} | Allows you to delete tracking categories
[**delete_tracking_options**](AccountingApi.md#delete_tracking_options) | **DELETE** /TrackingCategories/{TrackingCategoryID}/Options/{TrackingOptionID} | Allows you to delete a specified option for a specified tracking category
[**email_invoice**](AccountingApi.md#email_invoice) | **POST** /Invoices/{InvoiceID}/Email | Allows you to email a copy of invoice to related Contact
[**get_account**](AccountingApi.md#get_account) | **GET** /Accounts/{AccountID} | Allows you to retrieve a single chart of accounts
[**get_account_attachment_by_file_name**](AccountingApi.md#get_account_attachment_by_file_name) | **GET** /Accounts/{AccountID}/Attachments/{FileName} | Allows you to retrieve Attachment on Account by Filename
[**get_account_attachment_by_id**](AccountingApi.md#get_account_attachment_by_id) | **GET** /Accounts/{AccountID}/Attachments/{AttachmentID} | Allows you to retrieve specific Attachment on Account
[**get_account_attachments**](AccountingApi.md#get_account_attachments) | **GET** /Accounts/{AccountID}/Attachments | Allows you to retrieve Attachments for accounts
[**get_accounts**](AccountingApi.md#get_accounts) | **GET** /Accounts | Allows you to retrieve the full chart of accounts
[**get_bank_transaction**](AccountingApi.md#get_bank_transaction) | **GET** /BankTransactions/{BankTransactionID} | Allows you to retrieve a single spend or receive money transaction
[**get_bank_transaction_attachment_by_file_name**](AccountingApi.md#get_bank_transaction_attachment_by_file_name) | **GET** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Allows you to retrieve Attachments on BankTransaction by Filename
[**get_bank_transaction_attachment_by_id**](AccountingApi.md#get_bank_transaction_attachment_by_id) | **GET** /BankTransactions/{BankTransactionID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on a specific BankTransaction
[**get_bank_transaction_attachments**](AccountingApi.md#get_bank_transaction_attachments) | **GET** /BankTransactions/{BankTransactionID}/Attachments | Allows you to retrieve any attachments to bank transactions
[**get_bank_transactions**](AccountingApi.md#get_bank_transactions) | **GET** /BankTransactions | Allows you to retrieve any spend or receive money transactions
[**get_bank_transactions_history**](AccountingApi.md#get_bank_transactions_history) | **GET** /BankTransactions/{BankTransactionID}/History | Allows you to retrieve history from a bank transactions
[**get_bank_transfer**](AccountingApi.md#get_bank_transfer) | **GET** /BankTransfers/{BankTransferID} | Allows you to retrieve any bank transfers
[**get_bank_transfer_attachment_by_file_name**](AccountingApi.md#get_bank_transfer_attachment_by_file_name) | **GET** /BankTransfers/{BankTransferID}/Attachments/{FileName} | Allows you to retrieve Attachments on BankTransfer by file name
[**get_bank_transfer_attachment_by_id**](AccountingApi.md#get_bank_transfer_attachment_by_id) | **GET** /BankTransfers/{BankTransferID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on BankTransfer
[**get_bank_transfer_attachments**](AccountingApi.md#get_bank_transfer_attachments) | **GET** /BankTransfers/{BankTransferID}/Attachments | Allows you to retrieve Attachments from  bank transfers
[**get_bank_transfer_history**](AccountingApi.md#get_bank_transfer_history) | **GET** /BankTransfers/{BankTransferID}/History | Allows you to retrieve history from a bank transfers
[**get_bank_transfers**](AccountingApi.md#get_bank_transfers) | **GET** /BankTransfers | Allows you to retrieve all bank transfers
[**get_batch_payment_history**](AccountingApi.md#get_batch_payment_history) | **GET** /BatchPayments/{BatchPaymentID}/History | Allows you to retrieve history from a Batch Payment
[**get_batch_payments**](AccountingApi.md#get_batch_payments) | **GET** /BatchPayments | Retrieve either one or many BatchPayments for invoices
[**get_branding_theme**](AccountingApi.md#get_branding_theme) | **GET** /BrandingThemes/{BrandingThemeID} | Allows you to retrieve a specific BrandingThemes
[**get_branding_theme_payment_services**](AccountingApi.md#get_branding_theme_payment_services) | **GET** /BrandingThemes/{BrandingThemeID}/PaymentServices | Allows you to retrieve the Payment services for a Branding Theme
[**get_branding_themes**](AccountingApi.md#get_branding_themes) | **GET** /BrandingThemes | Allows you to retrieve all the BrandingThemes
[**get_contact**](AccountingApi.md#get_contact) | **GET** /Contacts/{ContactID} | Allows you to retrieve, add and update contacts in a Xero organisation
[**get_contact_attachment_by_file_name**](AccountingApi.md#get_contact_attachment_by_file_name) | **GET** /Contacts/{ContactID}/Attachments/{FileName} | Allows you to retrieve Attachments on Contacts by file name
[**get_contact_attachment_by_id**](AccountingApi.md#get_contact_attachment_by_id) | **GET** /Contacts/{ContactID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on Contacts
[**get_contact_attachments**](AccountingApi.md#get_contact_attachments) | **GET** /Contacts/{ContactID}/Attachments | Allows you to retrieve, add and update contacts in a Xero organisation
[**get_contact_cis_settings**](AccountingApi.md#get_contact_cis_settings) | **GET** /Contacts/{ContactID}/CISSettings | Allows you to retrieve CISSettings for a contact in a Xero organisation
[**get_contact_group**](AccountingApi.md#get_contact_group) | **GET** /ContactGroups/{ContactGroupID} | Allows you to retrieve a unique Contract Group by ID
[**get_contact_groups**](AccountingApi.md#get_contact_groups) | **GET** /ContactGroups | Allows you to retrieve the ContactID and Name of all the contacts in a contact group
[**get_contact_history**](AccountingApi.md#get_contact_history) | **GET** /Contacts/{ContactID}/History | Allows you to retrieve a history records of an Contact
[**get_contacts**](AccountingApi.md#get_contacts) | **GET** /Contacts | Allows you to retrieve, add and update contacts in a Xero organisation
[**get_credit_note**](AccountingApi.md#get_credit_note) | **GET** /CreditNotes/{CreditNoteID} | Allows you to retrieve a specific credit note
[**get_credit_note_as_pdf**](AccountingApi.md#get_credit_note_as_pdf) | **GET** /CreditNotes/{CreditNoteID}/pdf | Allows you to retrieve Credit Note as PDF files
[**get_credit_note_attachment_by_file_name**](AccountingApi.md#get_credit_note_attachment_by_file_name) | **GET** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Allows you to retrieve Attachments on CreditNote by file name
[**get_credit_note_attachment_by_id**](AccountingApi.md#get_credit_note_attachment_by_id) | **GET** /CreditNotes/{CreditNoteID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on CreditNote
[**get_credit_note_attachments**](AccountingApi.md#get_credit_note_attachments) | **GET** /CreditNotes/{CreditNoteID}/Attachments | Allows you to retrieve Attachments for credit notes
[**get_credit_note_history**](AccountingApi.md#get_credit_note_history) | **GET** /CreditNotes/{CreditNoteID}/History | Allows you to retrieve a history records of an CreditNote
[**get_credit_notes**](AccountingApi.md#get_credit_notes) | **GET** /CreditNotes | Allows you to retrieve any credit notes
[**get_currencies**](AccountingApi.md#get_currencies) | **GET** /Currencies | Allows you to retrieve currencies for your organisation
[**get_employee**](AccountingApi.md#get_employee) | **GET** /Employees/{EmployeeID} | Allows you to retrieve a specific employee used in Xero payrun
[**get_employees**](AccountingApi.md#get_employees) | **GET** /Employees | Allows you to retrieve employees used in Xero payrun
[**get_expense_claim**](AccountingApi.md#get_expense_claim) | **GET** /ExpenseClaims/{ExpenseClaimID} | Allows you to retrieve a specified expense claim
[**get_expense_claim_history**](AccountingApi.md#get_expense_claim_history) | **GET** /ExpenseClaims/{ExpenseClaimID}/History | Allows you to retrieve a history records of an ExpenseClaim
[**get_expense_claims**](AccountingApi.md#get_expense_claims) | **GET** /ExpenseClaims | Allows you to retrieve expense claims
[**get_invoice**](AccountingApi.md#get_invoice) | **GET** /Invoices/{InvoiceID} | Allows you to retrieve a specified sales invoice or purchase bill
[**get_invoice_as_pdf**](AccountingApi.md#get_invoice_as_pdf) | **GET** /Invoices/{InvoiceID}/pdf | Allows you to retrieve invoices or purchase bills as PDF files
[**get_invoice_attachment_by_file_name**](AccountingApi.md#get_invoice_attachment_by_file_name) | **GET** /Invoices/{InvoiceID}/Attachments/{FileName} | Allows you to retrieve Attachment on invoices or purchase bills by it&#39;s filename
[**get_invoice_attachment_by_id**](AccountingApi.md#get_invoice_attachment_by_id) | **GET** /Invoices/{InvoiceID}/Attachments/{AttachmentID} | Allows you to retrieve a specified Attachment on invoices or purchase bills by it&#39;s ID
[**get_invoice_attachments**](AccountingApi.md#get_invoice_attachments) | **GET** /Invoices/{InvoiceID}/Attachments | Allows you to retrieve Attachments on invoices or purchase bills
[**get_invoice_history**](AccountingApi.md#get_invoice_history) | **GET** /Invoices/{InvoiceID}/History | Allows you to retrieve a history records of an invoice
[**get_invoice_reminders**](AccountingApi.md#get_invoice_reminders) | **GET** /InvoiceReminders/Settings | Allows you to retrieve invoice reminder settings
[**get_invoices**](AccountingApi.md#get_invoices) | **GET** /Invoices | Allows you to retrieve any sales invoices or purchase bills
[**get_item**](AccountingApi.md#get_item) | **GET** /Items/{ItemID} | Allows you to retrieve a specified item
[**get_item_history**](AccountingApi.md#get_item_history) | **GET** /Items/{ItemID}/History | Allows you to retrieve history for items
[**get_items**](AccountingApi.md#get_items) | **GET** /Items | Allows you to retrieve any items
[**get_journal**](AccountingApi.md#get_journal) | **GET** /Journals/{JournalID} | Allows you to retrieve a specified journals.
[**get_journals**](AccountingApi.md#get_journals) | **GET** /Journals | Allows you to retrieve any journals.
[**get_linked_transaction**](AccountingApi.md#get_linked_transaction) | **GET** /LinkedTransactions/{LinkedTransactionID} | Allows you to retrieve a specified linked transactions (billable expenses)
[**get_linked_transactions**](AccountingApi.md#get_linked_transactions) | **GET** /LinkedTransactions | Retrieve linked transactions (billable expenses)
[**get_manual_journal**](AccountingApi.md#get_manual_journal) | **GET** /ManualJournals/{ManualJournalID} | Allows you to retrieve a specified manual journals
[**get_manual_journal_attachment_by_file_name**](AccountingApi.md#get_manual_journal_attachment_by_file_name) | **GET** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Allows you to retrieve specified Attachment on ManualJournal by file name
[**get_manual_journal_attachment_by_id**](AccountingApi.md#get_manual_journal_attachment_by_id) | **GET** /ManualJournals/{ManualJournalID}/Attachments/{AttachmentID} | Allows you to retrieve specified Attachment on ManualJournals
[**get_manual_journal_attachments**](AccountingApi.md#get_manual_journal_attachments) | **GET** /ManualJournals/{ManualJournalID}/Attachments | Allows you to retrieve Attachment for manual journals
[**get_manual_journals**](AccountingApi.md#get_manual_journals) | **GET** /ManualJournals | Allows you to retrieve any manual journals
[**get_online_invoice**](AccountingApi.md#get_online_invoice) | **GET** /Invoices/{InvoiceID}/OnlineInvoice | Allows you to retrieve a URL to an online invoice
[**get_organisation_cis_settings**](AccountingApi.md#get_organisation_cis_settings) | **GET** /Organisation/{OrganisationID}/CISSettings | Allows you To verify if an organisation is using contruction industry scheme, you can retrieve the CIS settings for the organistaion.
[**get_organisations**](AccountingApi.md#get_organisations) | **GET** /Organisation | Allows you to retrieve Organisation details
[**get_overpayment**](AccountingApi.md#get_overpayment) | **GET** /Overpayments/{OverpaymentID} | Allows you to retrieve a specified overpayments
[**get_overpayment_history**](AccountingApi.md#get_overpayment_history) | **GET** /Overpayments/{OverpaymentID}/History | Allows you to retrieve a history records of an Overpayment
[**get_overpayments**](AccountingApi.md#get_overpayments) | **GET** /Overpayments | Allows you to retrieve overpayments
[**get_payment**](AccountingApi.md#get_payment) | **GET** /Payments/{PaymentID} | Allows you to retrieve a specified payment for invoices and credit notes
[**get_payment_history**](AccountingApi.md#get_payment_history) | **GET** /Payments/{PaymentID}/History | Allows you to retrieve history records of a payment
[**get_payment_services**](AccountingApi.md#get_payment_services) | **GET** /PaymentServices | Allows you to retrieve payment services
[**get_payments**](AccountingApi.md#get_payments) | **GET** /Payments | Allows you to retrieve payments for invoices and credit notes
[**get_prepayment**](AccountingApi.md#get_prepayment) | **GET** /Prepayments/{PrepaymentID} | Allows you to retrieve a specified prepayments
[**get_prepayment_history**](AccountingApi.md#get_prepayment_history) | **GET** /Prepayments/{PrepaymentID}/History | Allows you to retrieve a history records of an Prepayment
[**get_prepayments**](AccountingApi.md#get_prepayments) | **GET** /Prepayments | Allows you to retrieve prepayments
[**get_purchase_order**](AccountingApi.md#get_purchase_order) | **GET** /PurchaseOrders/{PurchaseOrderID} | Allows you to retrieve a specified purchase orders
[**get_purchase_order_history**](AccountingApi.md#get_purchase_order_history) | **GET** /PurchaseOrders/{PurchaseOrderID}/History | Allows you to retrieve history for PurchaseOrder
[**get_purchase_orders**](AccountingApi.md#get_purchase_orders) | **GET** /PurchaseOrders | Allows you to retrieve purchase orders
[**get_receipt**](AccountingApi.md#get_receipt) | **GET** /Receipts/{ReceiptID} | Allows you to retrieve a specified draft expense claim receipts
[**get_receipt_attachment_by_file_name**](AccountingApi.md#get_receipt_attachment_by_file_name) | **GET** /Receipts/{ReceiptID}/Attachments/{FileName} | Allows you to retrieve Attachments on expense claim receipts by file name
[**get_receipt_attachment_by_id**](AccountingApi.md#get_receipt_attachment_by_id) | **GET** /Receipts/{ReceiptID}/Attachments/{AttachmentID} | Allows you to retrieve Attachments on expense claim receipts by ID
[**get_receipt_attachments**](AccountingApi.md#get_receipt_attachments) | **GET** /Receipts/{ReceiptID}/Attachments | Allows you to retrieve Attachments for expense claim receipts
[**get_receipt_history**](AccountingApi.md#get_receipt_history) | **GET** /Receipts/{ReceiptID}/History | Allows you to retrieve a history records of an Receipt
[**get_receipts**](AccountingApi.md#get_receipts) | **GET** /Receipts | Allows you to retrieve draft expense claim receipts for any user
[**get_repeating_invoice**](AccountingApi.md#get_repeating_invoice) | **GET** /RepeatingInvoices/{RepeatingInvoiceID} | Allows you to retrieve a specified repeating invoice
[**get_repeating_invoice_attachment_by_file_name**](AccountingApi.md#get_repeating_invoice_attachment_by_file_name) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Allows you to retrieve specified attachment on repeating invoices by file name
[**get_repeating_invoice_attachment_by_id**](AccountingApi.md#get_repeating_invoice_attachment_by_id) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{AttachmentID} | Allows you to retrieve a specified Attachments on repeating invoices
[**get_repeating_invoice_attachments**](AccountingApi.md#get_repeating_invoice_attachments) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments | Allows you to retrieve Attachments on repeating invoice
[**get_repeating_invoice_history**](AccountingApi.md#get_repeating_invoice_history) | **GET** /RepeatingInvoices/{RepeatingInvoiceID}/History | Allows you to retrieve history for a repeating invoice
[**get_repeating_invoices**](AccountingApi.md#get_repeating_invoices) | **GET** /RepeatingInvoices | Allows you to retrieve any repeating invoices
[**get_report_aged_payables_by_contact**](AccountingApi.md#get_report_aged_payables_by_contact) | **GET** /Reports/AgedPayablesByContact | Allows you to retrieve report for AgedPayablesByContact
[**get_report_aged_receivables_by_contact**](AccountingApi.md#get_report_aged_receivables_by_contact) | **GET** /Reports/AgedReceivablesByContact | Allows you to retrieve report for AgedReceivablesByContact
[**get_report_ba_sor_gst**](AccountingApi.md#get_report_ba_sor_gst) | **GET** /Reports/{ReportID} | Allows you to retrieve report for BAS only valid for AU orgs
[**get_report_ba_sor_gst_list**](AccountingApi.md#get_report_ba_sor_gst_list) | **GET** /Reports | Allows you to retrieve report for BAS only valid for AU orgs
[**get_report_balance_sheet**](AccountingApi.md#get_report_balance_sheet) | **GET** /Reports/BalanceSheet | Allows you to retrieve report for BalanceSheet
[**get_report_bank_summary**](AccountingApi.md#get_report_bank_summary) | **GET** /Reports/BankSummary | Allows you to retrieve report for BankSummary
[**get_report_budget_summary**](AccountingApi.md#get_report_budget_summary) | **GET** /Reports/BudgetSummary | Allows you to retrieve report for Budget Summary
[**get_report_executive_summary**](AccountingApi.md#get_report_executive_summary) | **GET** /Reports/ExecutiveSummary | Allows you to retrieve report for ExecutiveSummary
[**get_report_profit_and_loss**](AccountingApi.md#get_report_profit_and_loss) | **GET** /Reports/ProfitAndLoss | Allows you to retrieve report for ProfitAndLoss
[**get_report_ten_ninety_nine**](AccountingApi.md#get_report_ten_ninety_nine) | **GET** /Reports/TenNinetyNine | Allows you to retrieve report for TenNinetyNine
[**get_report_trial_balance**](AccountingApi.md#get_report_trial_balance) | **GET** /Reports/TrialBalance | Allows you to retrieve report for TrialBalance
[**get_tax_rates**](AccountingApi.md#get_tax_rates) | **GET** /TaxRates | Allows you to retrieve Tax Rates
[**get_tracking_categories**](AccountingApi.md#get_tracking_categories) | **GET** /TrackingCategories | Allows you to retrieve tracking categories and options
[**get_tracking_category**](AccountingApi.md#get_tracking_category) | **GET** /TrackingCategories/{TrackingCategoryID} | Allows you to retrieve tracking categories and options for specified category
[**get_user**](AccountingApi.md#get_user) | **GET** /Users/{UserID} | Allows you to retrieve a specified user
[**get_users**](AccountingApi.md#get_users) | **GET** /Users | Allows you to retrieve users
[**update_account**](AccountingApi.md#update_account) | **POST** /Accounts/{AccountID} | Allows you to update a chart of accounts
[**update_account_attachment_by_file_name**](AccountingApi.md#update_account_attachment_by_file_name) | **POST** /Accounts/{AccountID}/Attachments/{FileName} | Allows you to update Attachment on Account by Filename
[**update_bank_transaction**](AccountingApi.md#update_bank_transaction) | **POST** /BankTransactions/{BankTransactionID} | Allows you to update a single spend or receive money transaction
[**update_bank_transaction_attachment_by_file_name**](AccountingApi.md#update_bank_transaction_attachment_by_file_name) | **POST** /BankTransactions/{BankTransactionID}/Attachments/{FileName} | Allows you to update an Attachment on BankTransaction by Filename
[**update_bank_transfer_attachment_by_file_name**](AccountingApi.md#update_bank_transfer_attachment_by_file_name) | **POST** /BankTransfers/{BankTransferID}/Attachments/{FileName} | 
[**update_contact**](AccountingApi.md#update_contact) | **POST** /Contacts/{ContactID} | 
[**update_contact_attachment_by_file_name**](AccountingApi.md#update_contact_attachment_by_file_name) | **POST** /Contacts/{ContactID}/Attachments/{FileName} | 
[**update_contact_group**](AccountingApi.md#update_contact_group) | **POST** /ContactGroups/{ContactGroupID} | Allows you to update a Contract Group
[**update_credit_note**](AccountingApi.md#update_credit_note) | **POST** /CreditNotes/{CreditNoteID} | Allows you to update a specific credit note
[**update_credit_note_attachment_by_file_name**](AccountingApi.md#update_credit_note_attachment_by_file_name) | **POST** /CreditNotes/{CreditNoteID}/Attachments/{FileName} | Allows you to update Attachments on CreditNote by file name
[**update_employee**](AccountingApi.md#update_employee) | **POST** /Employees/{EmployeeID} | Allows you to update a specific employee used in Xero payrun
[**update_expense_claim**](AccountingApi.md#update_expense_claim) | **POST** /ExpenseClaims/{ExpenseClaimID} | Allows you to update specified expense claims
[**update_invoice**](AccountingApi.md#update_invoice) | **POST** /Invoices/{InvoiceID} | Allows you to update a specified sales invoices or purchase bills
[**update_invoice_attachment_by_file_name**](AccountingApi.md#update_invoice_attachment_by_file_name) | **POST** /Invoices/{InvoiceID}/Attachments/{FileName} | Allows you to update Attachment on invoices or purchase bills by it&#39;s filename
[**update_item**](AccountingApi.md#update_item) | **POST** /Items/{ItemID} | Allows you to udpate a specified item
[**update_linked_transaction**](AccountingApi.md#update_linked_transaction) | **POST** /LinkedTransactions/{LinkedTransactionID} | Allows you to update a specified linked transactions (billable expenses)
[**update_manual_journal**](AccountingApi.md#update_manual_journal) | **POST** /ManualJournals/{ManualJournalID} | Allows you to update a specified manual journal
[**update_manual_journal_attachment_by_file_name**](AccountingApi.md#update_manual_journal_attachment_by_file_name) | **POST** /ManualJournals/{ManualJournalID}/Attachments/{FileName} | Allows you to update a specified Attachment on ManualJournal by file name
[**update_purchase_order**](AccountingApi.md#update_purchase_order) | **POST** /PurchaseOrders/{PurchaseOrderID} | Allows you to update a specified purchase order
[**update_receipt**](AccountingApi.md#update_receipt) | **POST** /Receipts/{ReceiptID} | Allows you to retrieve a specified draft expense claim receipts
[**update_receipt_attachment_by_file_name**](AccountingApi.md#update_receipt_attachment_by_file_name) | **POST** /Receipts/{ReceiptID}/Attachments/{FileName} | Allows you to update Attachment on expense claim receipts by file name
[**update_repeating_invoice_attachment_by_file_name**](AccountingApi.md#update_repeating_invoice_attachment_by_file_name) | **POST** /RepeatingInvoices/{RepeatingInvoiceID}/Attachments/{FileName} | Allows you to update specified attachment on repeating invoices by file name
[**update_tax_rate**](AccountingApi.md#update_tax_rate) | **POST** /TaxRates | Allows you to update Tax Rates
[**update_tracking_category**](AccountingApi.md#update_tracking_category) | **POST** /TrackingCategories/{TrackingCategoryID} | Allows you to update tracking categories


# **create_account**
> Accounts create_account(account)

Allows you to create a new chart of accounts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account = { "Code":"123456", "Name":"Foobar", "Type":"EXPENSE", "Description":"Hello World" } # Account | Request of type Account

try:
    # Allows you to create a new chart of accounts
    api_response = api_instance.create_account(account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**Account**](Account.md)| Request of type Account | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - created new Account and return response of type Accounts array with new Account |  -  |
**400** | Validation Error - some data was incorrect returns response of type Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account_attachment_by_file_name**
> Attachments create_account_attachment_by_file_name(account_id, file_name, body)

Allows you to create Attachment on Account

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account_id = 'account_id_example' # str | Unique identifier for Account object
file_name = 'file_name_example' # str | Name of the attachment
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to create Attachment on Account
    api_response = api_instance.create_account_attachment_by_file_name(account_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_account_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| Unique identifier for Account object | 
 **file_name** | **str**| Name of the attachment | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array of Attachment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transaction**
> BankTransactions create_bank_transaction(bank_transactions, summarize_errors=summarize_errors)

Allows you to create a spend or receive money transaction

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transactions = { "BankTransactions":[ { "Type":"SPEND", "Contact":{ "ContactID":"5cc8cf28-567e-4d43-b287-687cfcaec47c" }, "Lineitems":[ { "Description":"Foobar", "Quantity":1.0, "UnitAmount":20.0, "AccountCode":"400" } ], "BankAccount":{ "Code":"088" } } ] } # BankTransactions | 
summarize_errors = True # bool | response format that shows validation errors for each bank transaction (optional)

try:
    # Allows you to create a spend or receive money transaction
    api_response = api_instance.create_bank_transaction(bank_transactions, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transactions** | [**BankTransactions**](BankTransactions.md)|  | 
 **summarize_errors** | **bool**| response format that shows validation errors for each bank transaction | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type BankTransactions array with new BankTransaction |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transaction_attachment_by_file_name**
> Attachments create_bank_transaction_attachment_by_file_name(bank_transaction_id, file_name, body)

Allows you to createa an Attachment on BankTransaction by Filename

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction
file_name = 'file_name_example' # str | The name of the file being attached
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to createa an Attachment on BankTransaction by Filename
    api_response = api_instance.create_bank_transaction_attachment_by_file_name(bank_transaction_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transaction_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **file_name** | **str**| The name of the file being attached | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of Attachments array of Attachment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transaction_history_record**
> HistoryRecords create_bank_transaction_history_record(bank_transaction_id, history_records)

Allows you to create history record for a bank transactions

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction
history_records = openapi_client.HistoryRecords() # HistoryRecords | 

try:
    # Allows you to create history record for a bank transactions
    api_response = api_instance.create_bank_transaction_history_record(bank_transaction_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transaction_history_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transfer**
> BankTransfers create_bank_transfer(bank_transfers)

Allows you to create a bank transfers

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfers = { "BankTransfers":[ { "FromBankAccount":{ "Code":"090", "Name":"My Savings", "AccountID":"7e5e243b-9fcd-4aef-8e3a-c70be1e39bfa", "Type":"BANK", "BankAccountNumber":"123455", "Status":"ACTIVE", "BankAccountType":"BANK", "CurrencyCode":"USD", "TaxType":"NONE", "EnablePaymentsToAccount":false, "ShowInExpenseClaims":false, "Class":"ASSET", "ReportingCode":"ASS", "ReportingCodeName":"Assets", "HasAttachments":false, "UpdatedDateUTC":"2016-10-17T13:45:33.993-07:00" }, "ToBankAccount":{ "Code":"088", "Name":"Business Wells Fargo", "AccountID":"6f7594f2-f059-4d56-9e67-47ac9733bfe9", "Type":"BANK", "BankAccountNumber":"123455", "Status":"ACTIVE", "BankAccountType":"BANK", "CurrencyCode":"USD", "TaxType":"NONE", "EnablePaymentsToAccount":false, "ShowInExpenseClaims":false, "Class":"ASSET", "ReportingCode":"ASS", "ReportingCodeName":"Assets", "HasAttachments":false, "UpdatedDateUTC":"2016-06-03T08:31:14.517-07:00" }, "Amount":"50.00" } ] } # BankTransfers | 

try:
    # Allows you to create a bank transfers
    api_response = api_instance.create_bank_transfer(bank_transfers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfers** | [**BankTransfers**](BankTransfers.md)|  | 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of BankTransfers array of one BankTransfer |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transfer_attachment_by_file_name**
> Attachments create_bank_transfer_attachment_by_file_name(bank_transfer_id, file_name, body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfer_id = 'bank_transfer_id_example' # str | Xero generated unique identifier for a bank transfer
file_name = 'file_name_example' # str | The name of the file being attached to a Bank Transfer
body = 'body_example' # str | Byte array of file in body of request

try:
    api_response = api_instance.create_bank_transfer_attachment_by_file_name(bank_transfer_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transfer_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **file_name** | **str**| The name of the file being attached to a Bank Transfer | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of Attachments array of 0 to N Attachment for a Bank Transfer |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bank_transfer_history_record**
> HistoryRecords create_bank_transfer_history_record(bank_transfer_id, history_records)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfer_id = 'bank_transfer_id_example' # str | Xero generated unique identifier for a bank transfer
history_records = openapi_client.HistoryRecords() # HistoryRecords | 

try:
    api_response = api_instance.create_bank_transfer_history_record(bank_transfer_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_bank_transfer_history_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response HistoryRecords array with the newly created HistoryRecord for a Bank Transfer |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_payment**
> BatchPayments create_batch_payment(batch_payments)

Create one or many BatchPayments for invoices

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
batch_payments = { "BatchPayments":[ { "Account":{ "AccountID":"5ec2f302-cd60-4f8b-a915-9229dd45e6fa" }, "Reference":"Foobar38515", "Date":"2019-02-22", "Amount":3.0, "Payments":[ { "Invoice":{ "LineItems":[
], "InvoiceID":"e6039672-b161-40cd-b07b-a0178e7186ad" }, "Account":{ "AccountID":"5ec2f302-cd60-4f8b-a915-9229dd45e6fa" }, "Date":"2019-02-22", "Amount":1.0 }, { "Invoice":{ "LineItems":[
], "InvoiceID":"e4abafb4-1f5b-4d9f-80b3-9a7b815bc302" }, "Account":{ "AccountID":"5ec2f302-cd60-4f8b-a915-9229dd45e6fa" }, "Date":"2019-02-22", "Amount":1.0 }, { "Invoice":{ "LineItems":[
], "InvoiceID":"3323652c-155e-433b-8a73-4dde7cfbf410" }, "Account":{ "AccountID":"5ec2f302-cd60-4f8b-a915-9229dd45e6fa" }, "Date":"2019-02-22", "Amount":1.0 } ] } ] } # BatchPayments | Request of type BatchPayments containing a Payments array with one or more Payment objects

try:
    # Create one or many BatchPayments for invoices
    api_response = api_instance.create_batch_payment(batch_payments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_batch_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_payments** | [**BatchPayments**](BatchPayments.md)| Request of type BatchPayments containing a Payments array with one or more Payment objects | 

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type BatchPayments array of BatchPayment objects |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_payment_history_record**
> HistoryRecords create_batch_payment_history_record(batch_payment_id, history_records)

Allows you to create a history record for a Batch Payment

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
batch_payment_id = 'batch_payment_id_example' # str | Unique identifier for BatchPayment
history_records = { "HistoryRecords":[ { "Details":"Hello World" } ] } # HistoryRecords | 

try:
    # Allows you to create a history record for a Batch Payment
    api_response = api_instance.create_batch_payment_history_record(batch_payment_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_batch_payment_history_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_payment_id** | [**str**](.md)| Unique identifier for BatchPayment | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_branding_theme_payment_services**
> PaymentServices create_branding_theme_payment_services(branding_theme_id, payment_service)

Allow for the creation of new custom payment service for specified Branding Theme

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
branding_theme_id = 'branding_theme_id_example' # str | Unique identifier for a Branding Theme
payment_service = { "PaymentServiceID":"dede7858-14e3-4a46-bf95-4d4cc491e645", "PaymentServiceName":"ACME Payments", "PaymentServiceUrl":"https://www.payupnow.com/", "PayNowText":"Pay Now" } # PaymentService | 

try:
    # Allow for the creation of new custom payment service for specified Branding Theme
    api_response = api_instance.create_branding_theme_payment_services(branding_theme_id, payment_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_branding_theme_payment_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branding_theme_id** | [**str**](.md)| Unique identifier for a Branding Theme | 
 **payment_service** | [**PaymentService**](PaymentService.md)|  | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type PaymentServices array with newly created PaymentService |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> Contacts create_contact(contact)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact = { "Name":"Foo9987", "EmailAddress":"sid32476@blah.com", "Phones":[ { "PhoneType":"MOBILE", "PhoneNumber":"555-1212", "PhoneAreaCode":"415" } ], "PaymentTerms":{ "Bills":{ "Day":15, "Type":"OFCURRENTMONTH" }, "Sales":{ "Day":10, "Type":"DAYSAFTERBILLMONTH" } } } # Contact | 

try:
    api_response = api_instance.create_contact(contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact** | [**Contact**](Contact.md)|  | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contacts array with newly created Contact |  -  |
**400** | Validation Error - some data was incorrect returns response of type Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_attachment_by_file_name**
> Attachments create_contact_attachment_by_file_name(contact_id, file_name, body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact
file_name = 'file_name_example' # str | Name for the file you are attaching
body = 'body_example' # str | Byte array of file in body of request

try:
    api_response = api_instance.create_contact_attachment_by_file_name(contact_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **file_name** | **str**| Name for the file you are attaching | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with an newly created Attachment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_group**
> ContactGroups create_contact_group(contact_groups=contact_groups)

Allows you to create a contact group

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_groups = { "ContactGroups":[ { "Name":"Suppliers" } ] } # ContactGroups |  (optional)

try:
    # Allows you to create a contact group
    api_response = api_instance.create_contact_group(contact_groups=contact_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_groups** | [**ContactGroups**](ContactGroups.md)|  | [optional] 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contact Groups array of newly created Contact Group |  -  |
**400** | Validation Error - some data was incorrect returns response of type Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_group_contacts**
> Contacts create_contact_group_contacts(contact_group_id, contacts=contacts)

Allows you to add Contacts to a Contract Group

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_group_id = 'contact_group_id_example' # str | Unique identifier for a Contact Group
contacts = { "Contacts":[ { "ContactID":"a3675fc4-f8dd-4f03-ba5b-f1870566bcd7" }, { "ContactID":"4e1753b9-018a-4775-b6aa-1bc7871cfee3" } ] } # Contacts |  (optional)

try:
    # Allows you to add Contacts to a Contract Group
    api_response = api_instance.create_contact_group_contacts(contact_group_id, contacts=contacts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact_group_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 
 **contacts** | [**Contacts**](Contacts.md)|  | [optional] 

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contacts array of added Contacts |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_history**
> HistoryRecords create_contact_history(contact_id, history_records)

Allows you to retrieve a history records of an Contact

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact
history_records = { "HistoryRecords":[ { "Details":"Hello World" } ] } # HistoryRecords | 

try:
    # Allows you to retrieve a history records of an Contact
    api_response = api_instance.create_contact_history(contact_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_contact_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type History Records array of newly created History Record for a specific Contact |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note**
> CreditNotes create_credit_note(summarize_errors=summarize_errors, credit_notes=credit_notes)

Allows you to create a credit note

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
summarize_errors = True # bool | shows validation errors for each credit note (optional)
credit_notes = { "CreditNotes":[ { "Type":"ACCPAYCREDIT", "Contact":{ "ContactID":"430fa14a-f945-44d3-9f97-5df5e28441b8" }, "Date":"2019-01-05", "LineItems":[ { "Description":"Foobar", "Quantity":2.0, "UnitAmount":20.0, "AccountCode":"400" } ] } ] } # CreditNotes |  (optional)

try:
    # Allows you to create a credit note
    api_response = api_instance.create_credit_note(summarize_errors=summarize_errors, credit_notes=credit_notes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarize_errors** | **bool**| shows validation errors for each credit note | [optional] 
 **credit_notes** | [**CreditNotes**](CreditNotes.md)|  | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Credit Notes array of newly created CreditNote |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note_allocation**
> Allocations create_credit_note_allocation(credit_note_id, allocations=allocations)

Allows you to create Allocation on CreditNote

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note
allocations = { "Allocations":[ { "Invoice":{ "LineItems":[
], "InvoiceID":"c45720a1-ade3-4a38-a064-d15489be6841" }, "Amount":1.0, "Date":"2019-03-05" } ] } # Allocations |  (optional)

try:
    # Allows you to create Allocation on CreditNote
    api_response = api_instance.create_credit_note_allocation(credit_note_id, allocations=allocations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_credit_note_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **allocations** | [**Allocations**](Allocations.md)|  | [optional] 

### Return type

[**Allocations**](Allocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Allocations array with newly created Allocation for specific Credit Note |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note_attachment_by_file_name**
> Attachments create_credit_note_attachment_by_file_name(credit_note_id, file_name, body)

Allows you to create Attachments on CreditNote by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note
file_name = 'file_name_example' # str | Name of the file you are attaching to Credit Note
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to create Attachments on CreditNote by file name
    api_response = api_instance.create_credit_note_attachment_by_file_name(credit_note_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_credit_note_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **file_name** | **str**| Name of the file you are attaching to Credit Note | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with newly created Attachment for specific Credit Note |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credit_note_history**
> HistoryRecords create_credit_note_history(credit_note_id, history_records)

Allows you to retrieve a history records of an CreditNote

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note
history_records = { "HistoryRecords":[ { "Details":"Hello World" } ] } # HistoryRecords | 

try:
    # Allows you to retrieve a history records of an CreditNote
    api_response = api_instance.create_credit_note_history(credit_note_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_credit_note_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with newly created HistoryRecord for specific Credit Note |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_currency**
> Currencies create_currency(currencies)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
currencies = { "Currencies":[ { "Code":"USD", "Description":"United States Dollar" } ] } # Currencies | 

try:
    api_response = api_instance.create_currency(currencies)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencies** | [**Currencies**](Currencies.md)|  | 

### Return type

[**Currencies**](Currencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsupported - return response incorrect exception, API is not able to create new Currency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_employee**
> Employees create_employee(employees)

Allows you to create new employees used in Xero payrun

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
employees = { "Employees":[ { "FirstName":"Nick", "LastName":"Fury", "ExternalLink":{ "Url":"http://twitter.com/#!/search/Nick+Fury" } } ] } # Employees | 

try:
    # Allows you to create new employees used in Xero payrun
    api_response = api_instance.create_employee(employees)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employees** | [**Employees**](Employees.md)|  | 

### Return type

[**Employees**](Employees.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Employees array with new Employee |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_expense_claim**
> ExpenseClaims create_expense_claim(expense_claims, summarize_errors=summarize_errors)

Allows you to retrieve expense claims

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
expense_claims = { "ExpenseClaims":[ { "Status":"SUBMITTED", "User":{ "UserID":"d1164823-0ac1-41ad-987b-b4e30fe0b273" }, "Receipts":[ { "Lineitems":[
], "ReceiptID":"dc1c7f6d-0a4c-402f-acac-551d62ce5816" } ] } ] } # ExpenseClaims | 
summarize_errors = True # bool | shows validation errors for each expense claim (optional)

try:
    # Allows you to retrieve expense claims
    api_response = api_instance.create_expense_claim(expense_claims, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_expense_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_claims** | [**ExpenseClaims**](ExpenseClaims.md)|  | 
 **summarize_errors** | **bool**| shows validation errors for each expense claim | [optional] 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ExpenseClaims array with newly created ExpenseClaim |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_expense_claim_history**
> HistoryRecords create_expense_claim_history(expense_claim_id, history_records)

Allows you to create a history records of an ExpenseClaim

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
expense_claim_id = 'expense_claim_id_example' # str | Unique identifier for a ExpenseClaim
history_records = { "HistoryRecords":[ { "Details":"Hello World" } ] } # HistoryRecords | 

try:
    # Allows you to create a history records of an ExpenseClaim
    api_response = api_instance.create_expense_claim_history(expense_claim_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_expense_claim_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_claim_id** | [**str**](.md)| Unique identifier for a ExpenseClaim | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Expense Claims |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice**
> Invoices create_invoice(invoices, summarize_errors=summarize_errors)

Allows you to create any sales invoices or purchase bills

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoices = { "Invoices":[ { "Type":"ACCREC", "Contact":{ "ContactID":"430fa14a-f945-44d3-9f97-5df5e28441b8" }, "LineItems":[ { "Description":"Acme Tires", "Quantity":2.0, "UnitAmount":20.0, "AccountCode":"200", "TaxType":"NONE", "LineAmount":40.0 } ], "Date":"2019-03-11", "DueDate":"2018-12-10", "Reference":"Website Design", "Status":"AUTHORISED" } ] } # Invoices | 
summarize_errors = True # bool | shows validation errors for each invoice (optional)

try:
    # Allows you to create any sales invoices or purchase bills
    api_response = api_instance.create_invoice(invoices, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoices** | [**Invoices**](Invoices.md)|  | 
 **summarize_errors** | **bool**| shows validation errors for each invoice | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Invoices array with newly created Invoice |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_attachment_by_file_name**
> Attachments create_invoice_attachment_by_file_name(invoice_id, file_name, body)

Allows you to create an Attachment on invoices or purchase bills by it's filename

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice
file_name = 'file_name_example' # str | Name of the file you are attaching
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to create an Attachment on invoices or purchase bills by it's filename
    api_response = api_instance.create_invoice_attachment_by_file_name(invoice_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **file_name** | **str**| Name of the file you are attaching | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with newly created Attachment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_history**
> HistoryRecords create_invoice_history(invoice_id, history_records)

Allows you to retrieve a history records of an invoice

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice
history_records = { "HistoryRecords":[ { "Details":"Hello World" } ] } # HistoryRecords | 

try:
    # Allows you to retrieve a history records of an invoice
    api_response = api_instance.create_invoice_history(invoice_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_invoice_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with newly created HistoryRecord for specific Invoice |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item**
> Items create_item(items)

Allows you to create an item

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
items = { "Items":[ { "Code":"abc65591", "Name":"Hello11350", "Description":"foobar" } ] } # Items | 

try:
    # Allows you to create an item
    api_response = api_instance.create_item(items)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **items** | [**Items**](Items.md)|  | 

### Return type

[**Items**](Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Items array with newly created Item |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_item_history**
> HistoryRecords create_item_history(item_id, history_records)

Allows you to create a history record for items

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
item_id = 'item_id_example' # str | Unique identifier for an Item
history_records = { "HistoryRecords":[ { "Details":"Hello World" } ] } # HistoryRecords | 

try:
    # Allows you to create a history record for items
    api_response = api_instance.create_item_history(item_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_item_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**str**](.md)| Unique identifier for an Item | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_linked_transaction**
> LinkedTransactions create_linked_transaction(linked_transactions)

Allows you to create linked transactions (billable expenses)

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
linked_transactions = { "LinkedTransactions":[ { "SourceTransactionID":"a848644a-f20f-4630-98c3-386bd7505631", "SourceLineItemID":"b0df260d-3cc8-4ced-9bd6-41924f624ed3" } ] } # LinkedTransactions | 

try:
    # Allows you to create linked transactions (billable expenses)
    api_response = api_instance.create_linked_transaction(linked_transactions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_linked_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_transactions** | [**LinkedTransactions**](LinkedTransactions.md)|  | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type LinkedTransactions array with newly created LinkedTransaction |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_manual_journal**
> ManualJournals create_manual_journal(manual_journals)

Allows you to create a manual journal

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
manual_journals = { "ManualJournals":[ { "Narration":"Foo bar", "JournalLines":[ { "LineAmount":100.0, "AccountCode":"400", "Description":"Hello there" }, { "LineAmount":-100.0, "AccountCode":"400", "Description":"Goodbye", "Tracking":[ { "Name":"Simpsons", "Option":"Bart" } ] } ], "Date":"2019-03-14" } ] } # ManualJournals | 

try:
    # Allows you to create a manual journal
    api_response = api_instance.create_manual_journal(manual_journals)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_manual_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_journals** | [**ManualJournals**](ManualJournals.md)|  | 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ManualJournals array with newly created ManualJournal |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_manual_journal_attachment_by_file_name**
> Attachments create_manual_journal_attachment_by_file_name(manual_journal_id, file_name, body)

Allows you to create a specified Attachment on ManualJournal by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
manual_journal_id = 'manual_journal_id_example' # str | Unique identifier for a ManualJournal
file_name = 'file_name_example' # str | The name of the file being attached to a ManualJournal
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to create a specified Attachment on ManualJournal by file name
    api_response = api_instance.create_manual_journal_attachment_by_file_name(manual_journal_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_manual_journal_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **file_name** | **str**| The name of the file being attached to a ManualJournal | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with a newly created Attachment for a ManualJournals |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_overpayment_allocation**
> Allocations create_overpayment_allocation(overpayment_id, allocations)

Allows you to retrieve Allocations for overpayments

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
overpayment_id = 'overpayment_id_example' # str | Unique identifier for a Overpayment
allocations = { "Allocations":[ { "Invoice":{ "LineItems":[
], "InvoiceID":"c45720a1-ade3-4a38-a064-d15489be6841" }, "Amount":1.0, "Date":"2019-03-12" } ] } # Allocations | 

try:
    # Allows you to retrieve Allocations for overpayments
    api_response = api_instance.create_overpayment_allocation(overpayment_id, allocations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_overpayment_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overpayment_id** | [**str**](.md)| Unique identifier for a Overpayment | 
 **allocations** | [**Allocations**](Allocations.md)|  | 

### Return type

[**Allocations**](Allocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Allocations array with all Allocation for Overpayments |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_overpayment_history**
> HistoryRecords create_overpayment_history(overpayment_id, history_records)

Allows you to create history records of an Overpayment

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
overpayment_id = 'overpayment_id_example' # str | Unique identifier for a Overpayment
history_records = openapi_client.HistoryRecords() # HistoryRecords | 

try:
    # Allows you to create history records of an Overpayment
    api_response = api_instance.create_overpayment_history(overpayment_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_overpayment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overpayment_id** | [**str**](.md)| Unique identifier for a Overpayment | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Overpayments |  -  |
**400** | A failed request due to validation error - API is not able to create HistoryRecord for Overpayments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment**
> Payments create_payment(payments)

Allows you to create payments for invoices and credit notes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
payments = { "Payments":[ { "Invoice":{ "LineItems":[
], "InvoiceID":"c7c37b83-ac95-45ea-88ba-8ad83a5f22fe" }, "Account":{ "Code":"970" }, "Date":"2019-03-12", "Amount":1.0 } ] } # Payments | 

try:
    # Allows you to create payments for invoices and credit notes
    api_response = api_instance.create_payment(payments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payments** | [**Payments**](Payments.md)|  | 

### Return type

[**Payments**](Payments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Payments array for newly created Payment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_history**
> HistoryRecords create_payment_history(payment_id, history_records)

Allows you to create a history record for a payment

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
payment_id = 'payment_id_example' # str | Unique identifier for a Payment
history_records = { "HistoryRecords":[ { "Details":"Hello World" } ] } # HistoryRecords | 

try:
    # Allows you to create a history record for a payment
    api_response = api_instance.create_payment_history(payment_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_payment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)| Unique identifier for a Payment | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Payments |  -  |
**400** | A failed request due to validation error - API is not able to create HistoryRecord for Payments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_service**
> PaymentServices create_payment_service(payment_services)

Allows you to create payment services

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
payment_services = { "PaymentServices":[ { "PaymentServiceName":"PayUpNow", "PaymentServiceUrl":"https://www.payupnow.com/", "PayNowText":"Time To Pay" } ] } # PaymentServices | 

try:
    # Allows you to create payment services
    api_response = api_instance.create_payment_service(payment_services)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_payment_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_services** | [**PaymentServices**](PaymentServices.md)|  | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type PaymentServices array for newly created PaymentService |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_prepayment_allocation**
> Allocations create_prepayment_allocation(prepayment_id, allocations)

Allows you to create an Allocation for prepayments

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
prepayment_id = 'prepayment_id_example' # str | 
allocations = { "Allocations":[ { "Invoice":{ "LineItems":[
], "InvoiceID":"c7c37b83-ac95-45ea-88ba-8ad83a5f22fe" }, "Amount":1.0, "Date":"2019-03-13" } ] } # Allocations | 

try:
    # Allows you to create an Allocation for prepayments
    api_response = api_instance.create_prepayment_allocation(prepayment_id, allocations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_prepayment_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepayment_id** | [**str**](.md)|  | 
 **allocations** | [**Allocations**](Allocations.md)|  | 

### Return type

[**Allocations**](Allocations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Allocations array of Allocation for all Prepayment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_prepayment_history**
> HistoryRecords create_prepayment_history(prepayment_id, history_records)

Allows you to create a history record for an Prepayment

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
prepayment_id = 'prepayment_id_example' # str | Unique identifier for a PrePayment
history_records = openapi_client.HistoryRecords() # HistoryRecords | 

try:
    # Allows you to create a history record for an Prepayment
    api_response = api_instance.create_prepayment_history(prepayment_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_prepayment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepayment_id** | [**str**](.md)| Unique identifier for a PrePayment | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array for newly created HistoryRecord for PrePayment |  -  |
**400** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Expense Claims |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_purchase_order**
> PurchaseOrders create_purchase_order(purchase_orders, summarize_errors=summarize_errors)

Allows you to create purchase orders

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
purchase_orders = { "PurchaseOrders":[ { "Contact":{ "ContactID":"430fa14a-f945-44d3-9f97-5df5e28441b8" }, "LineItems":[ { "Description":"Foobar", "Quantity":1.0, "UnitAmount":20.0, "AccountCode":"710" } ], "Date":"2019-03-13" } ] } # PurchaseOrders | 
summarize_errors = True # bool | shows validation errors for each purchase order. (optional)

try:
    # Allows you to create purchase orders
    api_response = api_instance.create_purchase_order(purchase_orders, summarize_errors=summarize_errors)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_orders** | [**PurchaseOrders**](PurchaseOrders.md)|  | 
 **summarize_errors** | **bool**| shows validation errors for each purchase order. | [optional] 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type PurchaseOrder array for specified PurchaseOrder |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_purchase_order_history**
> HistoryRecords create_purchase_order_history(purchase_order_id, history_records)

Allows you to create HistoryRecord for purchase orders

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
purchase_order_id = 'purchase_order_id_example' # str | Unique identifier for a PurchaseOrder
history_records = { "HistoryRecords":[ { "Details":"Hello World" } ] } # HistoryRecords | 

try:
    # Allows you to create HistoryRecord for purchase orders
    api_response = api_instance.create_purchase_order_history(purchase_order_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_purchase_order_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_id** | [**str**](.md)| Unique identifier for a PurchaseOrder | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array for newly created HistoryRecord for PurchaseOrder |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt**
> Receipts create_receipt(receipts)

Allows you to create draft expense claim receipts for any user

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipts = { "Receipts":[ { "Contact":{ "ContactID":"430fa14a-f945-44d3-9f97-5df5e28441b8" }, "Lineitems":[ { "Description":"Foobar", "Quantity":2.0, "UnitAmount":20.0, "AccountCode":"400", "TaxType":"NONE", "LineAmount":40.0 } ], "User":{ "UserID":"d1164823-0ac1-41ad-987b-b4e30fe0b273" }, "LineAmountTypes":"NoTax", "Status":"DRAFT" } ] } # Receipts | 

try:
    # Allows you to create draft expense claim receipts for any user
    api_response = api_instance.create_receipt(receipts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipts** | [**Receipts**](Receipts.md)|  | 

### Return type

[**Receipts**](Receipts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Receipts array for newly created Receipt |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt_attachment_by_file_name**
> Attachments create_receipt_attachment_by_file_name(receipt_id, file_name, body)

Allows you to create Attachment on expense claim receipts by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt
file_name = 'file_name_example' # str | The name of the file being attached to the Receipt
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to create Attachment on expense claim receipts by file name
    api_response = api_instance.create_receipt_attachment_by_file_name(receipt_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_receipt_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **file_name** | **str**| The name of the file being attached to the Receipt | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with newly created Attachment for a specified Receipt |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_receipt_history**
> HistoryRecords create_receipt_history(receipt_id, history_records)

Allows you to retrieve a history records of an Receipt

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt
history_records = openapi_client.HistoryRecords() # HistoryRecords | 

try:
    # Allows you to retrieve a history records of an Receipt
    api_response = api_instance.create_receipt_history(receipt_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_receipt_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Receipts |  -  |
**400** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Receipts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repeating_invoice_attachment_by_file_name**
> Attachments create_repeating_invoice_attachment_by_file_name(repeating_invoice_id, file_name, body)

Allows you to create attachment on repeating invoices by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
repeating_invoice_id = 'repeating_invoice_id_example' # str | Unique identifier for a Repeating Invoice
file_name = 'file_name_example' # str | The name of the file being attached to a Repeating Invoice
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to create attachment on repeating invoices by file name
    api_response = api_instance.create_repeating_invoice_attachment_by_file_name(repeating_invoice_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_repeating_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **file_name** | **str**| The name of the file being attached to a Repeating Invoice | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with updated Attachment for a specified Repeating Invoice |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repeating_invoice_history**
> HistoryRecords create_repeating_invoice_history(repeating_invoice_id, history_records)

Allows you to create history for a repeating invoice

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
repeating_invoice_id = 'repeating_invoice_id_example' # str | Unique identifier for a Repeating Invoice
history_records = openapi_client.HistoryRecords() # HistoryRecords | 

try:
    # Allows you to create history for a repeating invoice
    api_response = api_instance.create_repeating_invoice_history(repeating_invoice_id, history_records)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_repeating_invoice_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **history_records** | [**HistoryRecords**](HistoryRecords.md)|  | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Unsupported - return response incorrect exception, API is not able to create HistoryRecord for Repeating Invoice |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tax_rate**
> TaxRates create_tax_rate(tax_rates)

Allows you to create Tax Rates

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
tax_rates = { "TaxRates":[ { "Name":"SDKTax29067", "TaxComponents":[ { "Name":"State Tax", "Rate":2.25 } ], "ReportTaxType":"INPUT" } ] } # TaxRates | 

try:
    # Allows you to create Tax Rates
    api_response = api_instance.create_tax_rate(tax_rates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_tax_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rates** | [**TaxRates**](TaxRates.md)|  | 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TaxRates array newly created TaxRate |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tracking_category**
> TrackingCategories create_tracking_category(tracking_category)

Allows you to create tracking categories

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
tracking_category = { "Name":"FooBar" } # TrackingCategory | 

try:
    # Allows you to create tracking categories
    api_response = api_instance.create_tracking_category(tracking_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_category** | [**TrackingCategory**](TrackingCategory.md)|  | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TrackingCategories array of newly created TrackingCategory |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tracking_options**
> TrackingOptions create_tracking_options(tracking_category_id, tracking_option)

Allows you to create options for a specified tracking category

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
tracking_category_id = 'tracking_category_id_example' # str | Unique identifier for a TrackingCategory
tracking_option = { "Name":"Bar40423" } # TrackingOption | 

try:
    # Allows you to create options for a specified tracking category
    api_response = api_instance.create_tracking_options(tracking_category_id, tracking_option)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->create_tracking_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 
 **tracking_option** | [**TrackingOption**](TrackingOption.md)|  | 

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TrackingOptions array of options for a specified category |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_account**
> Accounts delete_account(account_id)

Allows you to delete a chart of accounts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account_id = 'account_id_example' # str | Unique identifier for retrieving single object

try:
    # Allows you to delete a chart of accounts
    api_response = api_instance.delete_account(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| Unique identifier for retrieving single object | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - delete existing Account and return response of type Accounts array with deleted Account |  -  |
**400** | Validation Error - some data was incorrect returns response of type Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_group_contact**
> delete_contact_group_contact(contact_group_id, contact_id)

Allows you to delete a specific Contact from a Contract Group

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_group_id = 'contact_group_id_example' # str | Unique identifier for a Contact Group
contact_id = 'contact_id_example' # str | Unique identifier for a Contact

try:
    # Allows you to delete a specific Contact from a Contract Group
    api_instance.delete_contact_group_contact(contact_group_id, contact_id)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_contact_group_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_group_contacts**
> delete_contact_group_contacts(contact_group_id)

Allows you to delete  all Contacts from a Contract Group

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_group_id = 'contact_group_id_example' # str | Unique identifier for a Contact Group

try:
    # Allows you to delete  all Contacts from a Contract Group
    api_instance.delete_contact_group_contacts(contact_group_id)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_contact_group_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response 204 no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> delete_item(item_id)

Allows you to delete a specified item

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
item_id = 'item_id_example' # str | Unique identifier for an Item

try:
    # Allows you to delete a specified item
    api_instance.delete_item(item_id)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**str**](.md)| Unique identifier for an Item | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_transaction**
> delete_linked_transaction(linked_transaction_id)

Allows you to delete a specified linked transactions (billable expenses)

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
linked_transaction_id = 'linked_transaction_id_example' # str | Unique identifier for a LinkedTransaction

try:
    # Allows you to delete a specified linked transactions (billable expenses)
    api_instance.delete_linked_transaction(linked_transaction_id)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_linked_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_transaction_id** | [**str**](.md)| Unique identifier for a LinkedTransaction | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment**
> Payments delete_payment(payment_id, payments)

Allows you to update a specified payment for invoices and credit notes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
payment_id = 'payment_id_example' # str | Unique identifier for a Payment
payments = { "Payments":[ { "Status":"DELETED" } ] } # Payments | 

try:
    # Allows you to update a specified payment for invoices and credit notes
    api_response = api_instance.delete_payment(payment_id, payments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)| Unique identifier for a Payment | 
 **payments** | [**Payments**](Payments.md)|  | 

### Return type

[**Payments**](Payments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Payments array for updated Payment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracking_category**
> TrackingCategories delete_tracking_category(tracking_category_id)

Allows you to delete tracking categories

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
tracking_category_id = 'tracking_category_id_example' # str | Unique identifier for a TrackingCategory

try:
    # Allows you to delete tracking categories
    api_response = api_instance.delete_tracking_category(tracking_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TrackingCategories array of deleted TrackingCategory |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tracking_options**
> TrackingOptions delete_tracking_options(tracking_category_id, tracking_option_id)

Allows you to delete a specified option for a specified tracking category

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
tracking_category_id = 'tracking_category_id_example' # str | Unique identifier for a TrackingCategory
tracking_option_id = 'tracking_option_id_example' # str | Unique identifier for a Tracking Option

try:
    # Allows you to delete a specified option for a specified tracking category
    api_response = api_instance.delete_tracking_options(tracking_category_id, tracking_option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->delete_tracking_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 
 **tracking_option_id** | [**str**](.md)| Unique identifier for a Tracking Option | 

### Return type

[**TrackingOptions**](TrackingOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TrackingOptions array of remaining options for a specified category |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_invoice**
> email_invoice(invoice_id, request_empty)

Allows you to email a copy of invoice to related Contact

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice
request_empty = openapi_client.RequestEmpty() # RequestEmpty | 

try:
    # Allows you to email a copy of invoice to related Contact
    api_instance.email_invoice(invoice_id, request_empty)
except ApiException as e:
    print("Exception when calling AccountingApi->email_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **request_empty** | [**RequestEmpty**](RequestEmpty.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success - return response 204 no content |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Accounts get_account(account_id)

Allows you to retrieve a single chart of accounts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account_id = 'account_id_example' # str | Unique identifier for retrieving single object

try:
    # Allows you to retrieve a single chart of accounts
    api_response = api_instance.get_account(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| Unique identifier for retrieving single object | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Accounts array with one Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_attachment_by_file_name**
> file get_account_attachment_by_file_name(account_id, file_name, content_type)

Allows you to retrieve Attachment on Account by Filename

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account_id = 'account_id_example' # str | Unique identifier for Account object
file_name = 'file_name_example' # str | Name of the attachment
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachment on Account by Filename
    api_response = api_instance.get_account_attachment_by_file_name(account_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_account_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| Unique identifier for Account object | 
 **file_name** | **str**| Name of the attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Account as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_attachment_by_id**
> file get_account_attachment_by_id(account_id, attachment_id, content_type)

Allows you to retrieve specific Attachment on Account

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account_id = 'account_id_example' # str | Unique identifier for Account object
attachment_id = 'attachment_id_example' # str | Unique identifier for Attachment object
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve specific Attachment on Account
    api_response = api_instance.get_account_attachment_by_id(account_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_account_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| Unique identifier for Account object | 
 **attachment_id** | [**str**](.md)| Unique identifier for Attachment object | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Account as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_attachments**
> Attachments get_account_attachments(account_id)

Allows you to retrieve Attachments for accounts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account_id = 'account_id_example' # str | Unique identifier for Account object

try:
    # Allows you to retrieve Attachments for accounts
    api_response = api_instance.get_account_attachments(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_account_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| Unique identifier for Account object | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array of Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> Accounts get_accounts(if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve the full chart of accounts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve the full chart of accounts
    api_response = api_instance.get_accounts(if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Accounts array with 0 to n Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transaction**
> BankTransactions get_bank_transaction(bank_transaction_id)

Allows you to retrieve a single spend or receive money transaction

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction

try:
    # Allows you to retrieve a single spend or receive money transaction
    api_response = api_instance.get_bank_transaction(bank_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type BankTransactions array with a specific BankTransaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transaction_attachment_by_file_name**
> file get_bank_transaction_attachment_by_file_name(bank_transaction_id, file_name, content_type)

Allows you to retrieve Attachments on BankTransaction by Filename

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction
file_name = 'file_name_example' # str | The name of the file being attached
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on BankTransaction by Filename
    api_response = api_instance.get_bank_transaction_attachment_by_file_name(bank_transaction_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transaction_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **file_name** | **str**| The name of the file being attached | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for BankTransaction as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transaction_attachment_by_id**
> file get_bank_transaction_attachment_by_id(bank_transaction_id, attachment_id, content_type)

Allows you to retrieve Attachments on a specific BankTransaction

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction
attachment_id = 'attachment_id_example' # str | Xero generated unique identifier for an attachment
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on a specific BankTransaction
    api_response = api_instance.get_bank_transaction_attachment_by_id(bank_transaction_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transaction_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **attachment_id** | [**str**](.md)| Xero generated unique identifier for an attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for BankTransaction as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transaction_attachments**
> Attachments get_bank_transaction_attachments(bank_transaction_id)

Allows you to retrieve any attachments to bank transactions

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction

try:
    # Allows you to retrieve any attachments to bank transactions
    api_response = api_instance.get_bank_transaction_attachments(bank_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transaction_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with 0 to n Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transactions**
> BankTransactions get_bank_transactions(if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)

Allows you to retrieve any spend or receive money transactions

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 bank transactions will be returned in a single API call with line items shown for each bank transaction (optional)
unitdp = 56 # int | e.g. unitdp=4 – You can opt in to use four decimal places for unit amounts (optional)

try:
    # Allows you to retrieve any spend or receive money transactions
    api_response = api_instance.get_bank_transactions(if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 bank transactions will be returned in a single API call with line items shown for each bank transaction | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type BankTransactions array with 0 to n BankTransaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transactions_history**
> HistoryRecords get_bank_transactions_history(bank_transaction_id)

Allows you to retrieve history from a bank transactions

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction

try:
    # Allows you to retrieve history from a bank transactions
    api_response = api_instance.get_bank_transactions_history(bank_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transactions_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer**
> BankTransfers get_bank_transfer(bank_transfer_id)

Allows you to retrieve any bank transfers

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfer_id = 'bank_transfer_id_example' # str | Xero generated unique identifier for a bank transfer

try:
    # Allows you to retrieve any bank transfers
    api_response = api_instance.get_bank_transfer(bank_transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of BankTransfers array with one BankTransfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer_attachment_by_file_name**
> file get_bank_transfer_attachment_by_file_name(bank_transfer_id, file_name, content_type)

Allows you to retrieve Attachments on BankTransfer by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfer_id = 'bank_transfer_id_example' # str | Xero generated unique identifier for a bank transfer
file_name = 'file_name_example' # str | The name of the file being attached to a Bank Transfer
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on BankTransfer by file name
    api_response = api_instance.get_bank_transfer_attachment_by_file_name(bank_transfer_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **file_name** | **str**| The name of the file being attached to a Bank Transfer | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of binary data from the Attachment to a Bank Transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer_attachment_by_id**
> file get_bank_transfer_attachment_by_id(bank_transfer_id, attachment_id, content_type)

Allows you to retrieve Attachments on BankTransfer

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfer_id = 'bank_transfer_id_example' # str | Xero generated unique identifier for a bank transfer
attachment_id = 'attachment_id_example' # str | Xero generated unique identifier for an Attachment to a bank transfer
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on BankTransfer
    api_response = api_instance.get_bank_transfer_attachment_by_id(bank_transfer_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **attachment_id** | [**str**](.md)| Xero generated unique identifier for an Attachment to a bank transfer | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of binary data from the Attachment to a Bank Transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer_attachments**
> Attachments get_bank_transfer_attachments(bank_transfer_id)

Allows you to retrieve Attachments from  bank transfers

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfer_id = 'bank_transfer_id_example' # str | Xero generated unique identifier for a bank transfer

try:
    # Allows you to retrieve Attachments from  bank transfers
    api_response = api_instance.get_bank_transfer_attachments(bank_transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of Attachments array of 0 to N Attachment for a Bank Transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfer_history**
> HistoryRecords get_bank_transfer_history(bank_transfer_id)

Allows you to retrieve history from a bank transfers

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfer_id = 'bank_transfer_id_example' # str | Xero generated unique identifier for a bank transfer

try:
    # Allows you to retrieve history from a bank transfers
    api_response = api_instance.get_bank_transfer_history(bank_transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfer_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of HistoryRecords array of 0 to N HistoryRecord for a Bank Transfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_transfers**
> BankTransfers get_bank_transfers(if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve all bank transfers

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve all bank transfers
    api_response = api_instance.get_bank_transfers(if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_bank_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**BankTransfers**](BankTransfers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of BankTransfers array of 0 to N BankTransfer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_payment_history**
> HistoryRecords get_batch_payment_history(batch_payment_id)

Allows you to retrieve history from a Batch Payment

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
batch_payment_id = 'batch_payment_id_example' # str | Unique identifier for BatchPayment

try:
    # Allows you to retrieve history from a Batch Payment
    api_response = api_instance.get_batch_payment_history(batch_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_batch_payment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_payment_id** | [**str**](.md)| Unique identifier for BatchPayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array of HistoryRecord objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_payments**
> BatchPayments get_batch_payments(if_modified_since=if_modified_since, where=where, order=order)

Retrieve either one or many BatchPayments for invoices

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Retrieve either one or many BatchPayments for invoices
    api_response = api_instance.get_batch_payments(if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_batch_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**BatchPayments**](BatchPayments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type BatchPayments array of BatchPayment objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_theme**
> BrandingThemes get_branding_theme(branding_theme_id)

Allows you to retrieve a specific BrandingThemes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
branding_theme_id = 'branding_theme_id_example' # str | Unique identifier for a Branding Theme

try:
    # Allows you to retrieve a specific BrandingThemes
    api_response = api_instance.get_branding_theme(branding_theme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_branding_theme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branding_theme_id** | [**str**](.md)| Unique identifier for a Branding Theme | 

### Return type

[**BrandingThemes**](BrandingThemes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type BrandingThemes with one BrandingTheme |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_theme_payment_services**
> PaymentServices get_branding_theme_payment_services(branding_theme_id)

Allows you to retrieve the Payment services for a Branding Theme

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
branding_theme_id = 'branding_theme_id_example' # str | Unique identifier for a Branding Theme

try:
    # Allows you to retrieve the Payment services for a Branding Theme
    api_response = api_instance.get_branding_theme_payment_services(branding_theme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_branding_theme_payment_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branding_theme_id** | [**str**](.md)| Unique identifier for a Branding Theme | 

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type PaymentServices array with 0 to N PaymentService |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_branding_themes**
> BrandingThemes get_branding_themes()

Allows you to retrieve all the BrandingThemes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()

try:
    # Allows you to retrieve all the BrandingThemes
    api_response = api_instance.get_branding_themes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_branding_themes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BrandingThemes**](BrandingThemes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type BrandingThemes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> Contacts get_contact(contact_id)

Allows you to retrieve, add and update contacts in a Xero organisation

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact

try:
    # Allows you to retrieve, add and update contacts in a Xero organisation
    api_response = api_instance.get_contact(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contacts array with a unique Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_attachment_by_file_name**
> file get_contact_attachment_by_file_name(contact_id, file_name, content_type)

Allows you to retrieve Attachments on Contacts by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact
file_name = 'file_name_example' # str | Name for the file you are attaching
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on Contacts by file name
    api_response = api_instance.get_contact_attachment_by_file_name(contact_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **file_name** | **str**| Name for the file you are attaching | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Contact as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_attachment_by_id**
> file get_contact_attachment_by_id(contact_id, attachment_id, content_type)

Allows you to retrieve Attachments on Contacts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact
attachment_id = 'attachment_id_example' # str | Unique identifier for a Attachment
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on Contacts
    api_response = api_instance.get_contact_attachment_by_id(contact_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Contact as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_attachments**
> Attachments get_contact_attachments(contact_id)

Allows you to retrieve, add and update contacts in a Xero organisation

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact

try:
    # Allows you to retrieve, add and update contacts in a Xero organisation
    api_response = api_instance.get_contact_attachments(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with 0 to N Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_cis_settings**
> CISSettings get_contact_cis_settings(contact_id)

Allows you to retrieve CISSettings for a contact in a Xero organisation

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact

try:
    # Allows you to retrieve CISSettings for a contact in a Xero organisation
    api_response = api_instance.get_contact_cis_settings(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_cis_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

[**CISSettings**](CISSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type CISSettings for a specific Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_group**
> ContactGroups get_contact_group(contact_group_id)

Allows you to retrieve a unique Contract Group by ID

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_group_id = 'contact_group_id_example' # str | Unique identifier for a Contact Group

try:
    # Allows you to retrieve a unique Contract Group by ID
    api_response = api_instance.get_contact_group(contact_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contact Groups array with a specific Contact Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_groups**
> ContactGroups get_contact_groups(where=where, order=order)

Allows you to retrieve the ContactID and Name of all the contacts in a contact group

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve the ContactID and Name of all the contacts in a contact group
    api_response = api_instance.get_contact_groups(where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contact Groups array of Contact Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_history**
> HistoryRecords get_contact_history(contact_id)

Allows you to retrieve a history records of an Contact

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact

try:
    # Allows you to retrieve a history records of an Contact
    api_response = api_instance.get_contact_history(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contact_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type History Records array of 0 to N History Record for a specific Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> Contacts get_contacts(if_modified_since=if_modified_since, where=where, order=order, i_ds=i_ds, page=page, include_archived=include_archived)

Allows you to retrieve, add and update contacts in a Xero organisation

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
i_ds = 'i_ds_example' # str | Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call. (optional)
page = 56 # int | e.g. page=1 - Up to 100 contacts will be returned in a single API call. (optional)
include_archived = True # bool | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response (optional)

try:
    # Allows you to retrieve, add and update contacts in a Xero organisation
    api_response = api_instance.get_contacts(if_modified_since=if_modified_since, where=where, order=order, i_ds=i_ds, page=page, include_archived=include_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **i_ds** | **str**| Filter by a comma separated list of ContactIDs. Allows you to retrieve a specific set of contacts in a single call. | [optional] 
 **page** | **int**| e.g. page&#x3D;1 - Up to 100 contacts will be returned in a single API call. | [optional] 
 **include_archived** | **bool**| e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response | [optional] 

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contacts array with 0 to N Contact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note**
> CreditNotes get_credit_note(credit_note_id)

Allows you to retrieve a specific credit note

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note

try:
    # Allows you to retrieve a specific credit note
    api_response = api_instance.get_credit_note(credit_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Credit Notes array with a unique CreditNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_as_pdf**
> file get_credit_note_as_pdf(credit_note_id, content_type)

Allows you to retrieve Credit Note as PDF files

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Credit Note as PDF files
    api_response = api_instance.get_credit_note_as_pdf(credit_note_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of binary data from the Attachment to a Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_attachment_by_file_name**
> file get_credit_note_attachment_by_file_name(credit_note_id, file_name, content_type)

Allows you to retrieve Attachments on CreditNote by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note
file_name = 'file_name_example' # str | Name of the file you are attaching to Credit Note
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on CreditNote by file name
    api_response = api_instance.get_credit_note_attachment_by_file_name(credit_note_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **file_name** | **str**| Name of the file you are attaching to Credit Note | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Credit Note as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_attachment_by_id**
> file get_credit_note_attachment_by_id(credit_note_id, attachment_id, content_type)

Allows you to retrieve Attachments on CreditNote

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note
attachment_id = 'attachment_id_example' # str | Unique identifier for a Attachment
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on CreditNote
    api_response = api_instance.get_credit_note_attachment_by_id(credit_note_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Credit Note as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_attachments**
> Attachments get_credit_note_attachments(credit_note_id)

Allows you to retrieve Attachments for credit notes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note

try:
    # Allows you to retrieve Attachments for credit notes
    api_response = api_instance.get_credit_note_attachments(credit_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with all Attachment for specific Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_note_history**
> HistoryRecords get_credit_note_history(credit_note_id)

Allows you to retrieve a history records of an CreditNote

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note

try:
    # Allows you to retrieve a history records of an CreditNote
    api_response = api_instance.get_credit_note_history(credit_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_note_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with all HistoryRecord for specific Credit Note |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit_notes**
> CreditNotes get_credit_notes(if_modified_since=if_modified_since, where=where, order=order, page=page)

Allows you to retrieve any credit notes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note (optional)

try:
    # Allows you to retrieve any credit notes
    api_response = api_instance.get_credit_notes(if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_credit_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 credit notes will be returned in a single API call with line items shown for each credit note | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Credit Notes array of CreditNote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currencies**
> Currencies get_currencies(where=where, order=order)

Allows you to retrieve currencies for your organisation

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve currencies for your organisation
    api_response = api_instance.get_currencies(where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Currencies**](Currencies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Currencies array with all Currencies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee**
> Employees get_employee(employee_id)

Allows you to retrieve a specific employee used in Xero payrun

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
employee_id = 'employee_id_example' # str | Unique identifier for a Employee

try:
    # Allows you to retrieve a specific employee used in Xero payrun
    api_response = api_instance.get_employee(employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)| Unique identifier for a Employee | 

### Return type

[**Employees**](Employees.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Employees array with specified Employee |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees**
> Employees get_employees(if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve employees used in Xero payrun

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve employees used in Xero payrun
    api_response = api_instance.get_employees(if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Employees**](Employees.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Employees array with all Employee |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_claim**
> ExpenseClaims get_expense_claim(expense_claim_id)

Allows you to retrieve a specified expense claim

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
expense_claim_id = 'expense_claim_id_example' # str | Unique identifier for a ExpenseClaim

try:
    # Allows you to retrieve a specified expense claim
    api_response = api_instance.get_expense_claim(expense_claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_expense_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_claim_id** | [**str**](.md)| Unique identifier for a ExpenseClaim | 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ExpenseClaims array with specified ExpenseClaim |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_claim_history**
> HistoryRecords get_expense_claim_history(expense_claim_id)

Allows you to retrieve a history records of an ExpenseClaim

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
expense_claim_id = 'expense_claim_id_example' # str | Unique identifier for a ExpenseClaim

try:
    # Allows you to retrieve a history records of an ExpenseClaim
    api_response = api_instance.get_expense_claim_history(expense_claim_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_expense_claim_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_claim_id** | [**str**](.md)| Unique identifier for a ExpenseClaim | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with all HistoryRecord for specific ExpenseClaim |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense_claims**
> ExpenseClaims get_expense_claims(if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve expense claims

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve expense claims
    api_response = api_instance.get_expense_claims(if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_expense_claims: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ExpenseClaims array with all ExpenseClaims |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice**
> Invoices get_invoice(invoice_id)

Allows you to retrieve a specified sales invoice or purchase bill

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice

try:
    # Allows you to retrieve a specified sales invoice or purchase bill
    api_response = api_instance.get_invoice(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 

### Return type

[**Invoices**](Invoices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Invoices array with specified Invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_as_pdf**
> file get_invoice_as_pdf(invoice_id, content_type)

Allows you to retrieve invoices or purchase bills as PDF files

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve invoices or purchase bills as PDF files
    api_response = api_instance.get_invoice_as_pdf(invoice_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_as_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of byte array pdf version of specified Invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_attachment_by_file_name**
> file get_invoice_attachment_by_file_name(invoice_id, file_name, content_type)

Allows you to retrieve Attachment on invoices or purchase bills by it's filename

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice
file_name = 'file_name_example' # str | Name of the file you are attaching
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachment on invoices or purchase bills by it's filename
    api_response = api_instance.get_invoice_attachment_by_file_name(invoice_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **file_name** | **str**| Name of the file you are attaching | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Invoice as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_attachment_by_id**
> file get_invoice_attachment_by_id(invoice_id, attachment_id, content_type)

Allows you to retrieve a specified Attachment on invoices or purchase bills by it's ID

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice
attachment_id = 'attachment_id_example' # str | Unique identifier for an Attachment
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve a specified Attachment on invoices or purchase bills by it's ID
    api_response = api_instance.get_invoice_attachment_by_id(invoice_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **attachment_id** | [**str**](.md)| Unique identifier for an Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Invoice as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_attachments**
> Attachments get_invoice_attachments(invoice_id)

Allows you to retrieve Attachments on invoices or purchase bills

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice

try:
    # Allows you to retrieve Attachments on invoices or purchase bills
    api_response = api_instance.get_invoice_attachments(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array of Attachments for specified Invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_history**
> HistoryRecords get_invoice_history(invoice_id)

Allows you to retrieve a history records of an invoice

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice

try:
    # Allows you to retrieve a history records of an invoice
    api_response = api_instance.get_invoice_history(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with all HistoryRecord for specific Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_reminders**
> InvoiceReminders get_invoice_reminders()

Allows you to retrieve invoice reminder settings

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()

try:
    # Allows you to retrieve invoice reminder settings
    api_response = api_instance.get_invoice_reminders()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoice_reminders: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InvoiceReminders**](InvoiceReminders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of Invoice Reminders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> Invoices get_invoices(if_modified_since=if_modified_since, where=where, order=order, i_ds=i_ds, invoice_numbers=invoice_numbers, contact_i_ds=contact_i_ds, statuses=statuses, page=page, include_archived=include_archived, created_by_my_app=created_by_my_app, unitdp=unitdp)

Allows you to retrieve any sales invoices or purchase bills

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
i_ds = 'i_ds_example' # str | Filter by a comma-separated list of InvoicesIDs. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. (optional)
invoice_numbers = 'invoice_numbers_example' # str | Filter by a comma-separated list of InvoiceNumbers. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. (optional)
contact_i_ds = 'contact_i_ds_example' # str | Filter by a comma-separated list of ContactIDs. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. (optional)
statuses = 'statuses_example' # str | Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. (optional)
page = 56 # int | e.g. page=1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice (optional)
include_archived = True # bool | e.g. includeArchived=true - Contacts with a status of ARCHIVED will be included in the response (optional)
created_by_my_app = True # bool | When set to true you'll only retrieve Invoices created by your app (optional)
unitdp = 56 # int | e.g. unitdp=4 – You can opt in to use four decimal places for unit amounts (optional)

try:
    # Allows you to retrieve any sales invoices or purchase bills
    api_response = api_instance.get_invoices(if_modified_since=if_modified_since, where=where, order=order, i_ds=i_ds, invoice_numbers=invoice_numbers, contact_i_ds=contact_i_ds, statuses=statuses, page=page, include_archived=include_archived, created_by_my_app=created_by_my_app, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **i_ds** | **str**| Filter by a comma-separated list of InvoicesIDs. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. | [optional] 
 **invoice_numbers** | **str**| Filter by a comma-separated list of InvoiceNumbers. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. | [optional] 
 **contact_i_ds** | **str**| Filter by a comma-separated list of ContactIDs. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. | [optional] 
 **statuses** | **str**| Filter by a comma-separated list Statuses. For faster response times we recommend using these explicit parameters instead of passing OR conditions into the Where filter. | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 invoices will be returned in a single API call with line items shown for each invoice | [optional] 
 **include_archived** | **bool**| e.g. includeArchived&#x3D;true - Contacts with a status of ARCHIVED will be included in the response | [optional] 
 **created_by_my_app** | **bool**| When set to true you&#39;ll only retrieve Invoices created by your app | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Invoices**](Invoices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Invoices array with all Invoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> Items get_item(item_id)

Allows you to retrieve a specified item

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
item_id = 'item_id_example' # str | Unique identifier for an Item

try:
    # Allows you to retrieve a specified item
    api_response = api_instance.get_item(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**str**](.md)| Unique identifier for an Item | 

### Return type

[**Items**](Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Items array with specified Item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_history**
> HistoryRecords get_item_history(item_id)

Allows you to retrieve history for items

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
item_id = 'item_id_example' # str | Unique identifier for an Item

try:
    # Allows you to retrieve history for items
    api_response = api_instance.get_item_history(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_item_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**str**](.md)| Unique identifier for an Item | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with all HistoryRecord for specific Item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items**
> Items get_items(if_modified_since=if_modified_since, where=where, order=order, unitdp=unitdp)

Allows you to retrieve any items

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
unitdp = 56 # int | e.g. unitdp=4 – You can opt in to use four decimal places for unit amounts (optional)

try:
    # Allows you to retrieve any items
    api_response = api_instance.get_items(if_modified_since=if_modified_since, where=where, order=order, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Items**](Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Items array with all Item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal**
> Journals get_journal(journal_id)

Allows you to retrieve a specified journals.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
journal_id = 'journal_id_example' # str | Unique identifier for a Journal

try:
    # Allows you to retrieve a specified journals.
    api_response = api_instance.get_journal(journal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_id** | [**str**](.md)| Unique identifier for a Journal | 

### Return type

[**Journals**](Journals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Journals array with specified Journal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journals**
> Journals get_journals(if_modified_since=if_modified_since, offset=offset, payments_only=payments_only)

Allows you to retrieve any journals.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
offset = 56 # int | Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned (optional)
payments_only = True # bool | Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default. (optional)

try:
    # Allows you to retrieve any journals.
    api_response = api_instance.get_journals(if_modified_since=if_modified_since, offset=offset, payments_only=payments_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **offset** | **int**| Offset by a specified journal number. e.g. journals with a JournalNumber greater than the offset will be returned | [optional] 
 **payments_only** | **bool**| Filter to retrieve journals on a cash basis. Journals are returned on an accrual basis by default. | [optional] 

### Return type

[**Journals**](Journals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Journals array with all Journals |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_transaction**
> LinkedTransactions get_linked_transaction(linked_transaction_id)

Allows you to retrieve a specified linked transactions (billable expenses)

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
linked_transaction_id = 'linked_transaction_id_example' # str | Unique identifier for a LinkedTransaction

try:
    # Allows you to retrieve a specified linked transactions (billable expenses)
    api_response = api_instance.get_linked_transaction(linked_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_linked_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_transaction_id** | [**str**](.md)| Unique identifier for a LinkedTransaction | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type LinkedTransactions array with a specified LinkedTransaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_transactions**
> LinkedTransactions get_linked_transactions(page=page, linked_transaction_id=linked_transaction_id, source_transaction_id=source_transaction_id, contact_id=contact_id, status=status, target_transaction_id=target_transaction_id)

Retrieve linked transactions (billable expenses)

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
page = 56 # int | Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page=1. (optional)
linked_transaction_id = 'linked_transaction_id_example' # str | The Xero identifier for an Linked Transaction (optional)
source_transaction_id = 'source_transaction_id_example' # str | Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice (optional)
contact_id = 'contact_id_example' # str | Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer. (optional)
status = 'status_example' # str | Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID=4bb34b03-3378-4bb2-a0ed-6345abf3224e&Status=APPROVED. (optional)
target_transaction_id = 'target_transaction_id_example' # str | Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice (optional)

try:
    # Retrieve linked transactions (billable expenses)
    api_response = api_instance.get_linked_transactions(page=page, linked_transaction_id=linked_transaction_id, source_transaction_id=source_transaction_id, contact_id=contact_id, status=status, target_transaction_id=target_transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_linked_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Up to 100 linked transactions will be returned in a single API call. Use the page parameter to specify the page to be returned e.g. page&#x3D;1. | [optional] 
 **linked_transaction_id** | **str**| The Xero identifier for an Linked Transaction | [optional] 
 **source_transaction_id** | **str**| Filter by the SourceTransactionID. Get all the linked transactions created from a particular ACCPAY invoice | [optional] 
 **contact_id** | **str**| Filter by the ContactID. Get all the linked transactions that have been assigned to a particular customer. | [optional] 
 **status** | **str**| Filter by the combination of ContactID and Status. Get all the linked transactions that have been assigned to a particular customer and have a particular status e.g. GET /LinkedTransactions?ContactID&#x3D;4bb34b03-3378-4bb2-a0ed-6345abf3224e&amp;Status&#x3D;APPROVED. | [optional] 
 **target_transaction_id** | **str**| Filter by the TargetTransactionID. Get all the linked transactions allocated to a particular ACCREC invoice | [optional] 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type LinkedTransactions array with all LinkedTransaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journal**
> ManualJournals get_manual_journal(manual_journal_id)

Allows you to retrieve a specified manual journals

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
manual_journal_id = 'manual_journal_id_example' # str | Unique identifier for a ManualJournal

try:
    # Allows you to retrieve a specified manual journals
    api_response = api_instance.get_manual_journal(manual_journal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ManualJournals array with a specified ManualJournals |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journal_attachment_by_file_name**
> file get_manual_journal_attachment_by_file_name(manual_journal_id, file_name, content_type)

Allows you to retrieve specified Attachment on ManualJournal by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
manual_journal_id = 'manual_journal_id_example' # str | Unique identifier for a ManualJournal
file_name = 'file_name_example' # str | The name of the file being attached to a ManualJournal
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve specified Attachment on ManualJournal by file name
    api_response = api_instance.get_manual_journal_attachment_by_file_name(manual_journal_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journal_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **file_name** | **str**| The name of the file being attached to a ManualJournal | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Manual Journal as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journal_attachment_by_id**
> file get_manual_journal_attachment_by_id(manual_journal_id, attachment_id, content_type)

Allows you to retrieve specified Attachment on ManualJournals

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
manual_journal_id = 'manual_journal_id_example' # str | Unique identifier for a ManualJournal
attachment_id = 'attachment_id_example' # str | Unique identifier for a Attachment
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve specified Attachment on ManualJournals
    api_response = api_instance.get_manual_journal_attachment_by_id(manual_journal_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journal_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Manual Journal as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journal_attachments**
> Attachments get_manual_journal_attachments(manual_journal_id)

Allows you to retrieve Attachment for manual journals

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
manual_journal_id = 'manual_journal_id_example' # str | Unique identifier for a ManualJournal

try:
    # Allows you to retrieve Attachment for manual journals
    api_response = api_instance.get_manual_journal_attachments(manual_journal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journal_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with all Attachments for a ManualJournals |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manual_journals**
> ManualJournals get_manual_journals(if_modified_since=if_modified_since, where=where, order=order, page=page)

Allows you to retrieve any manual journals

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment (optional)

try:
    # Allows you to retrieve any manual journals
    api_response = api_instance.get_manual_journals(if_modified_since=if_modified_since, where=where, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_manual_journals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 manual journals will be returned in a single API call with line items shown for each overpayment | [optional] 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ManualJournals array with a all ManualJournals |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_online_invoice**
> OnlineInvoices get_online_invoice(invoice_id)

Allows you to retrieve a URL to an online invoice

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice

try:
    # Allows you to retrieve a URL to an online invoice
    api_response = api_instance.get_online_invoice(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_online_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 

### Return type

[**OnlineInvoices**](OnlineInvoices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type OnlineInvoice array with one OnlineInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organisation_cis_settings**
> CISOrgSetting get_organisation_cis_settings(organisation_id)

Allows you To verify if an organisation is using contruction industry scheme, you can retrieve the CIS settings for the organistaion.

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
organisation_id = 'organisation_id_example' # str | 

try:
    # Allows you To verify if an organisation is using contruction industry scheme, you can retrieve the CIS settings for the organistaion.
    api_response = api_instance.get_organisation_cis_settings(organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_organisation_cis_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | [**str**](.md)|  | 

### Return type

[**CISOrgSetting**](CISOrgSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Organisation array with specified Organisation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organisations**
> Organisations get_organisations()

Allows you to retrieve Organisation details

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()

try:
    # Allows you to retrieve Organisation details
    api_response = api_instance.get_organisations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_organisations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Organisations**](Organisations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Organisation array with all Organisation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overpayment**
> Overpayments get_overpayment(overpayment_id)

Allows you to retrieve a specified overpayments

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
overpayment_id = 'overpayment_id_example' # str | Unique identifier for a Overpayment

try:
    # Allows you to retrieve a specified overpayments
    api_response = api_instance.get_overpayment(overpayment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_overpayment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overpayment_id** | [**str**](.md)| Unique identifier for a Overpayment | 

### Return type

[**Overpayments**](Overpayments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Overpayments array with specified Overpayments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overpayment_history**
> HistoryRecords get_overpayment_history(overpayment_id)

Allows you to retrieve a history records of an Overpayment

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
overpayment_id = 'overpayment_id_example' # str | Unique identifier for a Overpayment

try:
    # Allows you to retrieve a history records of an Overpayment
    api_response = api_instance.get_overpayment_history(overpayment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_overpayment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overpayment_id** | [**str**](.md)| Unique identifier for a Overpayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with all HistoryRecord for Overpayments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overpayments**
> Overpayments get_overpayments(if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)

Allows you to retrieve overpayments

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment (optional)
unitdp = 56 # int | e.g. unitdp=4 – You can opt in to use four decimal places for unit amounts (optional)

try:
    # Allows you to retrieve overpayments
    api_response = api_instance.get_overpayments(if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_overpayments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 overpayments will be returned in a single API call with line items shown for each overpayment | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Overpayments**](Overpayments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Overpayments array with all Overpayments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment**
> Payments get_payment(payment_id)

Allows you to retrieve a specified payment for invoices and credit notes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
payment_id = 'payment_id_example' # str | Unique identifier for a Payment

try:
    # Allows you to retrieve a specified payment for invoices and credit notes
    api_response = api_instance.get_payment(payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)| Unique identifier for a Payment | 

### Return type

[**Payments**](Payments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Payments array for specified Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_history**
> HistoryRecords get_payment_history(payment_id)

Allows you to retrieve history records of a payment

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
payment_id = 'payment_id_example' # str | Unique identifier for a Payment

try:
    # Allows you to retrieve history records of a payment
    api_response = api_instance.get_payment_history(payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_payment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)| Unique identifier for a Payment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with all HistoryRecord for Payments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_services**
> PaymentServices get_payment_services()

Allows you to retrieve payment services

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()

try:
    # Allows you to retrieve payment services
    api_response = api_instance.get_payment_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_payment_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PaymentServices**](PaymentServices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type PaymentServices array for all PaymentService |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments**
> Payments get_payments(if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve payments for invoices and credit notes

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve payments for invoices and credit notes
    api_response = api_instance.get_payments(if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Payments**](Payments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Payments array for all Payments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prepayment**
> Prepayments get_prepayment(prepayment_id)

Allows you to retrieve a specified prepayments

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
prepayment_id = 'prepayment_id_example' # str | Unique identifier for a PrePayment

try:
    # Allows you to retrieve a specified prepayments
    api_response = api_instance.get_prepayment(prepayment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_prepayment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepayment_id** | [**str**](.md)| Unique identifier for a PrePayment | 

### Return type

[**Prepayments**](Prepayments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Prepayments array for a specified Prepayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prepayment_history**
> HistoryRecords get_prepayment_history(prepayment_id)

Allows you to retrieve a history records of an Prepayment

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
prepayment_id = 'prepayment_id_example' # str | Unique identifier for a PrePayment

try:
    # Allows you to retrieve a history records of an Prepayment
    api_response = api_instance.get_prepayment_history(prepayment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_prepayment_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prepayment_id** | [**str**](.md)| Unique identifier for a PrePayment | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array with all HistoryRecord for PrePayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prepayments**
> Prepayments get_prepayments(if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)

Allows you to retrieve prepayments

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
page = 56 # int | e.g. page=1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment (optional)
unitdp = 56 # int | e.g. unitdp=4 – You can opt in to use four decimal places for unit amounts (optional)

try:
    # Allows you to retrieve prepayments
    api_response = api_instance.get_prepayments(if_modified_since=if_modified_since, where=where, order=order, page=page, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_prepayments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| e.g. page&#x3D;1 – Up to 100 prepayments will be returned in a single API call with line items shown for each overpayment | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Prepayments**](Prepayments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Prepayments array for all Prepayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_order**
> PurchaseOrders get_purchase_order(purchase_order_id)

Allows you to retrieve a specified purchase orders

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
purchase_order_id = 'purchase_order_id_example' # str | Unique identifier for a PurchaseOrder

try:
    # Allows you to retrieve a specified purchase orders
    api_response = api_instance.get_purchase_order(purchase_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_id** | [**str**](.md)| Unique identifier for a PurchaseOrder | 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type PurchaseOrder array for specified PurchaseOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_order_history**
> HistoryRecords get_purchase_order_history(purchase_order_id)

Allows you to retrieve history for PurchaseOrder

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
purchase_order_id = 'purchase_order_id_example' # str | Unique identifier for a PurchaseOrder

try:
    # Allows you to retrieve history for PurchaseOrder
    api_response = api_instance.get_purchase_order_history(purchase_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_purchase_order_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_id** | [**str**](.md)| Unique identifier for a PurchaseOrder | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array for all HistoryRecord for PurchaseOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_orders**
> PurchaseOrders get_purchase_orders(if_modified_since=if_modified_since, status=status, date_from=date_from, date_to=date_to, order=order, page=page)

Allows you to retrieve purchase orders

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
status = 'status_example' # str | Filter by purchase order status (optional)
date_from = 'date_from_example' # str | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31 (optional)
date_to = 'date_to_example' # str | Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom=2015-12-01&DateTo=2015-12-31 (optional)
order = 'order_example' # str | Order by an any element (optional)
page = 56 # int | To specify a page, append the page parameter to the URL e.g. ?page=1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page=2 and continuing this process until no more results are returned. (optional)

try:
    # Allows you to retrieve purchase orders
    api_response = api_instance.get_purchase_orders(if_modified_since=if_modified_since, status=status, date_from=date_from, date_to=date_to, order=order, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_purchase_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **status** | **str**| Filter by purchase order status | [optional] 
 **date_from** | **str**| Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31 | [optional] 
 **date_to** | **str**| Filter by purchase order date (e.g. GET https://.../PurchaseOrders?DateFrom&#x3D;2015-12-01&amp;DateTo&#x3D;2015-12-31 | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **page** | **int**| To specify a page, append the page parameter to the URL e.g. ?page&#x3D;1. If there are 100 records in the response you will need to check if there is any more data by fetching the next page e.g ?page&#x3D;2 and continuing this process until no more results are returned. | [optional] 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type PurchaseOrder array of all PurchaseOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt**
> Receipts get_receipt(receipt_id)

Allows you to retrieve a specified draft expense claim receipts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt

try:
    # Allows you to retrieve a specified draft expense claim receipts
    api_response = api_instance.get_receipt(receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 

### Return type

[**Receipts**](Receipts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Receipts array for a specified Receipt |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_attachment_by_file_name**
> file get_receipt_attachment_by_file_name(receipt_id, file_name, content_type)

Allows you to retrieve Attachments on expense claim receipts by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt
file_name = 'file_name_example' # str | The name of the file being attached to the Receipt
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on expense claim receipts by file name
    api_response = api_instance.get_receipt_attachment_by_file_name(receipt_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **file_name** | **str**| The name of the file being attached to the Receipt | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Receipt as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_attachment_by_id**
> file get_receipt_attachment_by_id(receipt_id, attachment_id, content_type)

Allows you to retrieve Attachments on expense claim receipts by ID

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt
attachment_id = 'attachment_id_example' # str | Unique identifier for a Attachment
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve Attachments on expense claim receipts by ID
    api_response = api_instance.get_receipt_attachment_by_id(receipt_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Receipt as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_attachments**
> Attachments get_receipt_attachments(receipt_id)

Allows you to retrieve Attachments for expense claim receipts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt

try:
    # Allows you to retrieve Attachments for expense claim receipts
    api_response = api_instance.get_receipt_attachments(receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array of Attachments for a specified Receipt |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipt_history**
> HistoryRecords get_receipt_history(receipt_id)

Allows you to retrieve a history records of an Receipt

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt

try:
    # Allows you to retrieve a history records of an Receipt
    api_response = api_instance.get_receipt_history(receipt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipt_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array of all HistoryRecord for Receipt |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_receipts**
> Receipts get_receipts(if_modified_since=if_modified_since, where=where, order=order, unitdp=unitdp)

Allows you to retrieve draft expense claim receipts for any user

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
unitdp = 56 # int | e.g. unitdp=4 – You can opt in to use four decimal places for unit amounts (optional)

try:
    # Allows you to retrieve draft expense claim receipts for any user
    api_response = api_instance.get_receipts(if_modified_since=if_modified_since, where=where, order=order, unitdp=unitdp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_receipts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **unitdp** | **int**| e.g. unitdp&#x3D;4 – You can opt in to use four decimal places for unit amounts | [optional] 

### Return type

[**Receipts**](Receipts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Receipts array for all Receipt |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice**
> RepeatingInvoices get_repeating_invoice(repeating_invoice_id)

Allows you to retrieve a specified repeating invoice

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
repeating_invoice_id = 'repeating_invoice_id_example' # str | Unique identifier for a Repeating Invoice

try:
    # Allows you to retrieve a specified repeating invoice
    api_response = api_instance.get_repeating_invoice(repeating_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 

### Return type

[**RepeatingInvoices**](RepeatingInvoices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Repeating Invoices array with a specified Repeating Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice_attachment_by_file_name**
> file get_repeating_invoice_attachment_by_file_name(repeating_invoice_id, file_name, content_type)

Allows you to retrieve specified attachment on repeating invoices by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
repeating_invoice_id = 'repeating_invoice_id_example' # str | Unique identifier for a Repeating Invoice
file_name = 'file_name_example' # str | The name of the file being attached to a Repeating Invoice
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve specified attachment on repeating invoices by file name
    api_response = api_instance.get_repeating_invoice_attachment_by_file_name(repeating_invoice_id, file_name, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **file_name** | **str**| The name of the file being attached to a Repeating Invoice | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Repeating Invoice as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice_attachment_by_id**
> file get_repeating_invoice_attachment_by_id(repeating_invoice_id, attachment_id, content_type)

Allows you to retrieve a specified Attachments on repeating invoices

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
repeating_invoice_id = 'repeating_invoice_id_example' # str | Unique identifier for a Repeating Invoice
attachment_id = 'attachment_id_example' # str | Unique identifier for a Attachment
content_type = 'content_type_example' # str | The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf

try:
    # Allows you to retrieve a specified Attachments on repeating invoices
    api_response = api_instance.get_repeating_invoice_attachment_by_id(repeating_invoice_id, attachment_id, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **attachment_id** | [**str**](.md)| Unique identifier for a Attachment | 
 **content_type** | **str**| The mime type of the attachment file you are retrieving i.e image/jpg, application/pdf | 

### Return type

**file**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of attachment for Repeating Invoice as binary data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice_attachments**
> Attachments get_repeating_invoice_attachments(repeating_invoice_id)

Allows you to retrieve Attachments on repeating invoice

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
repeating_invoice_id = 'repeating_invoice_id_example' # str | Unique identifier for a Repeating Invoice

try:
    # Allows you to retrieve Attachments on repeating invoice
    api_response = api_instance.get_repeating_invoice_attachments(repeating_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with all Attachments for a specified Repeating Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoice_history**
> HistoryRecords get_repeating_invoice_history(repeating_invoice_id)

Allows you to retrieve history for a repeating invoice

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
repeating_invoice_id = 'repeating_invoice_id_example' # str | Unique identifier for a Repeating Invoice

try:
    # Allows you to retrieve history for a repeating invoice
    api_response = api_instance.get_repeating_invoice_history(repeating_invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoice_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 

### Return type

[**HistoryRecords**](HistoryRecords.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type HistoryRecords array of all HistoryRecord for Repeating Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repeating_invoices**
> RepeatingInvoices get_repeating_invoices(where=where, order=order)

Allows you to retrieve any repeating invoices

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve any repeating invoices
    api_response = api_instance.get_repeating_invoices(where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_repeating_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**RepeatingInvoices**](RepeatingInvoices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Repeating Invoices array for all Repeating Invoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_aged_payables_by_contact**
> ReportWithRows get_report_aged_payables_by_contact(contact_id, date=date, from_date=from_date, to_date=to_date)

Allows you to retrieve report for AgedPayablesByContact

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact
date = '2013-10-20' # date | The date of the Aged Payables By Contact report (optional)
from_date = '2013-10-20' # date | The from date of the Aged Payables By Contact report (optional)
to_date = '2013-10-20' # date | The to date of the Aged Payables By Contact report (optional)

try:
    # Allows you to retrieve report for AgedPayablesByContact
    api_response = api_instance.get_report_aged_payables_by_contact(contact_id, date=date, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_aged_payables_by_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **date** | **date**| The date of the Aged Payables By Contact report | [optional] 
 **from_date** | **date**| The from date of the Aged Payables By Contact report | [optional] 
 **to_date** | **date**| The to date of the Aged Payables By Contact report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_aged_receivables_by_contact**
> ReportWithRows get_report_aged_receivables_by_contact(contact_id, date=date, from_date=from_date, to_date=to_date)

Allows you to retrieve report for AgedReceivablesByContact

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact
date = '2013-10-20' # date | The date of the Aged Receivables By Contact report (optional)
from_date = '2013-10-20' # date | The from date of the Aged Receivables By Contact report (optional)
to_date = '2013-10-20' # date | The to date of the Aged Receivables By Contact report (optional)

try:
    # Allows you to retrieve report for AgedReceivablesByContact
    api_response = api_instance.get_report_aged_receivables_by_contact(contact_id, date=date, from_date=from_date, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_aged_receivables_by_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **date** | **date**| The date of the Aged Receivables By Contact report | [optional] 
 **from_date** | **date**| The from date of the Aged Receivables By Contact report | [optional] 
 **to_date** | **date**| The to date of the Aged Receivables By Contact report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_ba_sor_gst**
> ReportWithRows get_report_ba_sor_gst(report_id)

Allows you to retrieve report for BAS only valid for AU orgs

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
report_id = 'report_id_example' # str | Unique identifier for a Report

try:
    # Allows you to retrieve report for BAS only valid for AU orgs
    api_response = api_instance.get_report_ba_sor_gst(report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_ba_sor_gst: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Unique identifier for a Report | 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_ba_sor_gst_list**
> ReportWithRows get_report_ba_sor_gst_list()

Allows you to retrieve report for BAS only valid for AU orgs

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()

try:
    # Allows you to retrieve report for BAS only valid for AU orgs
    api_response = api_instance.get_report_ba_sor_gst_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_ba_sor_gst_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_balance_sheet**
> ReportWithRows get_report_balance_sheet(date=date, periods=periods, timeframe=timeframe, tracking_option_id1=tracking_option_id1, tracking_option_id2=tracking_option_id2, standard_layout=standard_layout, payments_only=payments_only)

Allows you to retrieve report for BalanceSheet

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
date = 'date_example' # str | The date of the Balance Sheet report (optional)
periods = 56 # int | The number of periods for the Balance Sheet report (optional)
timeframe = 'timeframe_example' # str | The period size to compare to (MONTH, QUARTER, YEAR) (optional)
tracking_option_id1 = 'tracking_option_id1_example' # str | The tracking option 1 for the Balance Sheet report (optional)
tracking_option_id2 = 'tracking_option_id2_example' # str | The tracking option 2 for the Balance Sheet report (optional)
standard_layout = True # bool | The standard layout boolean for the Balance Sheet report (optional)
payments_only = True # bool | return a cash basis for the Balance Sheet report (optional)

try:
    # Allows you to retrieve report for BalanceSheet
    api_response = api_instance.get_report_balance_sheet(date=date, periods=periods, timeframe=timeframe, tracking_option_id1=tracking_option_id1, tracking_option_id2=tracking_option_id2, standard_layout=standard_layout, payments_only=payments_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_balance_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **str**| The date of the Balance Sheet report | [optional] 
 **periods** | **int**| The number of periods for the Balance Sheet report | [optional] 
 **timeframe** | **str**| The period size to compare to (MONTH, QUARTER, YEAR) | [optional] 
 **tracking_option_id1** | **str**| The tracking option 1 for the Balance Sheet report | [optional] 
 **tracking_option_id2** | **str**| The tracking option 2 for the Balance Sheet report | [optional] 
 **standard_layout** | **bool**| The standard layout boolean for the Balance Sheet report | [optional] 
 **payments_only** | **bool**| return a cash basis for the Balance Sheet report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_bank_summary**
> ReportWithRows get_report_bank_summary(date=date, period=period, timeframe=timeframe)

Allows you to retrieve report for BankSummary

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
date = '2013-10-20' # date | The date for the Bank Summary report e.g. 2018-03-31 (optional)
period = 56 # int | The number of periods to compare (integer between 1 and 12) (optional)
timeframe = 56 # int | The period size to compare to (1=month, 3=quarter, 12=year) (optional)

try:
    # Allows you to retrieve report for BankSummary
    api_response = api_instance.get_report_bank_summary(date=date, period=period, timeframe=timeframe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_bank_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **date**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] 
 **period** | **int**| The number of periods to compare (integer between 1 and 12) | [optional] 
 **timeframe** | **int**| The period size to compare to (1&#x3D;month, 3&#x3D;quarter, 12&#x3D;year) | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_budget_summary**
> ReportWithRows get_report_budget_summary(date=date, period=period, timeframe=timeframe)

Allows you to retrieve report for Budget Summary

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
date = '2013-10-20' # date | The date for the Bank Summary report e.g. 2018-03-31 (optional)
period = 56 # int | The number of periods to compare (integer between 1 and 12) (optional)
timeframe = 56 # int | The period size to compare to (1=month, 3=quarter, 12=year) (optional)

try:
    # Allows you to retrieve report for Budget Summary
    api_response = api_instance.get_report_budget_summary(date=date, period=period, timeframe=timeframe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_budget_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **date**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] 
 **period** | **int**| The number of periods to compare (integer between 1 and 12) | [optional] 
 **timeframe** | **int**| The period size to compare to (1&#x3D;month, 3&#x3D;quarter, 12&#x3D;year) | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success- return a Report with Rows object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_executive_summary**
> ReportWithRows get_report_executive_summary(date=date)

Allows you to retrieve report for ExecutiveSummary

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
date = '2013-10-20' # date | The date for the Bank Summary report e.g. 2018-03-31 (optional)

try:
    # Allows you to retrieve report for ExecutiveSummary
    api_response = api_instance.get_report_executive_summary(date=date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_executive_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **date**| The date for the Bank Summary report e.g. 2018-03-31 | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_profit_and_loss**
> ReportWithRows get_report_profit_and_loss(from_date=from_date, to_date=to_date, periods=periods, timeframe=timeframe, tracking_category_id=tracking_category_id, tracking_category_id2=tracking_category_id2, tracking_option_id=tracking_option_id, tracking_option_id2=tracking_option_id2, standard_layout=standard_layout, payments_only=payments_only)

Allows you to retrieve report for ProfitAndLoss

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
from_date = '2013-10-20' # date | The from date for the ProfitAndLoss report e.g. 2018-03-31 (optional)
to_date = '2013-10-20' # date | The to date for the ProfitAndLoss report e.g. 2018-03-31 (optional)
periods = 56 # int | The number of periods to compare (integer between 1 and 12) (optional)
timeframe = 'timeframe_example' # str | The period size to compare to (MONTH, QUARTER, YEAR) (optional)
tracking_category_id = 'tracking_category_id_example' # str | The trackingCategory 1 for the ProfitAndLoss report (optional)
tracking_category_id2 = 'tracking_category_id2_example' # str | The trackingCategory 2 for the ProfitAndLoss report (optional)
tracking_option_id = 'tracking_option_id_example' # str | The tracking option 1 for the ProfitAndLoss report (optional)
tracking_option_id2 = 'tracking_option_id2_example' # str | The tracking option 2 for the ProfitAndLoss report (optional)
standard_layout = True # bool | Return the standard layout for the ProfitAndLoss report (optional)
payments_only = True # bool | Return cash only basis for the ProfitAndLoss report (optional)

try:
    # Allows you to retrieve report for ProfitAndLoss
    api_response = api_instance.get_report_profit_and_loss(from_date=from_date, to_date=to_date, periods=periods, timeframe=timeframe, tracking_category_id=tracking_category_id, tracking_category_id2=tracking_category_id2, tracking_option_id=tracking_option_id, tracking_option_id2=tracking_option_id2, standard_layout=standard_layout, payments_only=payments_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_profit_and_loss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_date** | **date**| The from date for the ProfitAndLoss report e.g. 2018-03-31 | [optional] 
 **to_date** | **date**| The to date for the ProfitAndLoss report e.g. 2018-03-31 | [optional] 
 **periods** | **int**| The number of periods to compare (integer between 1 and 12) | [optional] 
 **timeframe** | **str**| The period size to compare to (MONTH, QUARTER, YEAR) | [optional] 
 **tracking_category_id** | **str**| The trackingCategory 1 for the ProfitAndLoss report | [optional] 
 **tracking_category_id2** | **str**| The trackingCategory 2 for the ProfitAndLoss report | [optional] 
 **tracking_option_id** | **str**| The tracking option 1 for the ProfitAndLoss report | [optional] 
 **tracking_option_id2** | **str**| The tracking option 2 for the ProfitAndLoss report | [optional] 
 **standard_layout** | **bool**| Return the standard layout for the ProfitAndLoss report | [optional] 
 **payments_only** | **bool**| Return cash only basis for the ProfitAndLoss report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_ten_ninety_nine**
> Reports get_report_ten_ninety_nine(report_year=report_year)

Allows you to retrieve report for TenNinetyNine

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
report_year = 'report_year_example' # str | The year of the 1099 report (optional)

try:
    # Allows you to retrieve report for TenNinetyNine
    api_response = api_instance.get_report_ten_ninety_nine(report_year=report_year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_ten_ninety_nine: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_year** | **str**| The year of the 1099 report | [optional] 

### Return type

[**Reports**](Reports.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Reports |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_trial_balance**
> ReportWithRows get_report_trial_balance(date=date, payments_only=payments_only)

Allows you to retrieve report for TrialBalance

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
date = '2013-10-20' # date | The date for the Trial Balance report e.g. 2018-03-31 (optional)
payments_only = True # bool | Return cash only basis for the Trial Balance report (optional)

try:
    # Allows you to retrieve report for TrialBalance
    api_response = api_instance.get_report_trial_balance(date=date, payments_only=payments_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_report_trial_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date** | **date**| The date for the Trial Balance report e.g. 2018-03-31 | [optional] 
 **payments_only** | **bool**| Return cash only basis for the Trial Balance report | [optional] 

### Return type

[**ReportWithRows**](ReportWithRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ReportWithRows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_rates**
> TaxRates get_tax_rates(where=where, order=order, tax_type=tax_type)

Allows you to retrieve Tax Rates

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
tax_type = 'tax_type_example' # str | Filter by tax type (optional)

try:
    # Allows you to retrieve Tax Rates
    api_response = api_instance.get_tax_rates(where=where, order=order, tax_type=tax_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_tax_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **tax_type** | **str**| Filter by tax type | [optional] 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TaxRates array with TaxRates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracking_categories**
> TrackingCategories get_tracking_categories(where=where, order=order, include_archived=include_archived)

Allows you to retrieve tracking categories and options

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)
include_archived = True # bool | e.g. includeArchived=true - Categories and options with a status of ARCHIVED will be included in the response (optional)

try:
    # Allows you to retrieve tracking categories and options
    api_response = api_instance.get_tracking_categories(where=where, order=order, include_archived=include_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_tracking_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 
 **include_archived** | **bool**| e.g. includeArchived&#x3D;true - Categories and options with a status of ARCHIVED will be included in the response | [optional] 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TrackingCategories array of TrackingCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tracking_category**
> TrackingCategories get_tracking_category(tracking_category_id)

Allows you to retrieve tracking categories and options for specified category

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
tracking_category_id = 'tracking_category_id_example' # str | Unique identifier for a TrackingCategory

try:
    # Allows you to retrieve tracking categories and options for specified category
    api_response = api_instance.get_tracking_category(tracking_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TrackingCategories array of specified TrackingCategory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> Users get_user(user_id)

Allows you to retrieve a specified user

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
user_id = 'user_id_example' # str | Unique identifier for a User

try:
    # Allows you to retrieve a specified user
    api_response = api_instance.get_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| Unique identifier for a User | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Users array of specified User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> Users get_users(if_modified_since=if_modified_since, where=where, order=order)

Allows you to retrieve users

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
if_modified_since = '2013-10-20T19:20:30+01:00' # datetime | Only records created or modified since this timestamp will be returned (optional)
where = 'where_example' # str | Filter by an any element (optional)
order = 'order_example' # str | Order by an any element (optional)

try:
    # Allows you to retrieve users
    api_response = api_instance.get_users(if_modified_since=if_modified_since, where=where, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **if_modified_since** | **datetime**| Only records created or modified since this timestamp will be returned | [optional] 
 **where** | **str**| Filter by an any element | [optional] 
 **order** | **str**| Order by an any element | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Users array of all User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account**
> Accounts update_account(account_id, accounts)

Allows you to update a chart of accounts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account_id = 'account_id_example' # str | Unique identifier for retrieving single object
accounts = { "Accounts":[ { "Code":"123456", "Name":"BarFoo", "AccountID":"99ce6032-0678-4aa0-8148-240c75fee33a", "Type":"EXPENSE", "Description":"GoodBye World", "TaxType":"INPUT", "EnablePaymentsToAccount":false, "ShowInExpenseClaims":false, "Class":"EXPENSE", "ReportingCode":"EXP", "ReportingCodeName":"Expense", "UpdatedDateUTC":"2019-02-21T16:29:47.96-08:00" } ] } # Accounts | Request of type Accounts array with one Account

try:
    # Allows you to update a chart of accounts
    api_response = api_instance.update_account(account_id, accounts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| Unique identifier for retrieving single object | 
 **accounts** | [**Accounts**](Accounts.md)| Request of type Accounts array with one Account | 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - update existing Account and return response of type Accounts array with updated Account |  -  |
**400** | Validation Error - some data was incorrect returns response of type Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_account_attachment_by_file_name**
> Attachments update_account_attachment_by_file_name(account_id, file_name, body)

Allows you to update Attachment on Account by Filename

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
account_id = 'account_id_example' # str | Unique identifier for Account object
file_name = 'file_name_example' # str | Name of the attachment
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to update Attachment on Account by Filename
    api_response = api_instance.update_account_attachment_by_file_name(account_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_account_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)| Unique identifier for Account object | 
 **file_name** | **str**| Name of the attachment | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array of Attachment |  -  |
**400** | Validation Error - some data was incorrect returns response of type Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_transaction**
> BankTransactions update_bank_transaction(bank_transaction_id, bank_transactions)

Allows you to update a single spend or receive money transaction

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction
bank_transactions = { "BankTransactions":[ { "Type":"SPEND", "Contact":{ "ContactID":"5cc8cf28-567e-4d43-b287-687cfcaec47c", "ContactStatus":"ACTIVE", "Name":"Katherine Warren", "FirstName":"Katherine", "LastName":"Warren", "EmailAddress":"kat.warren@clampett.com", "ContactPersons":[
], "BankAccountDetails":"", "Addresses":[ { "AddressType":"STREET", "City":"", "Region":"", "PostalCode":"", "Country":"" }, { "AddressType":"POBOX", "AddressLine1":"", "AddressLine2":"", "AddressLine3":"", "AddressLine4":"", "City":"Palo Alto", "Region":"CA", "PostalCode":"94020", "Country":"United States" } ], "Phones":[ { "PhoneType":"DEFAULT", "PhoneNumber":"847-1294", "PhoneAreaCode":"(626)", "PhoneCountryCode":"" }, { "PhoneType":"DDI", "PhoneNumber":"", "PhoneAreaCode":"", "PhoneCountryCode":"" }, { "PhoneType":"FAX", "PhoneNumber":"", "PhoneAreaCode":"", "PhoneCountryCode":"" }, { "PhoneType":"MOBILE", "PhoneNumber":"", "PhoneAreaCode":"", "PhoneCountryCode":"" } ], "UpdatedDateUTC":"2017-08-21T13:49:04.227-07:00", "ContactGroups":[
] }, "Lineitems":[
], "BankAccount":{ "Code":"088", "Name":"Business Wells Fargo", "AccountID":"6f7594f2-f059-4d56-9e67-47ac9733bfe9" }, "IsReconciled":false, "Date":"2019-02-25", "Reference":"You just updated", "CurrencyCode":"USD", "CurrencyRate":1.0, "Status":"AUTHORISED", "LineAmountTypes":"Inclusive", "TotalTax":1.74, "BankTransactionID":"1289c190-e46d-434b-9628-463ffdb52f00", "UpdatedDateUTC":"2019-02-26T12:39:27.813-08:00" } ] } # BankTransactions | 

try:
    # Allows you to update a single spend or receive money transaction
    api_response = api_instance.update_bank_transaction(bank_transaction_id, bank_transactions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_bank_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **bank_transactions** | [**BankTransactions**](BankTransactions.md)|  | 

### Return type

[**BankTransactions**](BankTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type BankTransactions array with updated BankTransaction |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_transaction_attachment_by_file_name**
> Attachments update_bank_transaction_attachment_by_file_name(bank_transaction_id, file_name, body)

Allows you to update an Attachment on BankTransaction by Filename

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transaction_id = 'bank_transaction_id_example' # str | Xero generated unique identifier for a bank transaction
file_name = 'file_name_example' # str | The name of the file being attached
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to update an Attachment on BankTransaction by Filename
    api_response = api_instance.update_bank_transaction_attachment_by_file_name(bank_transaction_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_bank_transaction_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transaction_id** | [**str**](.md)| Xero generated unique identifier for a bank transaction | 
 **file_name** | **str**| The name of the file being attached | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of Attachments array of Attachment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_transfer_attachment_by_file_name**
> Attachments update_bank_transfer_attachment_by_file_name(bank_transfer_id, file_name, body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
bank_transfer_id = 'bank_transfer_id_example' # str | Xero generated unique identifier for a bank transfer
file_name = 'file_name_example' # str | The name of the file being attached to a Bank Transfer
body = 'body_example' # str | Byte array of file in body of request

try:
    api_response = api_instance.update_bank_transfer_attachment_by_file_name(bank_transfer_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_bank_transfer_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bank_transfer_id** | [**str**](.md)| Xero generated unique identifier for a bank transfer | 
 **file_name** | **str**| The name of the file being attached to a Bank Transfer | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of Attachments array of 0 to N Attachment for a Bank Transfer |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> Contacts update_contact(contact_id, contacts=contacts)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact
contacts = { "Contacts":[ { "ContactID":"d5be01fb-b09f-4c3a-9c67-e10c2a03412c", "Name":"FooBar" } ] } # Contacts |  (optional)

try:
    api_response = api_instance.update_contact(contact_id, contacts=contacts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **contacts** | [**Contacts**](Contacts.md)|  | [optional] 

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contacts array with an updated Contact |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_attachment_by_file_name**
> Attachments update_contact_attachment_by_file_name(contact_id, file_name, body)



### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_id = 'contact_id_example' # str | Unique identifier for a Contact
file_name = 'file_name_example' # str | Name for the file you are attaching
body = 'body_example' # str | Byte array of file in body of request

try:
    api_response = api_instance.update_contact_attachment_by_file_name(contact_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_contact_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | [**str**](.md)| Unique identifier for a Contact | 
 **file_name** | **str**| Name for the file you are attaching | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with an updated Attachment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_group**
> ContactGroups update_contact_group(contact_group_id, contact_groups=contact_groups)

Allows you to update a Contract Group

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
contact_group_id = 'contact_group_id_example' # str | Unique identifier for a Contact Group
contact_groups = { "ContactGroups":[ { "Name":"Vendor" } ] } # ContactGroups |  (optional)

try:
    # Allows you to update a Contract Group
    api_response = api_instance.update_contact_group(contact_group_id, contact_groups=contact_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_contact_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_group_id** | [**str**](.md)| Unique identifier for a Contact Group | 
 **contact_groups** | [**ContactGroups**](ContactGroups.md)|  | [optional] 

### Return type

[**ContactGroups**](ContactGroups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Contact Groups array of updated Contact Group |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_note**
> CreditNotes update_credit_note(credit_note_id, credit_notes=credit_notes)

Allows you to update a specific credit note

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note
credit_notes = { "CreditNotes":[ { "Type":"ACCPAYCREDIT", "Contact":{ "ContactID":"430fa14a-f945-44d3-9f97-5df5e28441b8" }, "Date":"2019-01-05", "Status":"AUTHORISED", "Reference": "HelloWorld", "LineItems":[ { "Description":"Foobar", "Quantity":2.0, "UnitAmount":20.0, "AccountCode":"400" } ] } ] } # CreditNotes |  (optional)

try:
    # Allows you to update a specific credit note
    api_response = api_instance.update_credit_note(credit_note_id, credit_notes=credit_notes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_credit_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **credit_notes** | [**CreditNotes**](CreditNotes.md)|  | [optional] 

### Return type

[**CreditNotes**](CreditNotes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Credit Notes array with updated CreditNote |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credit_note_attachment_by_file_name**
> Attachments update_credit_note_attachment_by_file_name(credit_note_id, file_name, body)

Allows you to update Attachments on CreditNote by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
credit_note_id = 'credit_note_id_example' # str | Unique identifier for a Credit Note
file_name = 'file_name_example' # str | Name of the file you are attaching to Credit Note
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to update Attachments on CreditNote by file name
    api_response = api_instance.update_credit_note_attachment_by_file_name(credit_note_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_credit_note_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_note_id** | [**str**](.md)| Unique identifier for a Credit Note | 
 **file_name** | **str**| Name of the file you are attaching to Credit Note | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with updated Attachment for specific Credit Note |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee**
> Employees update_employee(employee_id, employees)

Allows you to update a specific employee used in Xero payrun

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
employee_id = 'employee_id_example' # str | Unique identifier for a Employee
employees = { "Employees":[ { "EmployeeID":"ad3db144-6362-459c-8c36-5d31d196e629", "FirstName":"Bruce", "LastName":"Banner" } ] } # Employees | 

try:
    # Allows you to update a specific employee used in Xero payrun
    api_response = api_instance.update_employee(employee_id, employees)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | [**str**](.md)| Unique identifier for a Employee | 
 **employees** | [**Employees**](Employees.md)|  | 

### Return type

[**Employees**](Employees.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Employees array with updated Employee |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_expense_claim**
> ExpenseClaims update_expense_claim(expense_claim_id, expense_claims)

Allows you to update specified expense claims

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
expense_claim_id = 'expense_claim_id_example' # str | Unique identifier for a ExpenseClaim
expense_claims = { "ExpenseClaims":[ { "Status":"AUTHORISED", "User":{ "UserID":"d1164823-0ac1-41ad-987b-b4e30fe0b273" }, "Receipts":[ { "Lineitems":[
], "ReceiptID":"dc1c7f6d-0a4c-402f-acac-551d62ce5816" } ] } ] } # ExpenseClaims | 

try:
    # Allows you to update specified expense claims
    api_response = api_instance.update_expense_claim(expense_claim_id, expense_claims)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_expense_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expense_claim_id** | [**str**](.md)| Unique identifier for a ExpenseClaim | 
 **expense_claims** | [**ExpenseClaims**](ExpenseClaims.md)|  | 

### Return type

[**ExpenseClaims**](ExpenseClaims.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ExpenseClaims array with updated ExpenseClaim |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> Invoices update_invoice(invoice_id, invoices)

Allows you to update a specified sales invoices or purchase bills

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice
invoices = { "Invoices":[ { "LineItems":[
], "Reference":"My the Force be With You", "InvoiceID":"4074292c-09b3-456d-84e7-add864c6c39b" } ] } # Invoices | 

try:
    # Allows you to update a specified sales invoices or purchase bills
    api_response = api_instance.update_invoice(invoice_id, invoices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **invoices** | [**Invoices**](Invoices.md)|  | 

### Return type

[**Invoices**](Invoices.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Invoices array with updated Invoice |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice_attachment_by_file_name**
> Attachments update_invoice_attachment_by_file_name(invoice_id, file_name, body)

Allows you to update Attachment on invoices or purchase bills by it's filename

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
invoice_id = 'invoice_id_example' # str | Unique identifier for an Invoice
file_name = 'file_name_example' # str | Name of the file you are attaching
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to update Attachment on invoices or purchase bills by it's filename
    api_response = api_instance.update_invoice_attachment_by_file_name(invoice_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | [**str**](.md)| Unique identifier for an Invoice | 
 **file_name** | **str**| Name of the file you are attaching | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with updated Attachment |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_item**
> Items update_item(item_id, items)

Allows you to udpate a specified item

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
item_id = 'item_id_example' # str | Unique identifier for an Item
items = { "Items":[ { "Code":"abc38306", "Description":"Hello Xero" } ] } # Items | 

try:
    # Allows you to udpate a specified item
    api_response = api_instance.update_item(item_id, items)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | [**str**](.md)| Unique identifier for an Item | 
 **items** | [**Items**](Items.md)|  | 

### Return type

[**Items**](Items.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Items array with updated Item |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_linked_transaction**
> LinkedTransactions update_linked_transaction(linked_transaction_id, linked_transactions)

Allows you to update a specified linked transactions (billable expenses)

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
linked_transaction_id = 'linked_transaction_id_example' # str | Unique identifier for a LinkedTransaction
linked_transactions = { "LinkedTransactions":[ { "ContactID":"4e1753b9-018a-4775-b6aa-1bc7871cfee3" } ] } # LinkedTransactions | 

try:
    # Allows you to update a specified linked transactions (billable expenses)
    api_response = api_instance.update_linked_transaction(linked_transaction_id, linked_transactions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_linked_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_transaction_id** | [**str**](.md)| Unique identifier for a LinkedTransaction | 
 **linked_transactions** | [**LinkedTransactions**](LinkedTransactions.md)|  | 

### Return type

[**LinkedTransactions**](LinkedTransactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type LinkedTransactions array with updated LinkedTransaction |  -  |
**400** | Success - return response of type LinkedTransactions array with updated LinkedTransaction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_manual_journal**
> ManualJournals update_manual_journal(manual_journal_id, manual_journals)

Allows you to update a specified manual journal

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
manual_journal_id = 'manual_journal_id_example' # str | Unique identifier for a ManualJournal
manual_journals = { "ManualJournals":[ { "Narration":"Hello Xero", "JournalLines":[
], "ManualJournalID":"07eac261-78ef-47a0-a0eb-a57b74137877" } ] } # ManualJournals | 

try:
    # Allows you to update a specified manual journal
    api_response = api_instance.update_manual_journal(manual_journal_id, manual_journals)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_manual_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **manual_journals** | [**ManualJournals**](ManualJournals.md)|  | 

### Return type

[**ManualJournals**](ManualJournals.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type ManualJournals array with an updated ManualJournal |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_manual_journal_attachment_by_file_name**
> Attachments update_manual_journal_attachment_by_file_name(manual_journal_id, file_name, body)

Allows you to update a specified Attachment on ManualJournal by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
manual_journal_id = 'manual_journal_id_example' # str | Unique identifier for a ManualJournal
file_name = 'file_name_example' # str | The name of the file being attached to a ManualJournal
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to update a specified Attachment on ManualJournal by file name
    api_response = api_instance.update_manual_journal_attachment_by_file_name(manual_journal_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_manual_journal_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_journal_id** | [**str**](.md)| Unique identifier for a ManualJournal | 
 **file_name** | **str**| The name of the file being attached to a ManualJournal | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with an update Attachment for a ManualJournals |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_purchase_order**
> PurchaseOrders update_purchase_order(purchase_order_id, purchase_orders)

Allows you to update a specified purchase order

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
purchase_order_id = 'purchase_order_id_example' # str | Unique identifier for a PurchaseOrder
purchase_orders = { "PurchaseOrders":[ { "LineItems":[
], "AttentionTo":"Jimmy" } ] } # PurchaseOrders | 

try:
    # Allows you to update a specified purchase order
    api_response = api_instance.update_purchase_order(purchase_order_id, purchase_orders)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_purchase_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purchase_order_id** | [**str**](.md)| Unique identifier for a PurchaseOrder | 
 **purchase_orders** | [**PurchaseOrders**](PurchaseOrders.md)|  | 

### Return type

[**PurchaseOrders**](PurchaseOrders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type PurchaseOrder array for updated PurchaseOrder |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receipt**
> Receipts update_receipt(receipt_id, receipts)

Allows you to retrieve a specified draft expense claim receipts

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt
receipts = { "Receipts":[ { "Lineitems":[
], "User":{ "UserID":"d1164823-0ac1-41ad-987b-b4e30fe0b273" }, "Reference":"Foobar" } ] } # Receipts | 

try:
    # Allows you to retrieve a specified draft expense claim receipts
    api_response = api_instance.update_receipt(receipt_id, receipts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **receipts** | [**Receipts**](Receipts.md)|  | 

### Return type

[**Receipts**](Receipts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Receipts array for updated Receipt |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_receipt_attachment_by_file_name**
> Attachments update_receipt_attachment_by_file_name(receipt_id, file_name, body)

Allows you to update Attachment on expense claim receipts by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
receipt_id = 'receipt_id_example' # str | Unique identifier for a Receipt
file_name = 'file_name_example' # str | The name of the file being attached to the Receipt
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to update Attachment on expense claim receipts by file name
    api_response = api_instance.update_receipt_attachment_by_file_name(receipt_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_receipt_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | [**str**](.md)| Unique identifier for a Receipt | 
 **file_name** | **str**| The name of the file being attached to the Receipt | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with updated Attachment for a specified Receipt |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repeating_invoice_attachment_by_file_name**
> Attachments update_repeating_invoice_attachment_by_file_name(repeating_invoice_id, file_name, body)

Allows you to update specified attachment on repeating invoices by file name

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
repeating_invoice_id = 'repeating_invoice_id_example' # str | Unique identifier for a Repeating Invoice
file_name = 'file_name_example' # str | The name of the file being attached to a Repeating Invoice
body = 'body_example' # str | Byte array of file in body of request

try:
    # Allows you to update specified attachment on repeating invoices by file name
    api_response = api_instance.update_repeating_invoice_attachment_by_file_name(repeating_invoice_id, file_name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_repeating_invoice_attachment_by_file_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repeating_invoice_id** | [**str**](.md)| Unique identifier for a Repeating Invoice | 
 **file_name** | **str**| The name of the file being attached to a Repeating Invoice | 
 **body** | **str**| Byte array of file in body of request | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type Attachments array with specified Attachment for a specified Repeating Invoice |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_rate**
> TaxRates update_tax_rate(tax_rates)

Allows you to update Tax Rates

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
tax_rates = { "TaxRates":[ { "Name":"SDKTax29067", "TaxComponents":[ { "Name":"State Tax", "Rate":2.25 } ], "Status":"DELETED", "ReportTaxType":"INPUT" } ] } # TaxRates | 

try:
    # Allows you to update Tax Rates
    api_response = api_instance.update_tax_rate(tax_rates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_tax_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rates** | [**TaxRates**](TaxRates.md)|  | 

### Return type

[**TaxRates**](TaxRates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TaxRates array updated TaxRate |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tracking_category**
> TrackingCategories update_tracking_category(tracking_category_id, tracking_category)

Allows you to update tracking categories

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = openapi_client.AccountingApi()
tracking_category_id = 'tracking_category_id_example' # str | Unique identifier for a TrackingCategory
tracking_category = { "Name":"BarFoo" } # TrackingCategory | 

try:
    # Allows you to update tracking categories
    api_response = api_instance.update_tracking_category(tracking_category_id, tracking_category)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingApi->update_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tracking_category_id** | [**str**](.md)| Unique identifier for a TrackingCategory | 
 **tracking_category** | [**TrackingCategory**](TrackingCategory.md)|  | 

### Return type

[**TrackingCategories**](TrackingCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - return response of type TrackingCategories array of updated TrackingCategory |  -  |
**400** | A failed request due to validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

