# GetIpDetailsV1RespBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_name** | **str** | The name of the AS the IP belongs to. If no AS is available for an IP this field will be omitted. | [optional] 
**asn** | **int** | The ASN the IP belongs to. If no ASN is available for an IP this field will be omitted. | [optional] 
**automated_score** | **int** | The score of the ip. If the ip is inactive or hasn&#39;t been scanned yet this field will be absent | [optional] 
**check_results** | [**list[CheckResult]**](CheckResult.md) | The results of the IP scan. This field will be omitted if the IP has not been scanned or no results are available, e.g. DNS source IP. | [optional] 
**country** | **str** | The country the IP belongs to. If no country is available for an IP this field will be omitted. | [optional] 
**domains** | [**list[DomainScore]**](DomainScore.md) | The list of domains associated with this IP. This field will be omitted if no domains are associated with the IP. | [optional] 
**ip** | **str** | The IP. | [optional] 
**labels** | **list[str]** | The labels associated with the IP. | [optional] 
**owner** | **str** | The owner of the IP. | [optional] 
**services** | **list[str]** | The list of discovered services IP. If no services were detected for the IP this field will be omitted. | [optional] 
**sources** | [**list[IPSource]**](IPSource.md) | The sources of the IP. | [optional] 
**waived_check_results** | [**list[CheckResult]**](CheckResult.md) | The waived risks for this IP. This field will be omitted if no waived risks are present. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


