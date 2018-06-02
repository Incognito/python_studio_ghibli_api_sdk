# studio_ghibli_api_sdk.SpeciesApi

All URIs are relative to *https://ghibliapi.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**species_get**](SpeciesApi.md#species_get) | **GET** /species | Species
[**species_id_get**](SpeciesApi.md#species_id_get) | **GET** /species/{id} | Species ID


# **species_get**
> list[Species] species_get(fields=fields, limit=limit)

Species

The Species endpoint returns information about all of the Studio Ghibli species. This includes humans, animals, and spirits et al. 

### Example
```python
from __future__ import print_function
import time
import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = studio_ghibli_api_sdk.SpeciesApi()
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)
limit = 789 # int | amount of results (default 50) (maximum 250) (optional)

try:
    # Species
    api_response = api_instance.species_get(fields=fields, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeciesApi->species_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 
 **limit** | **int**| amount of results (default 50) (maximum 250) | [optional] 

### Return type

[**list[Species]**](Species.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **species_id_get**
> list[Species] species_id_get(id, fields=fields)

Species ID

Returns an individual species

### Example
```python
from __future__ import print_function
import time
import studio_ghibli_api_sdk
from studio_ghibli_api_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = studio_ghibli_api_sdk.SpeciesApi()
id = '789' # str | film `id`
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)

try:
    # Species ID
    api_response = api_instance.species_id_get(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpeciesApi->species_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| film &#x60;id&#x60; | 
 **fields** | **str**| comma-separated list of fields to include in the response | [optional] 

### Return type

[**list[Species]**](Species.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

