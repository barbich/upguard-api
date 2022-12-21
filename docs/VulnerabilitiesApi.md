# upguard.VulnerabilitiesApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**org_vulnerabilities**](VulnerabilitiesApi.md#org_vulnerabilities) | **GET** /vulnerabilities | List potential vulnerabilities of your domains &amp; IPs
[**vendor_vulnerabilities**](VulnerabilitiesApi.md#vendor_vulnerabilities) | **GET** /vulnerabilities/vendor | List potential vulnerabilities of a vendor


# **org_vulnerabilities**
> GetOrgVulnerabilitiesV1RespBody org_vulnerabilities(labels=labels, page_token=page_token, page_size=page_size)

List potential vulnerabilities of your domains & IPs

Returns a list of potential vulnerabilities that have been detected for your account.

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
api_instance = upguard.VulnerabilitiesApi(upguard.ApiClient(configuration))
labels = ['labels_example'] # list[str] | A case-insensitive comma separated list of website labels to filter results by (optional)
page_token = 'page_token_example' # str | The `next_page_token` from a previous response, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)

try:
    # List potential vulnerabilities of your domains & IPs
    api_response = api_instance.org_vulnerabilities(labels=labels, page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VulnerabilitiesApi->org_vulnerabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **labels** | [**list[str]**](str.md)| A case-insensitive comma separated list of website labels to filter results by | [optional] 
 **page_token** | **str**| The &#x60;next_page_token&#x60; from a previous response, use this to get the next page of results. | [optional] 
 **page_size** | **int**| The number of results to return per page. | [optional] [default to 1000]

### Return type

[**GetOrgVulnerabilitiesV1RespBody**](GetOrgVulnerabilitiesV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_vulnerabilities**
> GetVendorVulnerabilitiesV1RespBody vendor_vulnerabilities(primary_hostname)

List potential vulnerabilities of a vendor

Returns a list of potential vulnerabilities that have been detected for a particular vendor.

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
api_instance = upguard.VulnerabilitiesApi(upguard.ApiClient(configuration))
primary_hostname = 'primary_hostname_example' # str | The primary hostname of the vendor to return vulnerabilities for

try:
    # List potential vulnerabilities of a vendor
    api_response = api_instance.vendor_vulnerabilities(primary_hostname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VulnerabilitiesApi->vendor_vulnerabilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_hostname** | **str**| The primary hostname of the vendor to return vulnerabilities for | 

### Return type

[**GetVendorVulnerabilitiesV1RespBody**](GetVendorVulnerabilitiesV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

