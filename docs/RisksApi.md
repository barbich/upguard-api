# upguard.RisksApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**available_risks**](RisksApi.md#available_risks) | **GET** /available_risks | Get a list of available risks in the platform
[**available_risks_v2**](RisksApi.md#available_risks_v2) | **GET** /available_risks/v2 | Get a list of available risks in the platform
[**org_risks_diff**](RisksApi.md#org_risks_diff) | **GET** /risks/diff | Get a list of risk changes for your account
[**risk**](RisksApi.md#risk) | **GET** /available_risks/risk | Get details for a risk in the platform
[**risks**](RisksApi.md#risks) | **GET** /risks | Get a list of active risks for your account
[**vendor_questionnaire_risks**](RisksApi.md#vendor_questionnaire_risks) | **GET** /risks/vendors/questionnaires | Get a list of questionnaire risks for one or more watched vendors or a specific questionnaire
[**vendor_questionnaire_risks_v2**](RisksApi.md#vendor_questionnaire_risks_v2) | **GET** /risks/vendors/questionnaires/v2 | (V2) Get a list of questionnaire risks for one or more watched vendors or a specific questionnaire
[**vendor_risks**](RisksApi.md#vendor_risks) | **GET** /risks/vendors | Get a list of active risks for a vendor
[**vendor_risks_diff**](RisksApi.md#vendor_risks_diff) | **GET** /risks/vendors/diff | Get a list of risk changes for a vendor
[**vendors_risks_diff**](RisksApi.md#vendors_risks_diff) | **GET** /risks/vendors/diffs | Get a list of risk changes for monitored vendors


# **available_risks**
> AvailableRisk available_risks()

Get a list of available risks in the platform

Returns a list of available risks in the UpGuard platform with detailed info. Please note this version of the endpoint has been deprecated, and v2 should be used instead.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))

try:
    # Get a list of available risks in the platform
    api_response = api_instance.available_risks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->available_risks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailableRisk**](AvailableRisk.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **available_risks_v2**
> list[AvailableRiskV2] available_risks_v2()

Get a list of available risks in the platform

Returns a list of available risks in the UpGuard platform with detailed info.  Some risks in the platform are generic risks like \"exposed_service:*\". The values of some of the fields for these risks depends on the details of the risk, e.g. which particular service is exposed. As such these fields are omitted from the response.  To get the full details for a specific risk, e.g. \"exposed_service:FTP\", use the risk details endpoint which will return the full information for the particular service.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))

try:
    # Get a list of available risks in the platform
    api_response = api_instance.available_risks_v2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->available_risks_v2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AvailableRiskV2]**](AvailableRiskV2.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_risks_diff**
> RisksDiffResponsePayloadBody org_risks_diff(start_date, end_date=end_date)

Get a list of risk changes for your account

Returns a list of the risks introduced and risks resolved for domains or IPs between two dates.  Risks resolved are not computed for dates prior to 2018-11-01 00:00:00.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))
start_date = '2013-10-20T19:20:30+01:00' # datetime | The date to use as the starting point for determining risks introduced/resolved (RFC 3339 format).
end_date = '2013-10-20T19:20:30+01:00' # datetime | The date to use as the final state for determining risks introduced/resolved (RFC 3339 format). If not provided, the latest risks will be used. (optional)

try:
    # Get a list of risk changes for your account
    api_response = api_instance.org_risks_diff(start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->org_risks_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The date to use as the starting point for determining risks introduced/resolved (RFC 3339 format). | 
 **end_date** | **datetime**| The date to use as the final state for determining risks introduced/resolved (RFC 3339 format). If not provided, the latest risks will be used. | [optional] 

### Return type

[**RisksDiffResponsePayloadBody**](RisksDiffResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **risk**
> AvailableRiskV2 risk(risk_id)

Get details for a risk in the platform

Returns the details for a risk.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))
risk_id = 'risk_id_example' # str | ID of the risk to fetch details for

try:
    # Get details for a risk in the platform
    api_response = api_instance.risk(risk_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->risk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **risk_id** | **str**| ID of the risk to fetch details for | 

### Return type

[**AvailableRiskV2**](AvailableRiskV2.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **risks**
> GetRisksV1RespBody risks(min_severity=min_severity)

Get a list of active risks for your account

Returns a list of risks that have been detected for your account.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))
min_severity = 'info' # str | Minimum severity for the risks (optional) (default to info)

try:
    # Get a list of active risks for your account
    api_response = api_instance.risks(min_severity=min_severity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->risks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **min_severity** | **str**| Minimum severity for the risks | [optional] [default to info]

### Return type

[**GetRisksV1RespBody**](GetRisksV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_questionnaire_risks**
> QuestionnaireRisksResponsePayloadBody vendor_questionnaire_risks(vendor_id=vendor_id, primary_hostname=primary_hostname, questionnaire_id=questionnaire_id, page_token=page_token, page_size=page_size)

Get a list of questionnaire risks for one or more watched vendors or a specific questionnaire

Returns a list of currently open questionnaire risks for one or more of an account's watched vendors. Please note this version of the endpoint has been deprecated, and v2 should be used instead.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))
vendor_id = 789 # int | Restricts the questionnaire risks returned to a specific watched vendor by ID (optional)
primary_hostname = 'primary_hostname_example' # str | Restricts the questionnaire risks returned to a specific watched vendor by vendor primary hostname (optional)
questionnaire_id = 789 # int | Restricts the questionnaire risks returned to a specific questionnaire by ID (optional)
page_token = 'page_token_example' # str | The token of the page to be returned. Will return the first page if left blank. (optional)
page_size = 789 # int | The number of risks to return per page. This Integer between 10 and 2000 defaults to 1000 if not supplied. (optional)

try:
    # Get a list of questionnaire risks for one or more watched vendors or a specific questionnaire
    api_response = api_instance.vendor_questionnaire_risks(vendor_id=vendor_id, primary_hostname=primary_hostname, questionnaire_id=questionnaire_id, page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->vendor_questionnaire_risks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Restricts the questionnaire risks returned to a specific watched vendor by ID | [optional] 
 **primary_hostname** | **str**| Restricts the questionnaire risks returned to a specific watched vendor by vendor primary hostname | [optional] 
 **questionnaire_id** | **int**| Restricts the questionnaire risks returned to a specific questionnaire by ID | [optional] 
 **page_token** | **str**| The token of the page to be returned. Will return the first page if left blank. | [optional] 
 **page_size** | **int**| The number of risks to return per page. This Integer between 10 and 2000 defaults to 1000 if not supplied. | [optional] 

### Return type

[**QuestionnaireRisksResponsePayloadBody**](QuestionnaireRisksResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_questionnaire_risks_v2**
> QuestionnaireRisksResponsePayloadBodyV2 vendor_questionnaire_risks_v2(vendor_id=vendor_id, primary_hostname=primary_hostname, questionnaire_id=questionnaire_id, page_token=page_token, page_size=page_size, ignore_waived_risks=ignore_waived_risks)

(V2) Get a list of questionnaire risks for one or more watched vendors or a specific questionnaire

Returns a list of currently open questionnaire risks for one or more of an account's watched vendors, including information on whether waivers exist for each risk.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))
vendor_id = 789 # int | Restricts the questionnaire risks returned to a specific watched vendor by ID (optional)
primary_hostname = 'primary_hostname_example' # str | Restricts the questionnaire risks returned to a specific watched vendor by vendor primary hostname (optional)
questionnaire_id = 789 # int | Restricts the questionnaire risks returned to a specific questionnaire by ID (optional)
page_token = 'page_token_example' # str | The token of the page to be returned. Will return the first page if left blank. (optional)
page_size = 789 # int | The number of risks to return per page. This Integer between 10 and 2000 defaults to 1000 if not supplied. (optional)
ignore_waived_risks = true # bool | Indicates that waived risks should not be returned in the risk set (optional)

try:
    # (V2) Get a list of questionnaire risks for one or more watched vendors or a specific questionnaire
    api_response = api_instance.vendor_questionnaire_risks_v2(vendor_id=vendor_id, primary_hostname=primary_hostname, questionnaire_id=questionnaire_id, page_token=page_token, page_size=page_size, ignore_waived_risks=ignore_waived_risks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->vendor_questionnaire_risks_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_id** | **int**| Restricts the questionnaire risks returned to a specific watched vendor by ID | [optional] 
 **primary_hostname** | **str**| Restricts the questionnaire risks returned to a specific watched vendor by vendor primary hostname | [optional] 
 **questionnaire_id** | **int**| Restricts the questionnaire risks returned to a specific questionnaire by ID | [optional] 
 **page_token** | **str**| The token of the page to be returned. Will return the first page if left blank. | [optional] 
 **page_size** | **int**| The number of risks to return per page. This Integer between 10 and 2000 defaults to 1000 if not supplied. | [optional] 
 **ignore_waived_risks** | **bool**| Indicates that waived risks should not be returned in the risk set | [optional] 

### Return type

[**QuestionnaireRisksResponsePayloadBodyV2**](QuestionnaireRisksResponsePayloadBodyV2.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_risks**
> GetRisksV1RespBody vendor_risks(primary_hostname, min_severity=min_severity)

Get a list of active risks for a vendor

Returns a list of risks that have been detected for a particular vendor.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))
primary_hostname = 'primary_hostname_example' # str | The primary hostname of the vendor to return risks for
min_severity = 'info' # str | Minimum severity for the risks (optional) (default to info)

try:
    # Get a list of active risks for a vendor
    api_response = api_instance.vendor_risks(primary_hostname, min_severity=min_severity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->vendor_risks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_hostname** | **str**| The primary hostname of the vendor to return risks for | 
 **min_severity** | **str**| Minimum severity for the risks | [optional] [default to info]

### Return type

[**GetRisksV1RespBody**](GetRisksV1RespBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendor_risks_diff**
> RisksDiffResponsePayloadBody vendor_risks_diff(vendor_primary_hostname, start_date, end_date=end_date)

Get a list of risk changes for a vendor

Returns a list of the risks introduced and risks resolved for domains or IPs between two dates.  # The maximum allowed interval is 30 days

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))
vendor_primary_hostname = 'vendor_primary_hostname_example' # str | The primary hostname for a vendor
start_date = '2013-10-20T19:20:30+01:00' # datetime | The date to use as the starting point for determining risks introduced/resolved (RFC 3339 format).
end_date = '2013-10-20T19:20:30+01:00' # datetime | The date to use as the final state for determining risks introduced/resolved (RFC 3339 format). If not provided, the latest risks will be used. (optional)

try:
    # Get a list of risk changes for a vendor
    api_response = api_instance.vendor_risks_diff(vendor_primary_hostname, start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->vendor_risks_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_primary_hostname** | **str**| The primary hostname for a vendor | 
 **start_date** | **datetime**| The date to use as the starting point for determining risks introduced/resolved (RFC 3339 format). | 
 **end_date** | **datetime**| The date to use as the final state for determining risks introduced/resolved (RFC 3339 format). If not provided, the latest risks will be used. | [optional] 

### Return type

[**RisksDiffResponsePayloadBody**](RisksDiffResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_risks_diff**
> VendorsRisksDiffResponsePayloadBody vendors_risks_diff(start_date, end_date=end_date, page_token=page_token, page_size=page_size)

Get a list of risk changes for monitored vendors

Returns a list of the risks introduced and risks resolved for domains or IPs between two dates across your monitored vendors.  The maximum allowed interval is 30 days.

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
api_instance = upguard.RisksApi(upguard.ApiClient(configuration))
start_date = '2013-10-20T19:20:30+01:00' # datetime | The date to use as the starting point for determining risks introduced/resolved (RFC 3339 format).
end_date = '2013-10-20T19:20:30+01:00' # datetime | The date to use as the final state for determining risks introduced/resolved (RFC 3339 format). If not provided, the latest risks will be used. (optional)
page_token = 'page_token_example' # str | The token of the page to be returned. Will return the first page if left blank. (optional)
page_size = 20 # int | The number of results to return per page. Valid values range from 10 to 200. Defaults to 20 if unset. (optional) (default to 20)

try:
    # Get a list of risk changes for monitored vendors
    api_response = api_instance.vendors_risks_diff(start_date, end_date=end_date, page_token=page_token, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RisksApi->vendors_risks_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The date to use as the starting point for determining risks introduced/resolved (RFC 3339 format). | 
 **end_date** | **datetime**| The date to use as the final state for determining risks introduced/resolved (RFC 3339 format). If not provided, the latest risks will be used. | [optional] 
 **page_token** | **str**| The token of the page to be returned. Will return the first page if left blank. | [optional] 
 **page_size** | **int**| The number of results to return per page. Valid values range from 10 to 200. Defaults to 20 if unset. | [optional] [default to 20]

### Return type

[**VendorsRisksDiffResponsePayloadBody**](VendorsRisksDiffResponsePayloadBody.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

