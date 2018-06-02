# studio_ghibli_api_sdk.PeopleApi

All URIs are relative to *https://ghibliapi.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**people_get**](PeopleApi.md#people_get) | **GET** /people | Return all people
[**people_id_get**](PeopleApi.md#people_id_get) | **GET** /people/{id} | People ID


# **people_get**
> list[People] people_get(fields=fields, limit=limit)

Return all people

The People endpoint returns information about all of the Studio Ghibli people. This broadly includes all Ghibli characters, human and non-. 

### Example
```python
from __future__ import print_function
import time
import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = studio_ghibli_api_sdk.PeopleApi()
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)
limit = 789 # int | amount of results (default 50) (maximum 250) (optional)

try:
    # Return all people
    api_response = api_instance.people_get(fields=fields, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 
 **limit** | **int**| amount of results (default 50) (maximum 250) | [optional] 

### Return type

[**list[People]**](People.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_id_get**
> list[People] people_id_get(id, fields=fields)

People ID

Returns a person based on a single ID 

### Example
```python
from __future__ import print_function
import time
import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = studio_ghibli_api_sdk.PeopleApi()
id = 789 # int | person `id`
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)

try:
    # People ID
    api_response = api_instance.people_id_get(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleApi->people_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| person &#x60;id&#x60; | 
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 

### Return type

[**list[People]**](People.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

