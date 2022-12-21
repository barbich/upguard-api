# VendorsRisk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The risk category identifier | [optional] 
**description** | **str** | Description of the risk | [optional] 
**finding** | **str** | A short description of the finding | [optional] 
**id** | **str** | The risk identifier | [optional] 
**risk_subtype** | **str** | The subtype of the risk, e.g. the subtype of the verified_vuln:CVE-2021-34473 is CVE-2021-34473. This field will be empty if the risk has no subtype, e.g. for wp_version_exposed, or for generic risks like verified_vuln:* where the subtype is only determined when the full risk is specified. | [optional] 
**risk_type** | **str** | The type of the risk, e.g. the type of the verified_vuln:CVE-2021-34473 is verified_vuln | [optional] 
**severity** | **str** | The risk severity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


