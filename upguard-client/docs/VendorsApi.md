# upguard.VendorsApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**additional_evidence**](VendorsApi.md#additional_evidence) | **GET** /vendor/additionalevidence | Retrieve (one or more) vendor additional evidence documents by id
[**additional_evidences_list**](VendorsApi.md#additional_evidences_list) | **GET** /vendor/additionalevidence/list | List vendor additional evidence instances
[**attachment**](VendorsApi.md#attachment) | **GET** /vendor/questionnaire/attachment | Retrieve (one or more) vendor questionnaire attachments by id
[**attachments**](VendorsApi.md#attachments) | **GET** /vendor/questionnaire/attachment/list | List vendor questionnaire attachments
[**document**](VendorsApi.md#document) | **GET** /vendor/document | Retrieve (one or more) vendor documents by id
[**documents**](VendorsApi.md#documents) | **GET** /vendor/documents | List vendor documents
[**questionnaires**](VendorsApi.md#questionnaires) | **GET** /vendor/questionnaires | List vendor questionnaires
[**questionnaires_v2**](VendorsApi.md#questionnaires_v2) | **GET** /vendor/questionnaires/v2 | List vendor questionnaires
[**vendor**](VendorsApi.md#vendor) | **GET** /vendor | Get vendor details
[**vendor_domain_details**](VendorsApi.md#vendor_domain_details) | **GET** /vendor/domain | Retrieve details for a domain
[**vendor_domain_update_labels**](VendorsApi.md#vendor_domain_update_labels) | **PUT** /vendor/domain/labels | Assign labels to an domain
[**vendor_domains**](VendorsApi.md#vendor_domains) | **GET** /vendor/domains | List vendor domains
[**vendor_ip_details**](VendorsApi.md#vendor_ip_details) | **GET** /vendor/ip | Retrieve details for an IP address
[**vendor_ip_update_labels**](VendorsApi.md#vendor_ip_update_labels) | **PUT** /vendor/ip/labels | Assign labels to an IP
[**vendor_ips**](VendorsApi.md#vendor_ips) | **GET** /vendor/ips | List vendor ips
[**vendor_ranges**](VendorsApi.md#vendor_ranges) | **GET** /vendor/ranges | List vendor ip ranges
[**vendor_update_attributes**](VendorsApi.md#vendor_update_attributes) | **PUT** /vendor/attributes | Assign or update the attributes for a vendor
[**vendor_update_labels**](VendorsApi.md#vendor_update_labels) | **PUT** /vendor/labels | Assign labels to a vendor
[**vendor_update_tier**](VendorsApi.md#vendor_update_tier) | **PUT** /vendor/tier | Assign tier to a vendor
[**vendors**](VendorsApi.md#vendors) | **GET** /vendors | List monitored vendors


# **additional_evidence**
> GetVendorAdditionalEvidenceResponsePayload additional_evidence(evidence_ids=evidence_ids, zip=zip)

Retrieve (one or more) vendor additional evidence documents by id

Returns the body of one or more additional evidence documents that have been attached to a specific vendor. If multiple additional evidence documents are requested, then by default the files are returned as a multi-part mime response. Alternately, the zip option can be used to return multiple files as a single zip archive

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
evidence_ids = [56] # list[int] | a comma-separated list of one or more additional evidence instances (by unique id) (optional)
zip = true # bool | indicates that for multiple additional evidence requests, the files should be returned as a multi-file zip (optional)

try:
    # Retrieve (one or more) vendor additional evidence documents by id
    api_response = api_instance.additional_evidence(evidence_ids=evidence_ids, zip=zip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->additional_evidence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evidence_ids** | [**list[int]**](int.md)| a comma-separated list of one or more additional evidence instances (by unique id) | [optional] 
 **zip** | **bool**| indicates that for multiple additional evidence requests, the files should be returned as a multi-file zip | [optional] 

### Return type

[**GetVendorAdditionalEvidenceResponsePayload**](GetVendorAdditionalEvidenceResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/jpeg, image/png, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **additional_evidences_list**
> GetVendorAdditionalEvidencesResponsePayload additional_evidences_list(vendor_primary_hostname=vendor_primary_hostname, page_token=page_token, page_size=page_size)

List vendor additional evidence instances

Returns a list of additional evidence instances that have been uploaded against this vendor in chronological order of when they were uploaded.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to show additional evidence for. (optional)
page_token = 'page_token_example' # str | The token of the page to be returned. Will return the first page if left blank. (optional)
page_size = 789 # int | The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. (optional)

try:
    # List vendor additional evidence instances
    api_response = api_instance.additional_evidences_list(vendor_primary_hostname=vendor_primary_hostname, page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->additional_evidences_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to show additional evidence for. | [optional] 
 **page_token** | **str**| The token of the page to be returned. Will return the first page if left blank. | [optional] 
 **page_size** | **int**| The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. | [optional] 

### Return type

[**GetVendorAdditionalEvidencesResponsePayload**](GetVendorAdditionalEvidencesResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachment**
> GetVendorAttachmentResponsePayload attachment(attachment_ids=attachment_ids, zip=zip)

Retrieve (one or more) vendor questionnaire attachments by id

Returns the body of one or more questionnaire attachments that have been attached to a one or more vendor questionnaire instances. If multiple attachments are requested, then by default the files are returned as a multi-part mime response. Alternately, the zip option can be used to return multiple files as a single zip archive

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
attachment_ids = [56] # list[int] | a comma-separated list of one or more attachments (by unique id) (optional)
zip = true # bool | indicates that for multiple attachment requests, the files should be returned as a multi-file zip (optional)

try:
    # Retrieve (one or more) vendor questionnaire attachments by id
    api_response = api_instance.attachment(attachment_ids=attachment_ids, zip=zip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_ids** | [**list[int]**](int.md)| a comma-separated list of one or more attachments (by unique id) | [optional] 
 **zip** | **bool**| indicates that for multiple attachment requests, the files should be returned as a multi-file zip | [optional] 

### Return type

[**GetVendorAttachmentResponsePayload**](GetVendorAttachmentResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/jpeg, image/png, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments**
> GetVendorQuestionnaireAttachmentsResponsePayload attachments(questionnaire_id=questionnaire_id, page_token=page_token, page_size=page_size)

List vendor questionnaire attachments

Returns a list of questionnaire attachments that have been attached to a specific questionnaire instance in chronological order of when they were uploaded.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
questionnaire_id = 789 # int | The id of the specific questionnaire of whose attachments are of interest (optional)
page_token = 'page_token_example' # str | The token of the page to be returned. Will return the first page if left blank. (optional)
page_size = 789 # int | The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. (optional)

try:
    # List vendor questionnaire attachments
    api_response = api_instance.attachments(questionnaire_id=questionnaire_id, page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_id** | **int**| The id of the specific questionnaire of whose attachments are of interest | [optional] 
 **page_token** | **str**| The token of the page to be returned. Will return the first page if left blank. | [optional] 
 **page_size** | **int**| The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. | [optional] 

### Return type

[**GetVendorQuestionnaireAttachmentsResponsePayload**](GetVendorQuestionnaireAttachmentsResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document**
> GetVendorDocumentResponsePayload document(document_ids=document_ids, zip=zip)

Retrieve (one or more) vendor documents by id

Returns the body of one or more documents that have been attached to a specific vendor. If multiple documents are requested, then by default the files are returned as a multi-part mime response. Alternately, the zip option can be used to return multiple files as a single zip archive

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
document_ids = [56] # list[int] | a comma-separated list of one or more documents (by unique id) (optional)
zip = true # bool | indicates that for multiple document requests, the files should be returned as a multi-file zip (optional)

try:
    # Retrieve (one or more) vendor documents by id
    api_response = api_instance.document(document_ids=document_ids, zip=zip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_ids** | [**list[int]**](int.md)| a comma-separated list of one or more documents (by unique id) | [optional] 
 **zip** | **bool**| indicates that for multiple document requests, the files should be returned as a multi-file zip | [optional] 

### Return type

[**GetVendorDocumentResponsePayload**](GetVendorDocumentResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/jpeg, image/png, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents**
> GetVendorDocumentsResponsePayload documents(vendor_primary_hostname=vendor_primary_hostname, page_token=page_token, page_size=page_size)

List vendor documents

Returns a list of documents that have been uploaded against this vendor in chronological order of when they were uploaded.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to show documents for. (optional)
page_token = 'page_token_example' # str | The token of the page to be returned. Will return the first page if left blank. (optional)
page_size = 789 # int | The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. (optional)

try:
    # List vendor documents
    api_response = api_instance.documents(vendor_primary_hostname=vendor_primary_hostname, page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to show documents for. | [optional] 
 **page_token** | **str**| The token of the page to be returned. Will return the first page if left blank. | [optional] 
 **page_size** | **int**| The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. | [optional] 

### Return type

[**GetVendorDocumentsResponsePayload**](GetVendorDocumentsResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **questionnaires**
> GetVendorQuestionnairesV1ResponsePayload questionnaires(vendor_primary_hostname=vendor_primary_hostname, page_token=page_token, page_size=page_size, usage_type=usage_type)

List vendor questionnaires

Returns a list of questionnaires that have been sent to this vendor in chronological order of when they were sent.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to which the questionnaires were sent. (optional)
page_token = 'page_token_example' # str | The token of the page to be returned. Will return the first page if left blank. (optional)
page_size = 789 # int | The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. (optional)
usage_type = 'usage_type_example' # str | The usage type of questionnaires to return Valid values: security, relationship Defaults to 'security' if not set (optional)

try:
    # List vendor questionnaires
    api_response = api_instance.questionnaires(vendor_primary_hostname=vendor_primary_hostname, page_token=page_token, page_size=page_size, usage_type=usage_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->questionnaires: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to which the questionnaires were sent. | [optional] 
 **page_token** | **str**| The token of the page to be returned. Will return the first page if left blank. | [optional] 
 **page_size** | **int**| The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. | [optional] 
 **usage_type** | **str**| The usage type of questionnaires to return Valid values: security, relationship Defaults to &#39;security&#39; if not set | [optional] 

### Return type

[**GetVendorQuestionnairesV1ResponsePayload**](GetVendorQuestionnairesV1ResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **questionnaires_v2**
> GetVendorQuestionnairesV2ResponsePayload questionnaires_v2(vendor_primary_hostname=vendor_primary_hostname, usage_type=usage_type, exclude_archived=exclude_archived)

List vendor questionnaires

Returns a list of questionnaires that have been sent to this vendor in chronological order of when they were sent.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to which the questionnaires were sent. (optional)
usage_type = 'usage_type_example' # str | The usage type of questionnaires to return Valid values: security, relationship Defaults to 'security' if not set (optional)
exclude_archived = false # bool | Optionally exclude archived questionnaires (optional) (default to false)

try:
    # List vendor questionnaires
    api_response = api_instance.questionnaires_v2(vendor_primary_hostname=vendor_primary_hostname, usage_type=usage_type, exclude_archived=exclude_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->questionnaires_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to which the questionnaires were sent. | [optional] 
 **usage_type** | **str**| The usage type of questionnaires to return Valid values: security, relationship Defaults to &#39;security&#39; if not set | [optional] 
 **exclude_archived** | **bool**| Optionally exclude archived questionnaires | [optional] [default to false]

### Return type

[**GetVendorQuestionnairesV2ResponsePayload**](GetVendorQuestionnairesV2ResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor**
> Vendor vendor(id=id, hostname=hostname, generate_ad_hoc_report=generate_ad_hoc_report, start_monitoring=start_monitoring, labels=labels, tier=tier, wait_for_scan=wait_for_scan)

Get vendor details

The following assertions are evaluated (in order) to determine whether you are licensed to view the vendor data (as soon as one assertion returns \"true\", the vendor data will be returned): 1. You are currently monitoring the vendor in CyberRisk 2. You have set \"start_monitoring\" to \"true\" AND are not currently monitoring all the vendors you are licensed for in CyberRisk 3. You have set \"generate_ad_hoc_report\" to \"true\" and have not currently used your monthly allocation of ad-hoc reports in CyberRisk.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
id = 789 # int | The ID of the vendor for which to return vendor data. e.g. 123456789 (optional)
hostname = 'hostname_example' # str | The hostname for which to return vendor data. e.g. \"upguard.com\". Required when id is not specified. When id is specified this field will be ignored. (optional)
generate_ad_hoc_report = true # bool | When set to true, if you haven't already used your monthly allocation of ad-hoc reports, generate an ad-hoc report for the given vendor, and return the vendor data. (optional)
start_monitoring = true # bool | When set to true, if the vendor is not already being monitored, and if you are not already monitoring all the vendors your are licensed for, start monitoring the vendor, and return the vendor data. (optional)
labels = ['labels_example'] # list[str] | The labels to assign to the vendor if start monitoring set to true. If you want to update the labels for an already monitored vendor use the /vendor/labels endpoint. (optional)
tier = 789 # int | The tier to assign to the vendor if start monitoring is set to true. (optional)
wait_for_scan = false # bool | Flag indicating whether the request should wait for scan results on new unknown vendors (optional) (default to false)

try:
    # Get vendor details
    api_response = api_instance.vendor(id=id, hostname=hostname, generate_ad_hoc_report=generate_ad_hoc_report, start_monitoring=start_monitoring, labels=labels, tier=tier, wait_for_scan=wait_for_scan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the vendor for which to return vendor data. e.g. 123456789 | [optional] 
 **hostname** | **str**| The hostname for which to return vendor data. e.g. \&quot;upguard.com\&quot;. Required when id is not specified. When id is specified this field will be ignored. | [optional] 
 **generate_ad_hoc_report** | **bool**| When set to true, if you haven&#39;t already used your monthly allocation of ad-hoc reports, generate an ad-hoc report for the given vendor, and return the vendor data. | [optional] 
 **start_monitoring** | **bool**| When set to true, if the vendor is not already being monitored, and if you are not already monitoring all the vendors your are licensed for, start monitoring the vendor, and return the vendor data. | [optional] 
 **labels** | [**list[str]**](str.md)| The labels to assign to the vendor if start monitoring set to true. If you want to update the labels for an already monitored vendor use the /vendor/labels endpoint. | [optional] 
 **tier** | **int**| The tier to assign to the vendor if start monitoring is set to true. | [optional] 
 **wait_for_scan** | **bool**| Flag indicating whether the request should wait for scan results on new unknown vendors | [optional] [default to false]

### Return type

[**Vendor**](Vendor.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_domain_details**
> GetDomainDetailsV1RespBody vendor_domain_details(vendor_primary_hostname, hostname)

Retrieve details for a domain

Returns the details for a domain. It will return 422 when requesting details of an inactive domain.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to show the domain detail for.
hostname = 'hostname_example' # str | The hostname for which to return the details, e.g. \"upguard.com\"

try:
    # Retrieve details for a domain
    api_response = api_instance.vendor_domain_details(vendor_primary_hostname, hostname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_domain_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to show the domain detail for. | 
 **hostname** | **str**| The hostname for which to return the details, e.g. \&quot;upguard.com\&quot; | 

### Return type

[**GetDomainDetailsV1RespBody**](GetDomainDetailsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_domain_update_labels**
> vendor_domain_update_labels(vendor_primary_hostname, hostname, labels)

Assign labels to an domain

Assign labels to a domain. To remove all labels pass an empty list.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to update the domain labels for.
hostname = 789 # int | The hostname to update labels for
labels = ['labels_example'] # list[str] | The labels to assign to the domain. You can pass an empty array to remove all labels.

try:
    # Assign labels to an domain
    api_instance.vendor_domain_update_labels(vendor_primary_hostname, hostname, labels)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_domain_update_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to update the domain labels for. | 
 **hostname** | **int**| The hostname to update labels for | 
 **labels** | [**list[str]**](str.md)| The labels to assign to the domain. You can pass an empty array to remove all labels. | 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_domains**
> GetDomainsV1RespBody vendor_domains(vendor_primary_hostname, active=active, inactive=inactive, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

List vendor domains

Returns a list of domains for a vendor.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to show domains for.
active = true # bool | Retrieve active domains (optional) (default to true)
inactive = true # bool | Retrieve inactive domains (optional) (default to true)
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'domain' # str | The value to sort the domains by  If not specified will default to `domain` and set `sort_desc` to `true` (optional) (default to domain)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # List vendor domains
    api_response = api_instance.vendor_domains(vendor_primary_hostname, active=active, inactive=inactive, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to show domains for. | 
 **active** | **bool**| Retrieve active domains | [optional] [default to true]
 **inactive** | **bool**| Retrieve inactive domains | [optional] [default to true]
 **labels** | [**list[str]**](str.md)| Filter result by the provided labels | [optional] 
 **page_token** | **str**| The &#x60;page_token&#x60; from a previous request, use this to get the next page of results. | [optional] 
 **page_size** | **int**| The number of results to return per page. | [optional] [default to 1000]
 **sort_by** | **str**| The value to sort the domains by  If not specified will default to &#x60;domain&#x60; and set &#x60;sort_desc&#x60; to &#x60;true&#x60; | [optional] [default to domain]
 **sort_desc** | **bool**| Whether or not to sort the results in descending order | [optional] [default to false]

### Return type

[**GetDomainsV1RespBody**](GetDomainsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_ip_details**
> GetIpDetailsV1RespBody vendor_ip_details(vendor_primary_hostname, ip)

Retrieve details for an IP address

Returns the details of the IP address. It will return 422 when requesting details of an inactive IP address.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to show the IP detail for.
ip = 'ip_example' # str | The IP address to get details for

try:
    # Retrieve details for an IP address
    api_response = api_instance.vendor_ip_details(vendor_primary_hostname, ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_ip_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to show the IP detail for. | 
 **ip** | **str**| The IP address to get details for | 

### Return type

[**GetIpDetailsV1RespBody**](GetIpDetailsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_ip_update_labels**
> vendor_ip_update_labels(vendor_primary_hostname, ip, labels)

Assign labels to an IP

Assign labels to an IP. To remove all labels pass an empty list.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to update the IP labels for.
ip = 789 # int | The IP to update labels for
labels = ['labels_example'] # list[str] | The labels to assign to the IP. You can pass an empty array to remove all labels.

try:
    # Assign labels to an IP
    api_instance.vendor_ip_update_labels(vendor_primary_hostname, ip, labels)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_ip_update_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to update the IP labels for. | 
 **ip** | **int**| The IP to update labels for | 
 **labels** | [**list[str]**](str.md)| The labels to assign to the IP. You can pass an empty array to remove all labels. | 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_ips**
> GetIPsV1RespBody vendor_ips(vendor_primary_hostname, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

List vendor ips

Returns a list of ips for a vendor.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to show ips for.
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'ip' # str | The value to sort the IPs by  If not specified will default to `ip` and set `sort_desc` to `true` (optional) (default to ip)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # List vendor ips
    api_response = api_instance.vendor_ips(vendor_primary_hostname, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to show ips for. | 
 **labels** | [**list[str]**](str.md)| Filter result by the provided labels | [optional] 
 **page_token** | **str**| The &#x60;page_token&#x60; from a previous request, use this to get the next page of results. | [optional] 
 **page_size** | **int**| The number of results to return per page. | [optional] [default to 1000]
 **sort_by** | **str**| The value to sort the IPs by  If not specified will default to &#x60;ip&#x60; and set &#x60;sort_desc&#x60; to &#x60;true&#x60; | [optional] [default to ip]
 **sort_desc** | **bool**| Whether or not to sort the results in descending order | [optional] [default to false]

### Return type

[**GetIPsV1RespBody**](GetIPsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_ranges**
> GetRangesV1RespBody vendor_ranges(vendor_primary_hostname, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

List vendor ip ranges

Returns a list of ip ranges for a vendor.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to show ips for.
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'num_ips' # str | The value to sort the IP ranges by  If not specified will default to `num_ips` and set `sort_desc` to `true` (optional) (default to num_ips)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # List vendor ip ranges
    api_response = api_instance.vendor_ranges(vendor_primary_hostname, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to show ips for. | 
 **labels** | [**list[str]**](str.md)| Filter result by the provided labels | [optional] 
 **page_token** | **str**| The &#x60;page_token&#x60; from a previous request, use this to get the next page of results. | [optional] 
 **page_size** | **int**| The number of results to return per page. | [optional] [default to 1000]
 **sort_by** | **str**| The value to sort the IP ranges by  If not specified will default to &#x60;num_ips&#x60; and set &#x60;sort_desc&#x60; to &#x60;true&#x60; | [optional] [default to num_ips]
 **sort_desc** | **bool**| Whether or not to sort the results in descending order | [optional] [default to false]

### Return type

[**GetRangesV1RespBody**](GetRangesV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_update_attributes**
> vendor_update_attributes(update_vendor_attributes_v1_request_body=update_vendor_attributes_v1_request_body)

Assign or update the attributes for a vendor

Assign or update the attributes for a vendor. To remove an attribute use null as its value in the payload.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
update_vendor_attributes_v1_request_body = upguard.UpdateVendorAttributesV1RequestBody() # UpdateVendorAttributesV1RequestBody |  (optional)

try:
    # Assign or update the attributes for a vendor
    api_instance.vendor_update_attributes(update_vendor_attributes_v1_request_body=update_vendor_attributes_v1_request_body)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_update_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_vendor_attributes_v1_request_body** | [**UpdateVendorAttributesV1RequestBody**](UpdateVendorAttributesV1RequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_update_labels**
> vendor_update_labels(vendor_primary_hostname, labels)

Assign labels to a vendor

Assign labels to a vendor. To remove all labels pass an empty list.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to update labels for.
labels = ['labels_example'] # list[str] | The labels to assign to the vendor. You can pass an empty array to remove all labels.

try:
    # Assign labels to a vendor
    api_instance.vendor_update_labels(vendor_primary_hostname, labels)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_update_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to update labels for. | 
 **labels** | [**list[str]**](str.md)| The labels to assign to the vendor. You can pass an empty array to remove all labels. | 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_update_tier**
> vendor_update_tier(vendor_primary_hostname, tier)

Assign tier to a vendor

Assign tier to a vendor. To remove a tier pass a value of zero.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname of the vendor to update tier for.
tier = 789 # int | The tier to assign to the vendor. You can pass a value of zero to remove a tier

try:
    # Assign tier to a vendor
    api_instance.vendor_update_tier(vendor_primary_hostname, tier)
except ApiException as e:
    print("Exception when calling VendorsApi->vendor_update_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname of the vendor to update tier for. | 
 **tier** | **int**| The tier to assign to the vendor. You can pass a value of zero to remove a tier | 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors**
> VendorsResponsePayloadBody vendors(include_ad_hoc_reports=include_ad_hoc_reports, page_token=page_token, page_size=page_size, labels=labels, include_risks=include_risks)

List monitored vendors

If the include_ad_hoc_reports parameter is set to true then vendors with ad hoc reports available will also be returned.

### Example
```python
from __future__ import print_function
import time
import upguard
from upguard.rest import ApiException
from pprint import pprint

# Configure API key authorization: API key in header
configuration = upguard.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = upguard.VendorsApi(upguard.ApiClient(configuration))
include_ad_hoc_reports = false # bool | Include vendors with an existing ad hoc report in the results. (optional) (default to false)
page_token = 'page_token_example' # str | The token of the page to be returned. Will return the first page if left blank. (optional)
page_size = 789 # int | The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. (optional)
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
include_risks = false # bool | Include risks (optional) (default to false)

try:
    # List monitored vendors
    api_response = api_instance.vendors(include_ad_hoc_reports=include_ad_hoc_reports, page_token=page_token, page_size=page_size, labels=labels, include_risks=include_risks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_ad_hoc_reports** | **bool**| Include vendors with an existing ad hoc report in the results. | [optional] [default to false]
 **page_token** | **str**| The token of the page to be returned. Will return the first page if left blank. | [optional] 
 **page_size** | **int**| The number of results to return per page. Valid values range from 10 to 2000. Defaults to 1000 if unset. | [optional] 
 **labels** | [**list[str]**](str.md)| Filter result by the provided labels | [optional] 
 **include_risks** | **bool**| Include risks | [optional] [default to false]

### Return type

[**VendorsResponsePayloadBody**](VendorsResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

