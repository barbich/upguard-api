# upguard.DataleaksApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataleaks_disclosures**](DataleaksApi.md#dataleaks_disclosures) | **GET** /dataleaks/disclosures | Get a list of disclosures
[**dataleaks_disclosures_update_status**](DataleaksApi.md#dataleaks_disclosures_update_status) | **PUT** /dataleaks/disclosures/status | Update the status of a disclosure


# **dataleaks_disclosures**
> DataLeaksDisclosuresResponsePayloadBody dataleaks_disclosures(min_time=min_time, max_time=max_time, statuses=statuses, ids=ids)

Get a list of disclosures

Returns a list of the disclosures in your account matching the given filters.  Required API key permissions: `DataLeaks` (select when creating API key in Account Settings)

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
api_instance = upguard.DataleaksApi(upguard.ApiClient(configuration))
min_time = '2013-10-20T19:20:30+01:00' # datetime | The minimum (non-inclusive) timestamp of a disclosure (RFC 3339 format). (optional)
max_time = '2013-10-20T19:20:30+01:00' # datetime | The maximum (non-inclusive) timestamp of a disclosure (RFC 3339 format). (optional)
statuses = 'statuses_example' # str | A comma-delimited list of statuses that disclosures should match. (optional)
ids = 'ids_example' # str | A comma-delimited list of IDs that disclosures should match. (optional)

try:
    # Get a list of disclosures
    api_response = api_instance.dataleaks_disclosures(min_time=min_time, max_time=max_time, statuses=statuses, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataleaksApi->dataleaks_disclosures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_time** | **datetime**| The minimum (non-inclusive) timestamp of a disclosure (RFC 3339 format). | [optional] 
 **max_time** | **datetime**| The maximum (non-inclusive) timestamp of a disclosure (RFC 3339 format). | [optional] 
 **statuses** | **str**| A comma-delimited list of statuses that disclosures should match. | [optional] 
 **ids** | **str**| A comma-delimited list of IDs that disclosures should match. | [optional] 

### Return type

[**DataLeaksDisclosuresResponsePayloadBody**](DataLeaksDisclosuresResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dataleaks_disclosures_update_status**
> dataleaks_disclosures_update_status(disclosure_id, new_status, user_email=user_email, comment=comment)

Update the status of a disclosure

Required API key permissions: `DataLeaks` (select when creating API key in Account Settings)

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
api_instance = upguard.DataleaksApi(upguard.ApiClient(configuration))
disclosure_id = 789 # int | The ID of the disclosure
new_status = 'new_status_example' # str | The new status for the disclosure
user_email = 'user_email_example' # str | The email address of the user changing the status (must have a Cyber Risk account with the \"Data Leaks\" role). (optional)
comment = 'comment_example' # str | A comment to accompany the status change, if required (optional)

try:
    # Update the status of a disclosure
    api_instance.dataleaks_disclosures_update_status(disclosure_id, new_status, user_email=user_email, comment=comment)
except ApiException as e:
    print("Exception when calling DataleaksApi->dataleaks_disclosures_update_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disclosure_id** | **int**| The ID of the disclosure | 
 **new_status** | **str**| The new status for the disclosure | 
 **user_email** | **str**| The email address of the user changing the status (must have a Cyber Risk account with the \&quot;Data Leaks\&quot; role). | [optional] 
 **comment** | **str**| A comment to accompany the status change, if required | [optional] 

### Return type

void (empty response body)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

