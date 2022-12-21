# upguard.DomainsApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_domains**](DomainsApi.md#add_custom_domains) | **PUT** /domains | Add custom domains
[**domain_details**](DomainsApi.md#domain_details) | **GET** /domain | Retrieve details for a domain
[**domain_update_labels**](DomainsApi.md#domain_update_labels) | **PUT** /domain/labels | Assign labels to a domain
[**domains**](DomainsApi.md#domains) | **GET** /domains | Get a list of domains
[**remove_custom_domains**](DomainsApi.md#remove_custom_domains) | **DELETE** /domains | Remove custom domains


# **add_custom_domains**
> add_custom_domains(hostnames, labels=labels)

Add custom domains

Add a list of custom domains to your account.

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
api_instance = upguard.DomainsApi(upguard.ApiClient(configuration))
hostnames = ['hostnames_example'] # list[str] | A comma separated list of hostnames to add
labels = ['labels_example'] # list[str] | The labels to add to the hostnames (optional)

try:
    # Add custom domains
    api_instance.add_custom_domains(hostnames, labels=labels)
except ApiException as e:
    print("Exception when calling DomainsApi->add_custom_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostnames** | [**list[str]**](str.md)| A comma separated list of hostnames to add | 
 **labels** | [**list[str]**](str.md)| The labels to add to the hostnames | [optional] 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_details**
> GetDomainDetailsV1RespBody domain_details(hostname)

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
api_instance = upguard.DomainsApi(upguard.ApiClient(configuration))
hostname = 'hostname_example' # str | The hostname for which to return the details, e.g. \"upguard.com\"

try:
    # Retrieve details for a domain
    api_response = api_instance.domain_details(hostname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domain_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| The hostname for which to return the details, e.g. \&quot;upguard.com\&quot; | 

### Return type

[**GetDomainDetailsV1RespBody**](GetDomainDetailsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_update_labels**
> domain_update_labels(hostname, labels)

Assign labels to a domain

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
api_instance = upguard.DomainsApi(upguard.ApiClient(configuration))
hostname = 'hostname_example' # str | The hostname to update labels for
labels = ['labels_example'] # list[str] | The labels to assign to the domain. You can pass an empty array to remove all labels.

try:
    # Assign labels to a domain
    api_instance.domain_update_labels(hostname, labels)
except ApiException as e:
    print("Exception when calling DomainsApi->domain_update_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostname** | **str**| The hostname to update labels for | 
 **labels** | [**list[str]**](str.md)| The labels to assign to the domain. You can pass an empty array to remove all labels. | 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domains**
> GetDomainsV1RespBody domains(active=active, inactive=inactive, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)

Get a list of domains

Returns a list of domains for your account.

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
api_instance = upguard.DomainsApi(upguard.ApiClient(configuration))
active = true # bool | Retrieve active domains (optional) (default to true)
inactive = true # bool | Retrieve inactive domains (optional) (default to true)
labels = ['labels_example'] # list[str] | Filter result by the provided labels (optional)
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'domain' # str | The value to sort the domains by  If not specified will default to `domain` and set `sort_desc` to `true` (optional) (default to domain)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)

try:
    # Get a list of domains
    api_response = api_instance.domains(active=active, inactive=inactive, labels=labels, page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **remove_custom_domains**
> remove_custom_domains(hostnames=hostnames, labels=labels)

Remove custom domains

Remove custom domains from your account.

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
api_instance = upguard.DomainsApi(upguard.ApiClient(configuration))
hostnames = ['hostnames_example'] # list[str] | A comma separated list of hostnames to remove. Only hostnames or labels can be specified not both (optional)
labels = ['labels_example'] # list[str] | A list of labels whose hostnames will be removed. All custom domains with at least one of the provided labels will be removed. Only hostnames or labels can be specified not both (optional)

try:
    # Remove custom domains
    api_instance.remove_custom_domains(hostnames=hostnames, labels=labels)
except ApiException as e:
    print("Exception when calling DomainsApi->remove_custom_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hostnames** | [**list[str]**](str.md)| A comma separated list of hostnames to remove. Only hostnames or labels can be specified not both | [optional] 
 **labels** | [**list[str]**](str.md)| A list of labels whose hostnames will be removed. All custom domains with at least one of the provided labels will be removed. Only hostnames or labels can be specified not both | [optional] 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

