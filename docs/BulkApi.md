# upguard.BulkApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_deregister_hostnames**](BulkApi.md#bulk_deregister_hostnames) | **DELETE** /bulk/hostnames | Deregister a list of hostnames
[**bulk_get_hostname_details**](BulkApi.md#bulk_get_hostname_details) | **GET** /bulk/hostnames/{hostname} | Get the details for a hostname
[**bulk_get_hostnames_stats**](BulkApi.md#bulk_get_hostnames_stats) | **GET** /bulk/hostnames/stats | Get statistics around registered bulk hostnames
[**bulk_hostname_put_labels**](BulkApi.md#bulk_hostname_put_labels) | **PUT** /bulk/hostnames/{hostname}/labels | Assign new labels to a hostname
[**bulk_list_hostnames**](BulkApi.md#bulk_list_hostnames) | **GET** /bulk/hostnames | List hostnames and their risks
[**bulk_register_hostnames**](BulkApi.md#bulk_register_hostnames) | **POST** /bulk/hostnames | Register a list of hostnames to be scanned for risks


# **bulk_deregister_hostnames**
> BulkDeregisterHostnamesV1ResponseBody bulk_deregister_hostnames(bulk_deregister_hostnames_v1_request_body=bulk_deregister_hostnames_v1_request_body)

Deregister a list of hostnames

Deregister a list of hostnames. The provided hostnames must be fully qualified domain names or IPv4 addresses. Currently, a maximum of 1000 hostnames in a single request is supported.

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
api_instance = upguard.BulkApi(upguard.ApiClient(configuration))
bulk_deregister_hostnames_v1_request_body = upguard.BulkDeregisterHostnamesV1RequestBody() # BulkDeregisterHostnamesV1RequestBody |  (optional)

try:
    # Deregister a list of hostnames
    api_response = api_instance.bulk_deregister_hostnames(bulk_deregister_hostnames_v1_request_body=bulk_deregister_hostnames_v1_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkApi->bulk_deregister_hostnames: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_deregister_hostnames_v1_request_body** | [**BulkDeregisterHostnamesV1RequestBody**](BulkDeregisterHostnamesV1RequestBody.md)|  | [optional] 

### Return type

[**BulkDeregisterHostnamesV1ResponseBody**](BulkDeregisterHostnamesV1ResponseBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_get_hostname_details**
> BulkHostname bulk_get_hostname_details(hostname, omit_scan_info=omit_scan_info, omit_vendor=omit_vendor, omit_labels=omit_labels)

Get the details for a hostname

Get the details for a hostname. The provided hostname must be a fully qualified domain name or an IPv4 address.

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
api_instance = upguard.BulkApi(upguard.ApiClient(configuration))
hostname = 'hostname_example' # str | The hostname to fetch details for. It must be a fully qualified domain name or an IPv4 address.
omit_scan_info = false # bool | Omit the scan information, i.e. risks, score and last scanned at. (optional) (default to false)
omit_vendor = false # bool | Omit the vendor information for a hostname in the response. (optional) (default to false)
omit_labels = false # bool | Omit the labels for a hostname in the response. (optional) (default to false)

try:
    # Get the details for a hostname
    api_response = api_instance.bulk_get_hostname_details(hostname, omit_scan_info=omit_scan_info, omit_vendor=omit_vendor, omit_labels=omit_labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkApi->bulk_get_hostname_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| The hostname to fetch details for. It must be a fully qualified domain name or an IPv4 address. | 
 **omit_scan_info** | **bool**| Omit the scan information, i.e. risks, score and last scanned at. | [optional] [default to false]
 **omit_vendor** | **bool**| Omit the vendor information for a hostname in the response. | [optional] [default to false]
 **omit_labels** | **bool**| Omit the labels for a hostname in the response. | [optional] [default to false]

### Return type

[**BulkHostname**](BulkHostname.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_get_hostnames_stats**
> BulkGetHostnamesStatsV1ResponseBody bulk_get_hostnames_stats()

Get statistics around registered bulk hostnames

Get statistics for the registered hostnames. This will return the number of registered hostnames, the number of remaining slots and the number of active and inactive hostnames

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
api_instance = upguard.BulkApi(upguard.ApiClient(configuration))

try:
    # Get statistics around registered bulk hostnames
    api_response = api_instance.bulk_get_hostnames_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkApi->bulk_get_hostnames_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BulkGetHostnamesStatsV1ResponseBody**](BulkGetHostnamesStatsV1ResponseBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_hostname_put_labels**
> bulk_hostname_put_labels(hostname, labels=labels)

Assign new labels to a hostname

Assign labels to a hostname replacing the existing ones if any. To remove all labels use an empty array in the request.

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
api_instance = upguard.BulkApi(upguard.ApiClient(configuration))
hostname = 'hostname_example' # str | The hostname to fetch details for. It must be a fully qualified domain name or an IPv4 address.
labels = [upguard.list[str]()] # list[str] | Labels list (optional)

try:
    # Assign new labels to a hostname
    api_instance.bulk_hostname_put_labels(hostname, labels=labels)
except ApiException as e:
    print("Exception when calling BulkApi->bulk_hostname_put_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| The hostname to fetch details for. It must be a fully qualified domain name or an IPv4 address. | 
 **labels** | **list[str]**| Labels list | [optional] 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_list_hostnames**
> BulkListHostnamesV1ResponseBody bulk_list_hostnames(page_token=page_token, page_size=page_size, sort_desc=sort_desc, omit_scan_info=omit_scan_info, omit_vendor=omit_vendor, omit_labels=omit_labels, exclude_active=exclude_active, exclude_inactive=exclude_inactive, labels=labels)

List hostnames and their risks

Get the list of registered hostnames and their risks. You can use the omit_risks, omit_vendor, omit_score and omit_labels query parameter to turn off these information from the response and quickly get a list of registered hostnames.

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
api_instance = upguard.BulkApi(upguard.ApiClient(configuration))
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 200 # int | The number of results to return per page. (optional) (default to 200)
sort_desc = false # bool | Whether to sort the results in descending order. (optional) (default to false)
omit_scan_info = false # bool | Omit the scan information, i.e. risks, score and last scanned at. (optional) (default to false)
omit_vendor = false # bool | Omit the vendor information for a hostname in the response. (optional) (default to false)
omit_labels = false # bool | Omit the labels for a hostname in the response. (optional) (default to false)
exclude_active = false # bool | Exclude active hostnames from the results. (optional) (default to false)
exclude_inactive = false # bool | Exclude inactive hostnames from the results. (optional) (default to false)
labels = ['false'] # list[str] | Filter results to only hostnames that have all the provided labels. (optional) (default to false)

try:
    # List hostnames and their risks
    api_response = api_instance.bulk_list_hostnames(page_token=page_token, page_size=page_size, sort_desc=sort_desc, omit_scan_info=omit_scan_info, omit_vendor=omit_vendor, omit_labels=omit_labels, exclude_active=exclude_active, exclude_inactive=exclude_inactive, labels=labels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkApi->bulk_list_hostnames: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**| The &#x60;page_token&#x60; from a previous request, use this to get the next page of results. | [optional] 
 **page_size** | **int**| The number of results to return per page. | [optional] [default to 200]
 **sort_desc** | **bool**| Whether to sort the results in descending order. | [optional] [default to false]
 **omit_scan_info** | **bool**| Omit the scan information, i.e. risks, score and last scanned at. | [optional] [default to false]
 **omit_vendor** | **bool**| Omit the vendor information for a hostname in the response. | [optional] [default to false]
 **omit_labels** | **bool**| Omit the labels for a hostname in the response. | [optional] [default to false]
 **exclude_active** | **bool**| Exclude active hostnames from the results. | [optional] [default to false]
 **exclude_inactive** | **bool**| Exclude inactive hostnames from the results. | [optional] [default to false]
 **labels** | [**list[str]**](str.md)| Filter results to only hostnames that have all the provided labels. | [optional] [default to false]

### Return type

[**BulkListHostnamesV1ResponseBody**](BulkListHostnamesV1ResponseBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_register_hostnames**
> BulkRegisterHostnamesV1ResponseBody bulk_register_hostnames(bulk_register_hostnames_v1_request_body=bulk_register_hostnames_v1_request_body)

Register a list of hostnames to be scanned for risks

Register a list of hostnames to be scanned for risks. The provided hostnames must be fully qualified domain names or IPv4 addresses. Currently, a maximum of 1000 hostnames in a single request is supported. This will always replace the labels of currently registered hostnames and if the request has empty labels they will all be removed.

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
api_instance = upguard.BulkApi(upguard.ApiClient(configuration))
bulk_register_hostnames_v1_request_body = upguard.BulkRegisterHostnamesV1RequestBody() # BulkRegisterHostnamesV1RequestBody |  (optional)

try:
    # Register a list of hostnames to be scanned for risks
    api_response = api_instance.bulk_register_hostnames(bulk_register_hostnames_v1_request_body=bulk_register_hostnames_v1_request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BulkApi->bulk_register_hostnames: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_register_hostnames_v1_request_body** | [**BulkRegisterHostnamesV1RequestBody**](BulkRegisterHostnamesV1RequestBody.md)|  | [optional] 

### Return type

[**BulkRegisterHostnamesV1ResponseBody**](BulkRegisterHostnamesV1ResponseBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

