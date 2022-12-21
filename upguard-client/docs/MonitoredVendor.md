# MonitoredVendor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessment_status** | **str** | Assessment status for the vendor. Possible values are Published, In progress, Not assessed. The field will be omitted for non monitored vendors. | [optional] 
**attributes** | **dict(str, str)** | The attributes applied to the vendor. If no attributes are applied this field will be omitted | [optional] 
**automated_score** | **int** | The current automated score of the vendor without questionnaire. Omitted if no current scanning score. | [optional] 
**category_scores** | [**CategoryScores**](CategoryScores.md) |  | [optional] 
**id** | **int** | The id of the vendor. Its possible for a hostname to change which vendor it belongs to for a number of reasons (eg. Company&#39;s legal entity changes, improved data quality, etc...). For this reason, do not assume a hostname will always return the same vendor id. | [optional] 
**labels** | **list[str]** | Labels that the vendor is currently associated with. | [optional] 
**last_assessed** | **datetime** | Date of the last assessment for the vendor. The field will be omitted if no published assessment is present. | [optional] 
**monitored** | **bool** | Indicates whether the vendor is monitored or not. | [optional] 
**name** | **str** | The name of the vendor | [optional] 
**overall_score** | **int** | The current score of the vendor including automated and questionnaire. Omitted if no current overall score. | [optional] 
**primary_hostname** | **str** | The primary hostname of the vendor | [optional] 
**questionnaire_score** | **int** | The current questionnaire score of the vendor. Omitted if no current questionnaire score. | [optional] 
**risks** | [**list[VendorsRisk]**](VendorsRisk.md) | Optional list of risks for the vendor. Note that this is a summary list of risks and does not take into account risk waivers. To have a precise view of a vendor risks use the /risks/vendors endpoint. | [optional] 
**score** | **int** | NOTE: deprecated (use OverallScore). The current score of the vendor. A -1 value represents no current score for the vendor. | [optional] 
**tier** | **int** | Tier currently assigned to the vendor. Omitted if no tier is assigned to the vendor. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


