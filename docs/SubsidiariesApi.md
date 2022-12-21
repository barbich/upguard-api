# upguard.SubsidiariesApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subsidiaries**](SubsidiariesApi.md#subsidiaries) | **GET** /subsidiaries | Get a list of subsidiaries
[**subsidiary_domain_details**](SubsidiariesApi.md#subsidiary_domain_details) | **GET** /subsidiary/domain | Retrieve details for a domain
[**subsidiary_domain_update_labels**](SubsidiariesApi.md#subsidiary_domain_update_labels) | **PUT** /subsidiary/domain/labels | Assign labels to an domain
[**subsidiary_domains**](SubsidiariesApi.md#subsidiary_domains) | **GET** /subsidiary/domains | List subsidiary domains
[**subsidiary_ip_details**](SubsidiariesApi.md#subsidiary_ip_details) | **GET** /subsidiary/ip | Retrieve details for an IP address
[**subsidiary_ip_update_labels**](SubsidiariesApi.md#subsidiary_ip_update_labels) | **PUT** /subsidiary/ip/labels | Assign labels to an IP
[**subsidiary_ips**](SubsidiariesApi.md#subsidiary_ips) | **GET** /subsidiary/ips | List subdiary ips
[**subsidiary_ranges**](SubsidiariesApi.md#subsidiary_ranges) | **GET** /subsidiary/ranges | List subsidiary ip ranges


# **subsidiaries**
> GetSubsidiariesV1RespBody subsidiaries()

Get a list of subsidiaries

Returns a list of subsidiaries.

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
api_instance = upguard.SubsidiariesApi(upguard.ApiClient(configuration))

try:
    # Get a list of subsidiaries
    api_response = api_instance.subsidiaries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidiariesApi->subsidiaries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSubsidiariesV1RespBody**](GetSubsidiariesV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subsidiary_domain_details**
> GetDomainDetailsV1RespBody subsidiary_domain_details(subsidiary_primary_hostname, hostname)

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
api_instance = upguard.SubsidiariesApi(upguard.ApiClient(configuration))
subsidiary_primary_hostname = 'subsidiary_primary_hostname_example' # str | The primary hostname of the subsidiary to show the domain detail for.
hostname = 'hostname_example' # str | The hostname for which to return the details, e.g. \"upguard.com\"

try:
    # Retrieve details for a domain
    api_response = api_instance.subsidiary_domain_details(subsidiary_primary_hostname, hostname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidiariesApi->subsidiary_domain_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsidiary_primary_hostname** | **str**| The primary hostname of the subsidiary to show the domain detail for. | 
 **hostname** | **str**| The hostname for which to return the details, e.g. \&quot;upguard.com\&quot; | 

### Return type

[**GetDomainDetailsV1RespBody**](GetDomainDetailsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subsidiary_domain_update_labels**
> subsidiary_domain_update_labels(subsidiary_primary_hostname, hostname, labels)

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
api_instance = upguard.SubsidiariesApi(upguard.ApiClient(configuration))
subsidiary_primary_hostname = 'subsidiary_primary_hostname_example' # str | The primary hostname of the subsidiary to update the domain labels for.
hostname = 789 # int | The hostname to update labels for
labels = ['labels_example'] # list[str] | The labels to assign to the domain. You can pass an empty array to remove all labels.

try:
    # Assign labels to an domain
    api_instance.subsidiary_domain_update_labels(subsidiary_primary_hostname, hostname, labels)
except ApiException as e:
    print("Exception when calling SubsidiariesApi->subsidiary_domain_update_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsidiary_primary_hostname** | **str**| The primary hostname of the subsidiary to update the domain labels for. | 
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

# **subsidiary_domains**
> GetDomainsV1RespBody subsidiary_domains(subsidiary_primary_hostname, active=active, inactive=inactive, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

List subsidiary domains

Returns a list of domains for a subsidiary.

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
api_instance = upguard.SubsidiariesApi(upguard.ApiClient(configuration))
subsidiary_primary_hostname = 'subsidiary_primary_hostname_example' # str | The primary hostname of the subsidiary to show domains for.
active = true # bool | Retrieve active domains (optional) (default to true)
inactive = true # bool | Retrieve inactive domains (optional) (default to true)
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'domain' # str | The value to sort the domains by  If not specified will default to `domain` and set `sort_desc` to `true` (optional) (default to domain)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # List subsidiary domains
    api_response = api_instance.subsidiary_domains(subsidiary_primary_hostname, active=active, inactive=inactive, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidiariesApi->subsidiary_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsidiary_primary_hostname** | **str**| The primary hostname of the subsidiary to show domains for. | 
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

# **subsidiary_ip_details**
> GetIpDetailsV1RespBody subsidiary_ip_details(subsidiary_primary_hostname, ip)

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
api_instance = upguard.SubsidiariesApi(upguard.ApiClient(configuration))
subsidiary_primary_hostname = 'subsidiary_primary_hostname_example' # str | The primary hostname of the subsidiary to show the IP detail for.
ip = 'ip_example' # str | The IP address to get details for

try:
    # Retrieve details for an IP address
    api_response = api_instance.subsidiary_ip_details(subsidiary_primary_hostname, ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidiariesApi->subsidiary_ip_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsidiary_primary_hostname** | **str**| The primary hostname of the subsidiary to show the IP detail for. | 
 **ip** | **str**| The IP address to get details for | 

### Return type

[**GetIpDetailsV1RespBody**](GetIpDetailsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subsidiary_ip_update_labels**
> subsidiary_ip_update_labels(subsidiary_primary_hostname, ip, labels)

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
api_instance = upguard.SubsidiariesApi(upguard.ApiClient(configuration))
subsidiary_primary_hostname = 'subsidiary_primary_hostname_example' # str | The primary hostname of the subsidiary to update the IP labels for.
ip = 789 # int | The IP to update labels for
labels = ['labels_example'] # list[str] | The labels to assign to the IP. You can pass an empty array to remove all labels.

try:
    # Assign labels to an IP
    api_instance.subsidiary_ip_update_labels(subsidiary_primary_hostname, ip, labels)
except ApiException as e:
    print("Exception when calling SubsidiariesApi->subsidiary_ip_update_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsidiary_primary_hostname** | **str**| The primary hostname of the subsidiary to update the IP labels for. | 
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

# **subsidiary_ips**
> GetIPsV1RespBody subsidiary_ips(subsidiary_primary_hostname, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

List subdiary ips

Returns a list of ips for a subsidiary.

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
api_instance = upguard.SubsidiariesApi(upguard.ApiClient(configuration))
subsidiary_primary_hostname = 'subsidiary_primary_hostname_example' # str | The primary hostname of the subsidiary to show ips for.
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'ip' # str | The value to sort the IPs by  If not specified will default to `ip` and set `sort_desc` to `true` (optional) (default to ip)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # List subdiary ips
    api_response = api_instance.subsidiary_ips(subsidiary_primary_hostname, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidiariesApi->subsidiary_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsidiary_primary_hostname** | **str**| The primary hostname of the subsidiary to show ips for. | 
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

# **subsidiary_ranges**
> GetRangesV1RespBody subsidiary_ranges(subsidiary_primary_hostname, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

List subsidiary ip ranges

Returns a list of ip ranges for a subsidiary.

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
api_instance = upguard.SubsidiariesApi(upguard.ApiClient(configuration))
subsidiary_primary_hostname = 'subsidiary_primary_hostname_example' # str | The primary hostname of the subsidiary to show ranges for.
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'num_ips' # str | The value to sort the IP ranges by  If not specified will default to `num_ips` and set `sort_desc` to `true` (optional) (default to num_ips)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # List subsidiary ip ranges
    api_response = api_instance.subsidiary_ranges(subsidiary_primary_hostname, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubsidiariesApi->subsidiary_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsidiary_primary_hostname** | **str**| The primary hostname of the subsidiary to show ranges for. | 
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

