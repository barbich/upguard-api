# upguard.OrganisationApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organisation_v1**](OrganisationApi.md#get_organisation_v1) | **GET** /organisation | Get the current organisation


# **get_organisation_v1**
> GetOrganisationV1RespBody get_organisation_v1()

Get the current organisation

Returns the information of the organisation associated with the API key used for the request.

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
api_instance = upguard.OrganisationApi(upguard.ApiClient(configuration))

try:
    # Get the current organisation
    api_response = api_instance.get_organisation_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationApi->get_organisation_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetOrganisationV1RespBody**](GetOrganisationV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

