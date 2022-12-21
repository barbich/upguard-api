# RiskWaiver

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_at** | **datetime** | Time the risk waiver was activated (RFC 3339 format) | [optional] 
**all_hostnames** | **bool** | Flag indicating whether the risk has been waived for all hostnames | [optional] 
**approved_by** | **str** | Email address of the user who approved the risk waiver. This field will be omitted if not applicable, e.g. self approved risk waivers. | [optional] 
**created_by** | **str** | Email address of the user who created the risk waiver | [optional] 
**expires_at** | **datetime** | Time the risk waiver will expire (RFC 3339 format). If the risk waiver is set not to expire this field will be omitted. | [optional] 
**hostnames** | **list[str]** | The list of hostnames the risk has been waived for. The field will be omitted if all_hostnames is true. | [optional] 
**justification** | **str** | Justification for the risk waiver. If not available this field will be omitted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


