# BulkHostname

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | The active state of the hostname. These will be omitted if the omit_scan_info query parameter is true. | [optional] 
**automated_score** | **int** | The automated score of the hostname. This will be omitted if the omit_scan_info query parameter is true. | [optional] 
**hostname** | **str** | The name of the hostname. | [optional] 
**labels** | **list[str]** | The list of labels associated with the hostname. This will be omitted if the omit_labels query parameter is true. | [optional] 
**last_scanned_at** | **datetime** | The timestamp this hostname was last scanned at. | [optional] 
**risks** | [**list[BulkRisk]**](BulkRisk.md) | The list of risks associated with the hostname. These will be omitted if the omit_scan_info query parameter is true. | [optional] 
**vendor** | [**BulkVendor**](BulkVendor.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


