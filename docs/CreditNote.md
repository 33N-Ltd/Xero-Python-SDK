# CreditNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | See Credit Note Types | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**date** | **date** | The date the credit note is issued YYYY-MM-DD. If the Date element is not specified then it will default to the current date based on the timezone setting of the organisation | [optional] 
**status** | **str** | See Credit Note Status Codes | [optional] 
**line_amount_types** | [**LineAmountTypes**](LineAmountTypes.md) |  | [optional] 
**line_items** | [**list[LineItem]**](LineItem.md) | See Invoice Line Items | [optional] 
**sub_total** | **float** | The subtotal of the credit note excluding taxes | [optional] 
**total_tax** | **float** | The total tax on the credit note | [optional] 
**total** | **float** | The total of the Credit Note(subtotal + total tax) | [optional] 
**updated_date_utc** | **datetime** | UTC timestamp of last update to the credit note | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**fully_paid_on_date** | **date** | Date when credit note was fully paid(UTC format) | [optional] 
**credit_note_id** | **str** | Xero generated unique identifier | [optional] 
**credit_note_number** | **str** | ACCRECCREDIT – Unique alpha numeric code identifying credit note (when missing will auto-generate from your Organisation Invoice Settings) | [optional] 
**reference** | **str** | ACCRECCREDIT only – additional reference number | [optional] 
**sent_to_contact** | **bool** | boolean to indicate if a credit note has been sent to a contact via  the Xero app (currently read only) | [optional] 
**currency_rate** | **float** | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used | [optional] 
**remaining_credit** | **float** | The remaining credit balance on the Credit Note | [optional] 
**allocations** | [**list[Allocation]**](Allocation.md) | See Allocations | [optional] 
**payments** | [**list[Payment]**](Payment.md) | See Payments | [optional] 
**branding_theme_id** | **str** | See BrandingThemes | [optional] 
**has_attachments** | **bool** | boolean to indicate if a credit note has an attachment | [optional] 
**validation_errors** | [**list[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


