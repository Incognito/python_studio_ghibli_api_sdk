# swagger-client
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.FilmsApi()
fields = 'fields_example' # str | comma-separated list of fields to include in the response (optional)
limit = 789 # int | amount of results (default 50) (maximum 250) (optional)

try:
    # Return all films
    api_response = api_instance.films_get(fields=fields, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilmsApi->films_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://ghibliapi.herokuapp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FilmsApi* | [**films_get**](docs/FilmsApi.md#films_get) | **GET** /films | Return all films
*FilmsApi* | [**films_id_get**](docs/FilmsApi.md#films_id_get) | **GET** /films/{id} | Film ID
*LocationsApi* | [**locations_get**](docs/LocationsApi.md#locations_get) | **GET** /locations | Return all locations
*LocationsApi* | [**locations_id_get**](docs/LocationsApi.md#locations_id_get) | **GET** /locations/{id} | Location ID
*PeopleApi* | [**people_get**](docs/PeopleApi.md#people_get) | **GET** /people | Return all people
*PeopleApi* | [**people_id_get**](docs/PeopleApi.md#people_id_get) | **GET** /people/{id} | People ID
*SpeciesApi* | [**species_get**](docs/SpeciesApi.md#species_get) | **GET** /species | Species
*SpeciesApi* | [**species_id_get**](docs/SpeciesApi.md#species_id_get) | **GET** /species/{id} | Species ID
*VehiclesApi* | [**vehicles_get**](docs/VehiclesApi.md#vehicles_get) | **GET** /vehicles | Vehicles
*VehiclesApi* | [**vehicles_id_get**](docs/VehiclesApi.md#vehicles_id_get) | **GET** /vehicles/{id} | Vehicle ID


## Documentation For Models

 - [Error](docs/Error.md)
 - [Films](docs/Films.md)
 - [Locations](docs/Locations.md)
 - [People](docs/People.md)
 - [Species](docs/Species.md)
 - [Vehicles](docs/Vehicles.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



