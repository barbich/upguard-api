# Diff

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_a** | **datetime** | The date of the first scan (RFC 3339 format) | [optional] 
**date_b** | **datetime** | The date of the second scan (RFC 3339 format) | [optional] 
**expected** | **str** | The expected status | [optional] 
**hostname** | **str** | The domain name or IP address experiencing the risk diff | [optional] 
**meta_value_a** | **str** | Metadata for the result of the first check | [optional] 
**meta_value_b** | **str** | Metadata for the result of the second check | [optional] 
**_property** | **str** | The property checked | [optional] 
**status_a** | [**DiffStatus**](DiffStatus.md) |  | [optional] 
**status_b** | [**DiffStatus**](DiffStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


