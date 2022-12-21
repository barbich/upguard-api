# Vendor

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **dict(str, str)** | The attributes applied to the vendor. If no attributes are applied this field will be omitted | [optional] 
**automated_score** | **int** | The automated score of the vendor without questionnaire. Omitted if no current scanning score. | [optional] 
**category_scores** | [**CategoryScores**](CategoryScores.md) |  | [optional] 
**id** | **int** | The id of the vendor. Its possible for a hostname to change which vendor it belongs to for a number of reasons (eg. Company&#39;s legal entity changes, improved data quality, etc...). For this reason, do not assume a hostname will always return the same vendor id. | [optional] 
**industry_group** | **str** | The industry group this vendor falls into. | [optional] 
**industry_sector** | **str** | The industry sector this vendor falls into. Industry sectors contain multiple industry groups. | [optional] 
**labels** | **list[str]** | The labels applied to the vendor. If no labels are present this field will be omitted. | [optional] 
**name** | **str** | The name of the vendor | [optional] 
**overall_score** | **int** | The current score of the vendor including automated and questionnaire. Omitted if no current overall score. | [optional] 
**primary_hostname** | **str** | The primary hostname of the vendor | [optional] 
**questionnaire_score** | **int** | The current questionnaire score of the vendor. Omitted if no current questionnaire score. | [optional] 
**score** | **int** | NOTE: deprecated (use AutomatedScore). The current automated score of the vendor. A -1 value represents no current score for the vendor. | [optional] 
**tier** | **int** | The tier applied to the vendor. If no tier is applied to the vendor this field will be omitted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


