# upguard.BreachesApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**breached_identities**](BreachesApi.md#breached_identities) | **GET** /breaches | Get a list of breached identities
[**identity_breach**](BreachesApi.md#identity_breach) | **GET** /breach | Get the details for an identity breach


# **breached_identities**
> BreachedIdentitiesResponsePayloadBody breached_identities(page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc, breach_id=breach_id)

Get a list of breached identities

Returns a list of identities ordered by last breached date.

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
api_instance = upguard.BreachesApi(upguard.ApiClient(configuration))
page_token = 'page_token_example' # str | The `page_token` from a previous request, use this to get the next page of results. (optional)
page_size = 1000 # int | The number of results to return per page. (optional) (default to 1000)
sort_by = 'date_last_breach' # str | The value to sort the breached identities by  If not specified will default to `date_last_breach` and set `sort_desc` to `true` (optional) (default to date_last_breach)
sort_desc = false # bool | Whether or not to sort the results in descending order (optional) (default to false)
breach_id = 'breach_id_example' # str | The breach ID to filter on (optional)

try:
    # Get a list of breached identities
    api_response = api_instance.breached_identities(page_token=page_token, page_size=page_size, sort_by=sort_by, sort_desc=sort_desc, breach_id=breach_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BreachesApi->breached_identities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_token** | **str**| The &#x60;page_token&#x60; from a previous request, use this to get the next page of results. | [optional] 
 **page_size** | **int**| The number of results to return per page. | [optional] [default to 1000]
 **sort_by** | **str**| The value to sort the breached identities by  If not specified will default to &#x60;date_last_breach&#x60; and set &#x60;sort_desc&#x60; to &#x60;true&#x60; | [optional] [default to date_last_breach]
 **sort_desc** | **bool**| Whether or not to sort the results in descending order | [optional] [default to false]
 **breach_id** | **str**| The breach ID to filter on | [optional] 

### Return type

[**BreachedIdentitiesResponsePayloadBody**](BreachedIdentitiesResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identity_breach**
> IdentityBreachResponsePayloadBody identity_breach(id=id)

Get the details for an identity breach

Returns the details of an identity breach.

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
api_instance = upguard.BreachesApi(upguard.ApiClient(configuration))
id = 'id_example' # str | The ID of the breach to fetch (optional)

try:
    # Get the details for an identity breach
    api_response = api_instance.identity_breach(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BreachesApi->identity_breach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the breach to fetch | [optional] 

### Return type

[**IdentityBreachResponsePayloadBody**](IdentityBreachResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

