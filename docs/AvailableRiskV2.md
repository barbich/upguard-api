# AvailableRiskV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category of the risk. This field will be omitted for generic risks | [optional] 
**description** | **str** | Detailed description of the risk. This field will be omitted for generic risks | [optional] 
**finding** | **str** | Description of the finding. This field will be omitted for generic risks | [optional] 
**generic** | **bool** | Flag indicating whether the risks is a generic risk, i.e. a risk where severity, category, finding etc. depend on other parameters | [optional] 
**group** | **str** | The risk group | [optional] 
**id** | **str** | The ID of the risk | [optional] 
**remediation** | **str** | Remediation recommendation. This field will be omitted for generic risks | [optional] 
**risk** | **str** | The risk title | [optional] 
**risk_subtype** | **str** | The subtype of the risk, e.g. the subtype of the verified_vuln:CVE-2021-34473 is CVE-2021-34473. This field will be empty if the risk has no subtype, e.g. for wp_version_exposed, or for generic risks like verified_vuln:* where the subtype is only determined when the full risk is specified. | [optional] 
**risk_type** | **str** | The type of the risk, e.g. the type of the verified_vuln:CVE-2021-34473 is verified_vuln | [optional] 
**severity** | **str** | The severity of the risk. This field will be omitted for generic risks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


