# RiskDiff

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category of the risk group | [optional] 
**description** | **str** | Description of the risk | [optional] 
**group** | **str** | The ID of the risk class | [optional] 
**id** | **str** | The ID of risk | [optional] 
**name** | **str** | The name of the risk | [optional] 
**risk_subtype** | **str** | The subtype of the risk, e.g. the subtype of the verified_vuln:CVE-2021-34473 is CVE-2021-34473. This field will be empty if the risk has no subtype, e.g. for wp_version_exposed, or for generic risks like verified_vuln:* where the subtype is only determined when the full risk is specified. | [optional] 
**risk_type** | **str** | The type of the risk, e.g. the type of the verified_vuln:CVE-2021-34473 is verified_vuln | [optional] 
**scan_diffs** | [**list[ScanDiff]**](ScanDiff.md) | The differences between our automated scans | [optional] 
**severity** | **int** | The severity of the risk | [optional] 
**severity_name** | **str** | The severity of the risks in human-readable form | [optional] 
**vendor_diff** | [**VendorDiff**](VendorDiff.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


