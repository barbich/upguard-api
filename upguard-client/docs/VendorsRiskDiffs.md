# VendorsRiskDiffs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the vendor. Its possible for a hostname to change which vendor it belongs to for a number of reasons (eg. Company&#39;s legal entity changes, improved data quality, etc...). For this reason, do not assume a hostname will always return the same vendor id. | [optional] 
**name** | **str** | The name of the vendor | [optional] 
**primary_hostname** | **str** | The primary hostname of the vendor | [optional] 
**risks_introduced** | [**list[RiskDiffGroup]**](RiskDiffGroup.md) | The risks introduced between start date and end date grouped by class | [optional] 
**risks_resolved** | [**list[RiskDiffGroup]**](RiskDiffGroup.md) | The risks resolved between start date and end date grouped by class | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


