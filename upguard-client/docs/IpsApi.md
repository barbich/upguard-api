# upguard.IpsApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_ips**](IpsApi.md#add_custom_ips) | **PUT** /ips | Add custom ips
[**ip_details**](IpsApi.md#ip_details) | **GET** /ip | Retrieve details for an IP address
[**ip_update_labels**](IpsApi.md#ip_update_labels) | **PUT** /ip/labels | Assign labels to an IP
[**ips**](IpsApi.md#ips) | **GET** /ips | Get a list of ips
[**ranges**](IpsApi.md#ranges) | **GET** /ranges | Get a list of ip ranges
[**remove_custom_ips**](IpsApi.md#remove_custom_ips) | **DELETE** /ips | Remove custom ips


# **add_custom_ips**
> add_custom_ips(ips, labels=labels)

Add custom ips

Add a list of custom ips to your account.

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
api_instance = upguard.IpsApi(upguard.ApiClient(configuration))
ips = ['ips_example'] # list[str] | The list of ips to add
labels = ['labels_example'] # list[str] | The labels to assign to the ips when added. (optional)

try:
    # Add custom ips
    api_instance.add_custom_ips(ips, labels=labels)
except ApiException as e:
    print("Exception when calling IpsApi->add_custom_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ips** | [**list[str]**](str.md)| The list of ips to add | 
 **labels** | [**list[str]**](str.md)| The labels to assign to the ips when added. | [optional] 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_details**
> GetIpDetailsV1RespBody ip_details(ip)

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
api_instance = upguard.IpsApi(upguard.ApiClient(configuration))
ip = 'ip_example' # str | The IP address to get details for

try:
    # Retrieve details for an IP address
    api_response = api_instance.ip_details(ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpsApi->ip_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| The IP address to get details for | 

### Return type

[**GetIpDetailsV1RespBody**](GetIpDetailsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_update_labels**
> ip_update_labels(ip, labels)

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
api_instance = upguard.IpsApi(upguard.ApiClient(configuration))
ip = 789 # int | The IP to update labels for
labels = ['labels_example'] # list[str] | The labels to assign to the IP. You can pass an empty array to remove all labels.

try:
    # Assign labels to an IP
    api_instance.ip_update_labels(ip, labels)
except ApiException as e:
    print("Exception when calling IpsApi->ip_update_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **ips**
> GetIPsV1RespBody ips(labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

Get a list of ips

Returns a list of ips for your account.

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
api_instance = upguard.IpsApi(upguard.ApiClient(configuration))
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'ip' # str | The value to sort the IPs by  If not specified will default to `ip` and set `sort_desc` to `true` (optional) (default to ip)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # Get a list of ips
    api_response = api_instance.ips(labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpsApi->ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **ranges**
> GetRangesV1RespBody ranges(labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

Get a list of ip ranges

Returns a list of ip ranges for your account.

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
api_instance = upguard.IpsApi(upguard.ApiClient(configuration))
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'num_ips' # str | The value to sort the IP ranges by  If not specified will default to `num_ips` and set `sort_desc` to `true` (optional) (default to num_ips)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # Get a list of ip ranges
    api_response = api_instance.ranges(labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpsApi->ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **remove_custom_ips**
> remove_custom_ips(ips=ips, labels=labels)

Remove custom ips

Remove custom ips from your account.

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
api_instance = upguard.IpsApi(upguard.ApiClient(configuration))
ips = ['ips_example'] # list[str] | A comma separated list of ips to remove. Only ips or labels can be specified not both (optional)
labels = ['labels_example'] # list[str] | A list of labels whose domains will be removed. All custom IPs with at least one of the provided labels will be removed. Only ips or labels can be specified not both (optional)

try:
    # Remove custom ips
    api_instance.remove_custom_ips(ips=ips, labels=labels)
except ApiException as e:
    print("Exception when calling IpsApi->remove_custom_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ips** | [**list[str]**](str.md)| A comma separated list of ips to remove. Only ips or labels can be specified not both | [optional] 
 **labels** | [**list[str]**](str.md)| A list of labels whose domains will be removed. All custom IPs with at least one of the provided labels will be removed. Only ips or labels can be specified not both | [optional] 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

