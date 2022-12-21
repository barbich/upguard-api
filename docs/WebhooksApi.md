# upguard.WebhooksApi

All URIs are relative to *https://cyber-risk.upguard.com/api/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Create a new webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks | Delete a webhook
[**list_webhooks**](WebhooksApi.md#list_webhooks) | **GET** /webhooks | List webhooks
[**sample_webhook**](WebhooksApi.md#sample_webhook) | **GET** /webhooks/sample | Webhook example data
[**webhooks_notification_types**](WebhooksApi.md#webhooks_notification_types) | **GET** /webhooks/notification_types | Webhook notification types


# **create_webhook**
> CreateWebhookResponsePayload create_webhook(name, hook_url, notification_type_ids, webhook_type=webhook_type)

Create a new webhook

Create a new webhook subscribing to the provided list of notifications.

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
api_instance = upguard.WebhooksApi(upguard.ApiClient(configuration))
name = 'name_example' # str | The name given to the webhook
hook_url = 'hook_url_example' # str | The URL used for sending notifications
notification_type_ids = ['notification_type_ids_example'] # list[str] | The list of notifications to subscribe to. For a list of supported notification types and their IDs use the /api/public/webhooks/notification_types endpoint.
webhook_type = 'webhook' # str | The type of webhook to create (optional) (default to webhook)

try:
    # Create a new webhook
    api_response = api_instance.create_webhook(name, hook_url, notification_type_ids, webhook_type=webhook_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name given to the webhook | 
 **hook_url** | **str**| The URL used for sending notifications | 
 **notification_type_ids** | [**list[str]**](str.md)| The list of notifications to subscribe to. For a list of supported notification types and their IDs use the /api/public/webhooks/notification_types endpoint. | 
 **webhook_type** | **str**| The type of webhook to create | [optional] [default to webhook]

### Return type

[**CreateWebhookResponsePayload**](CreateWebhookResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> DeleteWebhookResponsePayload delete_webhook(id)

Delete a webhook

Delete a webhook by ID.

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
api_instance = upguard.WebhooksApi(upguard.ApiClient(configuration))
id = 'id_example' # str | The id of the webhook to delete

try:
    # Delete a webhook
    api_response = api_instance.delete_webhook(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the webhook to delete | 

### Return type

[**DeleteWebhookResponsePayload**](DeleteWebhookResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> ListWebhookResponsePayload list_webhooks()

List webhooks

List all registered webhooks.

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
api_instance = upguard.WebhooksApi(upguard.ApiClient(configuration))

try:
    # List webhooks
    api_response = api_instance.list_webhooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->list_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListWebhookResponsePayload**](ListWebhookResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_webhook**
> ExampleDataWebhookResponsePayload sample_webhook(id=id, notification_type_ids=notification_type_ids)

Webhook example data

Get the example data for one or more notification types.

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
api_instance = upguard.WebhooksApi(upguard.ApiClient(configuration))
id = 'id_example' # str | The ID of a webhook. If specified sample data for all the notification types registered for that webhook will be returned. (optional)
notification_type_ids = ['notification_type_ids_example'] # list[str] | A list of notification type IDs you need sample data for. If a webhook ID is provided this parameter is ignored. (optional)

try:
    # Webhook example data
    api_response = api_instance.sample_webhook(id=id, notification_type_ids=notification_type_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->sample_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a webhook. If specified sample data for all the notification types registered for that webhook will be returned. | [optional] 
 **notification_type_ids** | [**list[str]**](str.md)| A list of notification type IDs you need sample data for. If a webhook ID is provided this parameter is ignored. | [optional] 

### Return type

[**ExampleDataWebhookResponsePayload**](ExampleDataWebhookResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_notification_types**
> GetWebhookNotificationTypesResponsePayload webhooks_notification_types()

Webhook notification types

Get a list of available webhook notification types and their descriptions for your organisation.

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
api_instance = upguard.WebhooksApi(upguard.ApiClient(configuration))

try:
    # Webhook notification types
    api_response = api_instance.webhooks_notification_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_notification_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetWebhookNotificationTypesResponsePayload**](GetWebhookNotificationTypesResponsePayload.md)

### Authorization

[API key in header](../README.md#API key in header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

