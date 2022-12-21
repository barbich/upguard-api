# TyposquatPermutationDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_records** | **list[str]** | The list of A records associated with the permutation. If no A records are associated with the permutation this field will be omitted. | [optional] 
**country** | **str** | The country where the permutation is registered. If missing the field will be omitted. | [optional] 
**date_detected** | **datetime** | The date the registered permutation was detected in RFC3339 format. If missing this field will be omitted. | [optional] 
**hostname** | **str** | The hostname of the permutation | [optional] 
**mx_records** | **list[str]** | The list of MX records associated with the permutation. If no MX records are associated with the permutation this field will be omitted. | [optional] 
**ns_records** | **list[str]** | The list of NS records associated with the permutation. If no NS records are associated with the permutation this field will be omitted. | [optional] 
**permutation_type** | [**PermutationType**](PermutationType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


