# IP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_name** | **str** | The name of the AS the IP belongs to. If no AS is available for an IP this field will be omitted. | [optional] 
**asn** | **int** | The ASN the IP belongs to. If no ASN is available for an IP this field will be omitted. | [optional] 
**automated_score** | **int** | The score of the ip. If the ip is inactive or hasn&#39;t been scanned yet this field will be absent | [optional] 
**country** | **str** | The country the IP belongs to. If no country is available for an IP this field will be omitted. | [optional] 
**ip** | **str** | The IP. | [optional] 
**labels** | **list[str]** | The labels associated with the IP. | [optional] 
**owner** | **str** | The owner of the IP. | [optional] 
**services** | **list[str]** | The list of discovered services IP. If no services were detected for the IP this field will be omitted. | [optional] 
**sources** | [**list[IPSource]**](IPSource.md) | The sources of the IP. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


