# studio_ghibli_api_sdk.FilmsApi

All URIs are relative to *https://ghibliapi.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**films_get**](FilmsApi.md#films_get) | **GET** /films | Return all films
[**films_id_get**](FilmsApi.md#films_id_get) | **GET** /films/{id} | Film ID


# **films_get**
> list[Films] films_get(fields=fields, limit=limit)

Return all films

The Films endpoint returns information about all of the Studio Ghibli films. 

### Example
```python
from __future__ import print_function
import time
import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = studio_ghibli_api_sdk.FilmsApi()
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)
limit = 789 # int | amount of results (default 50) (maximum 250) (optional)

try:
    # Return all films
    api_response = api_instance.films_get(fields=fields, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilmsApi->films_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 
 **limit** | **int**| amount of results (default 50) (maximum 250) | [optional] 

### Return type

[**list[Films]**](Films.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **films_id_get**
> list[Films] films_id_get(id, fields=fields)

Film ID

Returns a film based on a single ID 

### Example
```python
from __future__ import print_function
import time
import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = studio_ghibli_api_sdk.FilmsApi()
id = '2baf70d1-42bb-4437-b551-e5fed5a87abe' # str | film `id`

fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)

try:
    # Film ID
    api_response = api_instance.films_id_get(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilmsApi->films_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| film &#x60;id&#x60; | 
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 

### Return type

[**list[Films]**](Films.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

