# upguard.LabelsApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**labels**](LabelsApi.md#labels) | **GET** /labels | Get the list of registered labels


# **labels**
> GetLabelsV1RespBody labels()

Get the list of registered labels

Returns the list of labels for your account.

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
api_instance = upguard.LabelsApi(upguard.ApiClient(configuration))

try:
    # Get the list of registered labels
    api_response = api_instance.labels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->labels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLabelsV1RespBody**](GetLabelsV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

