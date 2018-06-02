# studio_ghibli_api_sdk.VehiclesApi

All URIs are relative to *https://ghibliapi.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vehicles_get**](VehiclesApi.md#vehicles_get) | **GET** /vehicles | Vehicles
[**vehicles_id_get**](VehiclesApi.md#vehicles_id_get) | **GET** /vehicles/{id} | Vehicle ID


# **vehicles_get**
> list[Vehicles] vehicles_get(fields=fields, limit=limit)

Vehicles

The Vehicles endpoint returns information about all of the Studio Ghibli vechiles. This includes cars, ships, and planes. 

### Example
```python
from __future__ import print_function
import time
import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = studio_ghibli_api_sdk.VehiclesApi()
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)
limit = 789 # int | amount of results (default 50) (maximum 250) (optional)

try:
    # Vehicles
    api_response = api_instance.vehicles_get(fields=fields, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->vehicles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 
 **limit** | **int**| amount of results (default 50) (maximum 250) | [optional] 

### Return type

[**list[Vehicles]**](Vehicles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vehicles_id_get**
> list[Vehicles] vehicles_id_get(id, fields=fields)

Vehicle ID

An individual vehicle

### Example
```python
from __future__ import print_function
import time
import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = studio_ghibli_api_sdk.VehiclesApi()
id = 789 # int | film `id`
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)

try:
    # Vehicle ID
    api_response = api_instance.vehicles_id_get(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehiclesApi->vehicles_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| film &#x60;id&#x60; | 
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 

### Return type

[**list[Vehicles]**](Vehicles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

