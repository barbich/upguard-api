# upguard.TyposquatApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_typosquat_domains**](TyposquatApi.md#list_typosquat_domains) | **GET** /typosquat | List typosquat domains
[**typosquat_details**](TyposquatApi.md#typosquat_details) | **GET** /typosquat/details | Retrieve typosquat details for a domain.


# **list_typosquat_domains**
> GetTyposquatResponsePayloadBody list_typosquat_domains()

List typosquat domains

Returns the list of enabled typosquatting domains.

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
api_instance = upguard.TyposquatApi(upguard.ApiClient(configuration))

try:
    # List typosquat domains
    api_response = api_instance.list_typosquat_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TyposquatApi->list_typosquat_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTyposquatResponsePayloadBody**](GetTyposquatResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **typosquat_details**
> GetTyposquatDetailsResponsePayloadBody typosquat_details(domain)

Retrieve typosquat details for a domain.

If the requested domain is not enabled a 404 will be returned. Use the /typosquat to retrieve the list of enabled domains first.

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
api_instance = upguard.TyposquatApi(upguard.ApiClient(configuration))
domain = 'domain_example' # str | The domain for which to return typosquat details. e.g. \"upguard.com\"

try:
    # Retrieve typosquat details for a domain.
    api_response = api_instance.typosquat_details(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TyposquatApi->typosquat_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| The domain for which to return typosquat details. e.g. \&quot;upguard.com\&quot; | 

### Return type

[**GetTyposquatDetailsResponsePayloadBody**](GetTyposquatDetailsResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

