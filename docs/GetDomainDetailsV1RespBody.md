# GetDomainDetailsV1RespBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_records** | **list[str]** | The list of A records associated with the domain. This field will be omitted if no A records were associated with the domain | [optional] 
**automated_score** | **int** | The score for the domain. If the domain has not been scanned or no score is present this field will be omitted. | [optional] 
**check_results** | [**list[CheckResult]**](CheckResult.md) | The results of the domain scan. This field will be omitted if the domain has not been scanned or no results are available. | [optional] 
**hostname** | **str** | The hostname of the domain | [optional] 
**labels** | **list[str]** | The labels associated with the domain. This field will be omitted if no labels are present. | [optional] 
**scanned_at** | **datetime** | The time the domain was scanned in RFC3339 format | [optional] 
**waived_check_results** | [**list[CheckResult]**](CheckResult.md) | The waived risks for this domain. This field will be omitted if no waived risks are present. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


