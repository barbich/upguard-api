# CheckResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual** | [**list[ModelProperty]**](ModelProperty.md) | The found properties of the check | [optional] 
**category** | [**Category**](Category.md) |  | [optional] 
**checked_at** | **datetime** | The time the check was performed in RFC3339 format | [optional] 
**description** | **str** | The description of the check performed | [optional] 
**expected** | [**list[ModelProperty]**](ModelProperty.md) | The expected properties of the check | [optional] 
**id** | **str** | The ID of the check | [optional] 
**_pass** | **bool** | Flag indicating whether the check passed or not | [optional] 
**risk_subtype** | **str** | The subtype of the risk, e.g. the subtype of the verified_vuln:CVE-2021-34473 is CVE-2021-34473. This field will be empty if the risk has no subtype, e.g. for wp_version_exposed, or for generic risks like verified_vuln:* where the subtype is only determined when the full risk is specified. | [optional] 
**risk_type** | **str** | The type of the risk, e.g. the type of the verified_vuln:CVE-2021-34473 is verified_vuln | [optional] 
**severity** | [**Severity**](Severity.md) |  | [optional] 
**severity_name** | **str** | The severity fo the risk in human-readable form | [optional] 
**sources** | **list[str]** | Sources contains information about the source of a check e.g. the IP addresses it was found on, or a domain name | [optional] 
**title** | **str** | The title of the check | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


