# swagger_client.LocationsApi

All URIs are relative to *https://ghibliapi.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_get**](LocationsApi.md#locations_get) | **GET** /locations | Return all locations
[**locations_id_get**](LocationsApi.md#locations_id_get) | **GET** /locations/{id} | Location ID


# **locations_get**
> list[Locations] locations_get(fields=fields, limit=limit)

Return all locations

The Locations endpoint returns information about all of the Studio Ghibli locations. This broadly includes lands, countries, and places. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationsApi()
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)
limit = 789 # int | amount of results (default 50) (maximum 250) (optional)

try:
    # Return all locations
    api_response = api_instance.locations_get(fields=fields, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->locations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 
 **limit** | **int**| amount of results (default 50) (maximum 250) | [optional] 

### Return type

[**list[Locations]**](Locations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **locations_id_get**
> object locations_id_get(id, fields=fields)

Location ID

Returns an individual location.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationsApi()
id = 789 # int | location `id`
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)

try:
    # Location ID
    api_response = api_instance.locations_id_get(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->locations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| location &#x60;id&#x60; | 
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

