# pynwsdata.DefaultApi

All URIs are relative to *https://api.weather.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alerts_active**](DefaultApi.md#alerts_active) | **GET** /alerts/active | 
[**alerts_active_area**](DefaultApi.md#alerts_active_area) | **GET** /alerts/active/area/{area} | 
[**alerts_active_count**](DefaultApi.md#alerts_active_count) | **GET** /alerts/active/count | 
[**alerts_active_region**](DefaultApi.md#alerts_active_region) | **GET** /alerts/active/region/{region} | 
[**alerts_active_zone**](DefaultApi.md#alerts_active_zone) | **GET** /alerts/active/zone/{zoneId} | 
[**alerts_query**](DefaultApi.md#alerts_query) | **GET** /alerts | 
[**alerts_single**](DefaultApi.md#alerts_single) | **GET** /alerts/{id} | 
[**alerts_types**](DefaultApi.md#alerts_types) | **GET** /alerts/types | 
[**cwa**](DefaultApi.md#cwa) | **GET** /aviation/cwsus/{cwsuId}/cwas/{date}/{sequence} | 
[**cwas**](DefaultApi.md#cwas) | **GET** /aviation/cwsus/{cwsuId}/cwas | 
[**cwsu**](DefaultApi.md#cwsu) | **GET** /aviation/cwsus/{cwsuId} | 
[**glossary**](DefaultApi.md#glossary) | **GET** /glossary | 
[**gridpoint**](DefaultApi.md#gridpoint) | **GET** /gridpoints/{wfo}/{x},{y} | 
[**gridpoint_forecast**](DefaultApi.md#gridpoint_forecast) | **GET** /gridpoints/{wfo}/{x},{y}/forecast | 
[**gridpoint_forecast_hourly**](DefaultApi.md#gridpoint_forecast_hourly) | **GET** /gridpoints/{wfo}/{x},{y}/forecast/hourly | 
[**gridpoint_stations**](DefaultApi.md#gridpoint_stations) | **GET** /gridpoints/{wfo}/{x},{y}/stations | 
[**icons**](DefaultApi.md#icons) | **GET** /icons/{set}/{timeOfDay}/{first} | 
[**icons_dual_condition**](DefaultApi.md#icons_dual_condition) | **GET** /icons/{set}/{timeOfDay}/{first}/{second} | 
[**icons_summary**](DefaultApi.md#icons_summary) | **GET** /icons | 
[**location_products**](DefaultApi.md#location_products) | **GET** /products/locations/{locationId}/types | 
[**obs_station**](DefaultApi.md#obs_station) | **GET** /stations/{stationId} | 
[**obs_stations**](DefaultApi.md#obs_stations) | **GET** /stations | 
[**office**](DefaultApi.md#office) | **GET** /offices/{officeId} | 
[**office_headline**](DefaultApi.md#office_headline) | **GET** /offices/{officeId}/headlines/{headlineId} | 
[**office_headlines**](DefaultApi.md#office_headlines) | **GET** /offices/{officeId}/headlines | 
[**point**](DefaultApi.md#point) | **GET** /points/{point} | 
[**point_stations**](DefaultApi.md#point_stations) | **GET** /points/{point}/stations | 
[**product**](DefaultApi.md#product) | **GET** /products/{productId} | 
[**product_locations**](DefaultApi.md#product_locations) | **GET** /products/locations | 
[**product_types**](DefaultApi.md#product_types) | **GET** /products/types | 
[**products_query**](DefaultApi.md#products_query) | **GET** /products | 
[**products_type**](DefaultApi.md#products_type) | **GET** /products/types/{typeId} | 
[**products_type_location**](DefaultApi.md#products_type_location) | **GET** /products/types/{typeId}/locations/{locationId} | 
[**products_type_locations**](DefaultApi.md#products_type_locations) | **GET** /products/types/{typeId}/locations | 
[**radar_profiler**](DefaultApi.md#radar_profiler) | **GET** /radar/profilers/{stationId} | 
[**radar_queue**](DefaultApi.md#radar_queue) | **GET** /radar/queues/{host} | 
[**radar_server**](DefaultApi.md#radar_server) | **GET** /radar/servers/{id} | 
[**radar_servers**](DefaultApi.md#radar_servers) | **GET** /radar/servers | 
[**radar_station**](DefaultApi.md#radar_station) | **GET** /radar/stations/{stationId} | 
[**radar_station_alarms**](DefaultApi.md#radar_station_alarms) | **GET** /radar/stations/{stationId}/alarms | 
[**radar_stations**](DefaultApi.md#radar_stations) | **GET** /radar/stations | 
[**satellite_thumbnails**](DefaultApi.md#satellite_thumbnails) | **GET** /thumbnails/satellite/{area} | 
[**sigmet**](DefaultApi.md#sigmet) | **GET** /aviation/sigmets/{atsu}/{date}/{time} | 
[**sigmet_query**](DefaultApi.md#sigmet_query) | **GET** /aviation/sigmets | 
[**sigmets_by_atsu**](DefaultApi.md#sigmets_by_atsu) | **GET** /aviation/sigmets/{atsu} | 
[**sigmets_by_atsuby_date**](DefaultApi.md#sigmets_by_atsuby_date) | **GET** /aviation/sigmets/{atsu}/{date} | 
[**station_observation_latest**](DefaultApi.md#station_observation_latest) | **GET** /stations/{stationId}/observations/latest | 
[**station_observation_list**](DefaultApi.md#station_observation_list) | **GET** /stations/{stationId}/observations | 
[**station_observation_time**](DefaultApi.md#station_observation_time) | **GET** /stations/{stationId}/observations/{time} | 
[**taf**](DefaultApi.md#taf) | **GET** /stations/{stationId}/tafs/{date}/{time} | 
[**tafs**](DefaultApi.md#tafs) | **GET** /stations/{stationId}/tafs | 
[**zone**](DefaultApi.md#zone) | **GET** /zones/{type}/{zoneId} | 
[**zone_forecast**](DefaultApi.md#zone_forecast) | **GET** /zones/{type}/{zoneId}/forecast | 
[**zone_list**](DefaultApi.md#zone_list) | **GET** /zones | 
[**zone_list_type**](DefaultApi.md#zone_list_type) | **GET** /zones/{type} | 
[**zone_obs**](DefaultApi.md#zone_obs) | **GET** /zones/forecast/{zoneId}/observations | 
[**zone_stations**](DefaultApi.md#zone_stations) | **GET** /zones/forecast/{zoneId}/stations | 


# **alerts_active**
> AlertCollectionGeoJson alerts_active(status=status, message_type=message_type, event=event, code=code, area=area, point=point, region=region, region_type=region_type, zone=zone, urgency=urgency, severity=severity, certainty=certainty, limit=limit)



Returns all currently active alerts

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.alert_certainty import AlertCertainty
from pynwsdata.models.alert_collection_geo_json import AlertCollectionGeoJson
from pynwsdata.models.alert_severity import AlertSeverity
from pynwsdata.models.alert_urgency import AlertUrgency
from pynwsdata.models.area_code import AreaCode
from pynwsdata.models.marine_region_code import MarineRegionCode
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    status = ['status_example'] # List[str] | Status (actual, exercise, system, test, draft) (optional)
    message_type = ['message_type_example'] # List[str] | Message type (alert, update, cancel) (optional)
    event = ['event_example'] # List[str] | Event name (optional)
    code = ['code_example'] # List[str] | Event code (optional)
    area = [pynwsdata.AreaCode()] # List[AreaCode] | State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone  (optional)
    point = 'point_example' # str | Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone  (optional)
    region = [pynwsdata.MarineRegionCode()] # List[MarineRegionCode] | Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone  (optional)
    region_type = 'region_type_example' # str | Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone  (optional)
    zone = ['zone_example'] # List[str] | Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type  (optional)
    urgency = [pynwsdata.AlertUrgency()] # List[AlertUrgency] | Urgency (immediate, expected, future, past, unknown) (optional)
    severity = [pynwsdata.AlertSeverity()] # List[AlertSeverity] | Severity (extreme, severe, moderate, minor, unknown) (optional)
    certainty = [pynwsdata.AlertCertainty()] # List[AlertCertainty] | Certainty (observed, likely, possible, unlikely, unknown) (optional)
    limit = 500 # int | Limit (optional) (default to 500)

    try:
        api_response = await api_instance.alerts_active(status=status, message_type=message_type, event=event, code=code, area=area, point=point, region=region, region_type=region_type, zone=zone, urgency=urgency, severity=severity, certainty=certainty, limit=limit)
        print("The response of DefaultApi->alerts_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alerts_active: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**List[str]**](str.md)| Status (actual, exercise, system, test, draft) | [optional] 
 **message_type** | [**List[str]**](str.md)| Message type (alert, update, cancel) | [optional] 
 **event** | [**List[str]**](str.md)| Event name | [optional] 
 **code** | [**List[str]**](str.md)| Event code | [optional] 
 **area** | [**List[AreaCode]**](AreaCode.md)| State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone  | [optional] 
 **point** | **str**| Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone  | [optional] 
 **region** | [**List[MarineRegionCode]**](MarineRegionCode.md)| Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone  | [optional] 
 **region_type** | **str**| Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone  | [optional] 
 **zone** | [**List[str]**](str.md)| Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type  | [optional] 
 **urgency** | [**List[AlertUrgency]**](AlertUrgency.md)| Urgency (immediate, expected, future, past, unknown) | [optional] 
 **severity** | [**List[AlertSeverity]**](AlertSeverity.md)| Severity (extreme, severe, moderate, minor, unknown) | [optional] 
 **certainty** | [**List[AlertCertainty]**](AlertCertainty.md)| Certainty (observed, likely, possible, unlikely, unknown) | [optional] 
 **limit** | **int**| Limit | [optional] [default to 500]

### Return type

[**AlertCollectionGeoJson**](AlertCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of alerts. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**301** | Certain common queries may be redirected to discrete URLs |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_active_area**
> AlertCollectionGeoJson alerts_active_area(area)



Returns active alerts for the given area (state or marine area)

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.alert_collection_geo_json import AlertCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    area = pynwsdata.AreaCode() # AreaCode | State/area ID

    try:
        api_response = await api_instance.alerts_active_area(area)
        print("The response of DefaultApi->alerts_active_area:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alerts_active_area: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | [**AreaCode**](.md)| State/area ID | 

### Return type

[**AlertCollectionGeoJson**](AlertCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of alerts. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_active_count**
> AlertsActiveCount200Response alerts_active_count()



Returns info on the number of active alerts

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.alerts_active_count200_response import AlertsActiveCount200Response
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)

    try:
        api_response = await api_instance.alerts_active_count()
        print("The response of DefaultApi->alerts_active_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alerts_active_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertsActiveCount200Response**](AlertsActiveCount200Response.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A data structure showing the counts of active alerts broken down by various categories |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_active_region**
> AlertCollectionGeoJson alerts_active_region(region)



Returns active alerts for the given marine region

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.alert_collection_geo_json import AlertCollectionGeoJson
from pynwsdata.models.marine_region_code import MarineRegionCode
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    region = pynwsdata.MarineRegionCode() # MarineRegionCode | Marine region ID

    try:
        api_response = await api_instance.alerts_active_region(region)
        print("The response of DefaultApi->alerts_active_region:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alerts_active_region: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | [**MarineRegionCode**](.md)| Marine region ID | 

### Return type

[**AlertCollectionGeoJson**](AlertCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of alerts. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_active_zone**
> AlertCollectionGeoJson alerts_active_zone(zone_id)



Returns active alerts for the given NWS public zone or county

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.alert_collection_geo_json import AlertCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    zone_id = 'zone_id_example' # str | NWS public zone/county identifier

    try:
        api_response = await api_instance.alerts_active_zone(zone_id)
        print("The response of DefaultApi->alerts_active_zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alerts_active_zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| NWS public zone/county identifier | 

### Return type

[**AlertCollectionGeoJson**](AlertCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of alerts. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_query**
> AlertCollectionGeoJson alerts_query(active=active, start=start, end=end, status=status, message_type=message_type, event=event, code=code, area=area, point=point, region=region, region_type=region_type, zone=zone, urgency=urgency, severity=severity, certainty=certainty, limit=limit, cursor=cursor)



Returns all alerts

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.alert_certainty import AlertCertainty
from pynwsdata.models.alert_collection_geo_json import AlertCollectionGeoJson
from pynwsdata.models.alert_severity import AlertSeverity
from pynwsdata.models.alert_urgency import AlertUrgency
from pynwsdata.models.area_code import AreaCode
from pynwsdata.models.marine_region_code import MarineRegionCode
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    active = True # bool | List only active alerts (use /alerts/active endpoints instead) (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start time (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End time (optional)
    status = ['status_example'] # List[str] | Status (actual, exercise, system, test, draft) (optional)
    message_type = ['message_type_example'] # List[str] | Message type (alert, update, cancel) (optional)
    event = ['event_example'] # List[str] | Event name (optional)
    code = ['code_example'] # List[str] | Event code (optional)
    area = [pynwsdata.AreaCode()] # List[AreaCode] | State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone  (optional)
    point = 'point_example' # str | Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone  (optional)
    region = [pynwsdata.MarineRegionCode()] # List[MarineRegionCode] | Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone  (optional)
    region_type = 'region_type_example' # str | Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone  (optional)
    zone = ['zone_example'] # List[str] | Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type  (optional)
    urgency = [pynwsdata.AlertUrgency()] # List[AlertUrgency] | Urgency (immediate, expected, future, past, unknown) (optional)
    severity = [pynwsdata.AlertSeverity()] # List[AlertSeverity] | Severity (extreme, severe, moderate, minor, unknown) (optional)
    certainty = [pynwsdata.AlertCertainty()] # List[AlertCertainty] | Certainty (observed, likely, possible, unlikely, unknown) (optional)
    limit = 500 # int | Limit (optional) (default to 500)
    cursor = 'cursor_example' # str | Pagination cursor (optional)

    try:
        api_response = await api_instance.alerts_query(active=active, start=start, end=end, status=status, message_type=message_type, event=event, code=code, area=area, point=point, region=region, region_type=region_type, zone=zone, urgency=urgency, severity=severity, certainty=certainty, limit=limit, cursor=cursor)
        print("The response of DefaultApi->alerts_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alerts_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| List only active alerts (use /alerts/active endpoints instead) | [optional] 
 **start** | **datetime**| Start time | [optional] 
 **end** | **datetime**| End time | [optional] 
 **status** | [**List[str]**](str.md)| Status (actual, exercise, system, test, draft) | [optional] 
 **message_type** | [**List[str]**](str.md)| Message type (alert, update, cancel) | [optional] 
 **event** | [**List[str]**](str.md)| Event name | [optional] 
 **code** | [**List[str]**](str.md)| Event code | [optional] 
 **area** | [**List[AreaCode]**](AreaCode.md)| State/territory code or marine area code This parameter is incompatible with the following parameters: point, region, region_type, zone  | [optional] 
 **point** | **str**| Point (latitude,longitude) This parameter is incompatible with the following parameters: area, region, region_type, zone  | [optional] 
 **region** | [**List[MarineRegionCode]**](MarineRegionCode.md)| Marine region code This parameter is incompatible with the following parameters: area, point, region_type, zone  | [optional] 
 **region_type** | **str**| Region type (land or marine) This parameter is incompatible with the following parameters: area, point, region, zone  | [optional] 
 **zone** | [**List[str]**](str.md)| Zone ID (forecast or county) This parameter is incompatible with the following parameters: area, point, region, region_type  | [optional] 
 **urgency** | [**List[AlertUrgency]**](AlertUrgency.md)| Urgency (immediate, expected, future, past, unknown) | [optional] 
 **severity** | [**List[AlertSeverity]**](AlertSeverity.md)| Severity (extreme, severe, moderate, minor, unknown) | [optional] 
 **certainty** | [**List[AlertCertainty]**](AlertCertainty.md)| Certainty (observed, likely, possible, unlikely, unknown) | [optional] 
 **limit** | **int**| Limit | [optional] [default to 500]
 **cursor** | **str**| Pagination cursor | [optional] 

### Return type

[**AlertCollectionGeoJson**](AlertCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/atom+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of alerts. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**301** | Certain common queries may be redirected to discrete URLs |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_single**
> AlertGeoJson alerts_single(id)



Returns a specific alert

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.alert_geo_json import AlertGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    id = 'id_example' # str | Alert identifier

    try:
        api_response = await api_instance.alerts_single(id)
        print("The response of DefaultApi->alerts_single:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alerts_single: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Alert identifier | 

### Return type

[**AlertGeoJson**](AlertGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/cap+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An alert record |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alerts_types**
> AlertsTypes200Response alerts_types()



Returns a list of alert types

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.alerts_types200_response import AlertsTypes200Response
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)

    try:
        api_response = await api_instance.alerts_types()
        print("The response of DefaultApi->alerts_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->alerts_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AlertsTypes200Response**](AlertsTypes200Response.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recognized event types |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cwa**
> CenterWeatherAdvisoryGeoJson cwa(cwsu_id, var_date, sequence)



Returns a list of Center Weather Advisories from a CWSU

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.center_weather_advisory_geo_json import CenterWeatherAdvisoryGeoJson
from pynwsdata.models.nws_center_weather_service_unit_id import NWSCenterWeatherServiceUnitId
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    cwsu_id = pynwsdata.NWSCenterWeatherServiceUnitId() # NWSCenterWeatherServiceUnitId | NWS CWSU ID
    var_date = '2013-10-20' # date | Date (YYYY-MM-DD format)
    sequence = 56 # int | Sequence number

    try:
        api_response = await api_instance.cwa(cwsu_id, var_date, sequence)
        print("The response of DefaultApi->cwa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cwa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cwsu_id** | [**NWSCenterWeatherServiceUnitId**](.md)| NWS CWSU ID | 
 **var_date** | **date**| Date (YYYY-MM-DD format) | 
 **sequence** | **int**| Sequence number | 

### Return type

[**CenterWeatherAdvisoryGeoJson**](CenterWeatherAdvisoryGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/vnd.noaa.uswx+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cwas**
> CenterWeatherAdvisoryCollectionGeoJson cwas(cwsu_id)



Returns a list of Center Weather Advisories from a CWSU

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.center_weather_advisory_collection_geo_json import CenterWeatherAdvisoryCollectionGeoJson
from pynwsdata.models.nws_center_weather_service_unit_id import NWSCenterWeatherServiceUnitId
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    cwsu_id = pynwsdata.NWSCenterWeatherServiceUnitId() # NWSCenterWeatherServiceUnitId | NWS CWSU ID

    try:
        api_response = await api_instance.cwas(cwsu_id)
        print("The response of DefaultApi->cwas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cwas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cwsu_id** | [**NWSCenterWeatherServiceUnitId**](.md)| NWS CWSU ID | 

### Return type

[**CenterWeatherAdvisoryCollectionGeoJson**](CenterWeatherAdvisoryCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cwsu**
> Office cwsu(cwsu_id)



Returns metadata about a Center Weather Service Unit

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.nws_center_weather_service_unit_id import NWSCenterWeatherServiceUnitId
from pynwsdata.models.office import Office
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    cwsu_id = pynwsdata.NWSCenterWeatherServiceUnitId() # NWSCenterWeatherServiceUnitId | NWS CWSU ID

    try:
        api_response = await api_instance.cwsu(cwsu_id)
        print("The response of DefaultApi->cwsu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->cwsu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cwsu_id** | [**NWSCenterWeatherServiceUnitId**](.md)| NWS CWSU ID | 

### Return type

[**Office**](Office.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **glossary**
> Glossary200Response glossary()



Returns glossary terms

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.glossary200_response import Glossary200Response
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)

    try:
        api_response = await api_instance.glossary()
        print("The response of DefaultApi->glossary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->glossary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Glossary200Response**](Glossary200Response.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set of glossary terms |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridpoint**
> GridpointGeoJson gridpoint(wfo, x, y)



Returns raw numerical forecast data for a 2.5km grid area

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.gridpoint_geo_json import GridpointGeoJson
from pynwsdata.models.nws_forecast_office_id import NWSForecastOfficeId
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    wfo = pynwsdata.NWSForecastOfficeId() # NWSForecastOfficeId | Forecast office ID
    x = 56 # int | Forecast grid X coordinate
    y = 56 # int | Forecast grid Y coordinate

    try:
        api_response = await api_instance.gridpoint(wfo, x, y)
        print("The response of DefaultApi->gridpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gridpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfo** | [**NWSForecastOfficeId**](.md)| Forecast office ID | 
 **x** | **int**| Forecast grid X coordinate | 
 **y** | **int**| Forecast grid Y coordinate | 

### Return type

[**GridpointGeoJson**](GridpointGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gridpoint forecast data |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridpoint_forecast**
> GridpointForecastGeoJson gridpoint_forecast(wfo, x, y, feature_flags=feature_flags, units=units)



Returns a textual forecast for a 2.5km grid area

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.gridpoint_forecast_geo_json import GridpointForecastGeoJson
from pynwsdata.models.gridpoint_forecast_units import GridpointForecastUnits
from pynwsdata.models.nws_forecast_office_id import NWSForecastOfficeId
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    wfo = pynwsdata.NWSForecastOfficeId() # NWSForecastOfficeId | Forecast office ID
    x = 56 # int | Forecast grid X coordinate
    y = 56 # int | Forecast grid Y coordinate
    feature_flags = ['feature_flags_example'] # List[str] | Enable future and experimental features (see documentation for more info): * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue  (optional)
    units = us # GridpointForecastUnits | Use US customary or SI (metric) units in textual output (optional) (default to us)

    try:
        api_response = await api_instance.gridpoint_forecast(wfo, x, y, feature_flags=feature_flags, units=units)
        print("The response of DefaultApi->gridpoint_forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gridpoint_forecast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfo** | [**NWSForecastOfficeId**](.md)| Forecast office ID | 
 **x** | **int**| Forecast grid X coordinate | 
 **y** | **int**| Forecast grid Y coordinate | 
 **feature_flags** | [**List[str]**](str.md)| Enable future and experimental features (see documentation for more info): * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue  | [optional] 
 **units** | [**GridpointForecastUnits**](.md)| Use US customary or SI (metric) units in textual output | [optional] [default to us]

### Return type

[**GridpointForecastGeoJson**](GridpointForecastGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.dwml+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A forecast for a gridpoint. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridpoint_forecast_hourly**
> GridpointForecastGeoJson gridpoint_forecast_hourly(wfo, x, y, feature_flags=feature_flags, units=units)



Returns a textual hourly forecast for a 2.5km grid area

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.gridpoint_forecast_geo_json import GridpointForecastGeoJson
from pynwsdata.models.gridpoint_forecast_units import GridpointForecastUnits
from pynwsdata.models.nws_forecast_office_id import NWSForecastOfficeId
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    wfo = pynwsdata.NWSForecastOfficeId() # NWSForecastOfficeId | Forecast office ID
    x = 56 # int | Forecast grid X coordinate
    y = 56 # int | Forecast grid Y coordinate
    feature_flags = ['feature_flags_example'] # List[str] | Enable future and experimental features (see documentation for more info): * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue  (optional)
    units = us # GridpointForecastUnits | Use US customary or SI (metric) units in textual output (optional) (default to us)

    try:
        api_response = await api_instance.gridpoint_forecast_hourly(wfo, x, y, feature_flags=feature_flags, units=units)
        print("The response of DefaultApi->gridpoint_forecast_hourly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gridpoint_forecast_hourly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfo** | [**NWSForecastOfficeId**](.md)| Forecast office ID | 
 **x** | **int**| Forecast grid X coordinate | 
 **y** | **int**| Forecast grid Y coordinate | 
 **feature_flags** | [**List[str]**](str.md)| Enable future and experimental features (see documentation for more info): * forecast_temperature_qv: Represent temperature as QuantitativeValue * forecast_wind_speed_qv: Represent wind speed as QuantitativeValue  | [optional] 
 **units** | [**GridpointForecastUnits**](.md)| Use US customary or SI (metric) units in textual output | [optional] [default to us]

### Return type

[**GridpointForecastGeoJson**](GridpointForecastGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.dwml+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A forecast for a gridpoint. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gridpoint_stations**
> ObservationStationCollectionGeoJson gridpoint_stations(wfo, x, y, limit=limit, cursor=cursor)



Returns a list of observation stations usable for a given 2.5km grid area

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.nws_forecast_office_id import NWSForecastOfficeId
from pynwsdata.models.observation_station_collection_geo_json import ObservationStationCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    wfo = pynwsdata.NWSForecastOfficeId() # NWSForecastOfficeId | Forecast office ID
    x = 56 # int | Forecast grid X coordinate
    y = 56 # int | Forecast grid Y coordinate
    limit = 500 # int | Limit (optional) (default to 500)
    cursor = 'cursor_example' # str | Pagination cursor (optional)

    try:
        api_response = await api_instance.gridpoint_stations(wfo, x, y, limit=limit, cursor=cursor)
        print("The response of DefaultApi->gridpoint_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->gridpoint_stations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wfo** | [**NWSForecastOfficeId**](.md)| Forecast office ID | 
 **x** | **int**| Forecast grid X coordinate | 
 **y** | **int**| Forecast grid Y coordinate | 
 **limit** | **int**| Limit | [optional] [default to 500]
 **cursor** | **str**| Pagination cursor | [optional] 

### Return type

[**ObservationStationCollectionGeoJson**](ObservationStationCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of observation stations. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icons**
> bytearray icons(set, time_of_day, first, size=size, fontsize=fontsize)



Returns a forecast icon. Icon services in API are deprecated.

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    set = 'set_example' # str | .
    time_of_day = 'time_of_day_example' # str | .
    first = 'first_example' # str | .
    size = pynwsdata.IconsSizeParameter() # IconsSizeParameter | Font size (optional)
    fontsize = 56 # int | Font size (optional)

    try:
        api_response = await api_instance.icons(set, time_of_day, first, size=size, fontsize=fontsize)
        print("The response of DefaultApi->icons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->icons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **str**| . | 
 **time_of_day** | **str**| . | 
 **first** | **str**| . | 
 **size** | [**IconsSizeParameter**](.md)| Font size | [optional] 
 **fontsize** | **int**| Font size | [optional] 

### Return type

**bytearray**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icons_dual_condition**
> bytearray icons_dual_condition(set, time_of_day, first, second, size=size, fontsize=fontsize)



Returns a forecast icon. Icon services in API are deprecated.

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    set = 'set_example' # str | .
    time_of_day = 'time_of_day_example' # str | .
    first = 'first_example' # str | .
    second = 'second_example' # str | .
    size = pynwsdata.IconsSizeParameter() # IconsSizeParameter | Font size (optional)
    fontsize = 56 # int | Font size (optional)

    try:
        api_response = await api_instance.icons_dual_condition(set, time_of_day, first, second, size=size, fontsize=fontsize)
        print("The response of DefaultApi->icons_dual_condition:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->icons_dual_condition: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **str**| . | 
 **time_of_day** | **str**| . | 
 **first** | **str**| . | 
 **second** | **str**| . | 
 **size** | [**IconsSizeParameter**](.md)| Font size | [optional] 
 **fontsize** | **int**| Font size | [optional] 

### Return type

**bytearray**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **icons_summary**
> IconsSummary200Response icons_summary()



Returns a list of icon codes and textual descriptions. Icon services in API are deprecated.

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.icons_summary200_response import IconsSummary200Response
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)

    try:
        api_response = await api_instance.icons_summary()
        print("The response of DefaultApi->icons_summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->icons_summary: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IconsSummary200Response**](IconsSummary200Response.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **location_products**
> TextProductTypeCollection location_products(location_id)



Returns a list of valid text product types for a given issuance location

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.text_product_type_collection import TextProductTypeCollection
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    location_id = 'location_id_example' # str | .

    try:
        api_response = await api_instance.location_products(location_id)
        print("The response of DefaultApi->location_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->location_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| . | 

### Return type

[**TextProductTypeCollection**](TextProductTypeCollection.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obs_station**
> ObservationStationGeoJson obs_station(station_id)



Returns metadata about a given observation station

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.observation_station_geo_json import ObservationStationGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Observation station ID

    try:
        api_response = await api_instance.obs_station(station_id)
        print("The response of DefaultApi->obs_station:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->obs_station: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Observation station ID | 

### Return type

[**ObservationStationGeoJson**](ObservationStationGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obs_stations**
> ObservationStationCollectionGeoJson obs_stations(id=id, state=state, limit=limit, cursor=cursor)



Returns a list of observation stations.

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.area_code import AreaCode
from pynwsdata.models.observation_station_collection_geo_json import ObservationStationCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    id = ['id_example'] # List[str] | Filter by observation station ID (optional)
    state = [pynwsdata.AreaCode()] # List[AreaCode] | Filter by state/marine area code (optional)
    limit = 500 # int | Limit (optional) (default to 500)
    cursor = 'cursor_example' # str | Pagination cursor (optional)

    try:
        api_response = await api_instance.obs_stations(id=id, state=state, limit=limit, cursor=cursor)
        print("The response of DefaultApi->obs_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->obs_stations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| Filter by observation station ID | [optional] 
 **state** | [**List[AreaCode]**](AreaCode.md)| Filter by state/marine area code | [optional] 
 **limit** | **int**| Limit | [optional] [default to 500]
 **cursor** | **str**| Pagination cursor | [optional] 

### Return type

[**ObservationStationCollectionGeoJson**](ObservationStationCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of observation stations. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office**
> Office office(office_id)



Returns metadata about a NWS forecast office

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.office import Office
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    office_id = pynwsdata.NWSOfficeId() # NWSOfficeId | NWS office ID

    try:
        api_response = await api_instance.office(office_id)
        print("The response of DefaultApi->office:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->office: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | [**NWSOfficeId**](.md)| NWS office ID | 

### Return type

[**Office**](Office.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office_headline**
> OfficeHeadline office_headline(office_id, headline_id)



Returns a specific news headline for a given NWS office

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.office_headline import OfficeHeadline
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    office_id = pynwsdata.NWSOfficeId() # NWSOfficeId | NWS office ID
    headline_id = 'headline_id_example' # str | Headline record ID

    try:
        api_response = await api_instance.office_headline(office_id, headline_id)
        print("The response of DefaultApi->office_headline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->office_headline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | [**NWSOfficeId**](.md)| NWS office ID | 
 **headline_id** | **str**| Headline record ID | 

### Return type

[**OfficeHeadline**](OfficeHeadline.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **office_headlines**
> OfficeHeadlineCollection office_headlines(office_id)



Returns a list of news headlines for a given NWS office

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.office_headline_collection import OfficeHeadlineCollection
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    office_id = pynwsdata.NWSOfficeId() # NWSOfficeId | NWS office ID

    try:
        api_response = await api_instance.office_headlines(office_id)
        print("The response of DefaultApi->office_headlines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->office_headlines: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | [**NWSOfficeId**](.md)| NWS office ID | 

### Return type

[**OfficeHeadlineCollection**](OfficeHeadlineCollection.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **point**
> PointGeoJson point(point)



Returns metadata about a given latitude/longitude point

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.point_geo_json import PointGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    point = 'point_example' # str | Point (latitude, longitude)

    try:
        api_response = await api_instance.point(point)
        print("The response of DefaultApi->point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->point: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point** | **str**| Point (latitude, longitude) | 

### Return type

[**PointGeoJson**](PointGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **point_stations**
> ProblemDetail point_stations(point)



Returns a list of observation stations for a given point

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.problem_detail import ProblemDetail
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    point = 'point_example' # str | Point (latitude, longitude)

    try:
        api_response = await api_instance.point_stations(point)
        print("The response of DefaultApi->point_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->point_stations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point** | **str**| Point (latitude, longitude) | 

### Return type

[**ProblemDetail**](ProblemDetail.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**301** | redirect to gridpoint stations |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product**
> TextProduct product(product_id)



Returns a specific text product

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.text_product import TextProduct
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    product_id = 'product_id_example' # str | .

    try:
        api_response = await api_instance.product(product_id)
        print("The response of DefaultApi->product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| . | 

### Return type

[**TextProduct**](TextProduct.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_locations**
> TextProductLocationCollection product_locations()



Returns a list of valid text product issuance locations

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.text_product_location_collection import TextProductLocationCollection
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)

    try:
        api_response = await api_instance.product_locations()
        print("The response of DefaultApi->product_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->product_locations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TextProductLocationCollection**](TextProductLocationCollection.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_types**
> TextProductTypeCollection product_types()



Returns a list of valid text product types and codes

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.text_product_type_collection import TextProductTypeCollection
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)

    try:
        api_response = await api_instance.product_types()
        print("The response of DefaultApi->product_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->product_types: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TextProductTypeCollection**](TextProductTypeCollection.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_query**
> TextProductCollection products_query(location=location, start=start, end=end, office=office, wmoid=wmoid, type=type, limit=limit)



Returns a list of text products

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.text_product_collection import TextProductCollection
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    location = ['location_example'] # List[str] | Location id (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start time (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End time (optional)
    office = ['office_example'] # List[str] | Issuing office (optional)
    wmoid = ['wmoid_example'] # List[str] | WMO id code (optional)
    type = ['type_example'] # List[str] | Product code (optional)
    limit = 56 # int | Limit (optional)

    try:
        api_response = await api_instance.products_query(location=location, start=start, end=end, office=office, wmoid=wmoid, type=type, limit=limit)
        print("The response of DefaultApi->products_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->products_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**List[str]**](str.md)| Location id | [optional] 
 **start** | **datetime**| Start time | [optional] 
 **end** | **datetime**| End time | [optional] 
 **office** | [**List[str]**](str.md)| Issuing office | [optional] 
 **wmoid** | [**List[str]**](str.md)| WMO id code | [optional] 
 **type** | [**List[str]**](str.md)| Product code | [optional] 
 **limit** | **int**| Limit | [optional] 

### Return type

[**TextProductCollection**](TextProductCollection.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_type**
> TextProductCollection products_type(type_id)



Returns a list of text products of a given type

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.text_product_collection import TextProductCollection
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    type_id = 'type_id_example' # str | .

    try:
        api_response = await api_instance.products_type(type_id)
        print("The response of DefaultApi->products_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->products_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**| . | 

### Return type

[**TextProductCollection**](TextProductCollection.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_type_location**
> TextProductCollection products_type_location(type_id, location_id)



Returns a list of text products of a given type for a given issuance location

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.text_product_collection import TextProductCollection
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    type_id = 'type_id_example' # str | .
    location_id = 'location_id_example' # str | .

    try:
        api_response = await api_instance.products_type_location(type_id, location_id)
        print("The response of DefaultApi->products_type_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->products_type_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**| . | 
 **location_id** | **str**| . | 

### Return type

[**TextProductCollection**](TextProductCollection.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_type_locations**
> TextProductLocationCollection products_type_locations(type_id)



Returns a list of valid text product issuance locations for a given product type

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.text_product_location_collection import TextProductLocationCollection
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    type_id = 'type_id_example' # str | .

    try:
        api_response = await api_instance.products_type_locations(type_id)
        print("The response of DefaultApi->products_type_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->products_type_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**| . | 

### Return type

[**TextProductLocationCollection**](TextProductLocationCollection.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_profiler**
> object radar_profiler(station_id, time=time, interval=interval)



Returns metadata about a given radar wind profiler

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Profiler station ID
    time = pynwsdata.ISO8601Interval() # ISO8601Interval | Time interval (optional)
    interval = 'interval_example' # str | Averaging interval (optional)

    try:
        api_response = await api_instance.radar_profiler(station_id, time=time, interval=interval)
        print("The response of DefaultApi->radar_profiler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->radar_profiler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Profiler station ID | 
 **time** | [**ISO8601Interval**](.md)| Time interval | [optional] 
 **interval** | **str**| Averaging interval | [optional] 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_queue**
> object radar_queue(host, limit=limit, arrived=arrived, created=created, published=published, station=station, type=type, feed=feed, resolution=resolution)



Returns metadata about a given radar queue

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    host = 'host_example' # str | LDM host
    limit = 56 # int | Record limit (optional)
    arrived = pynwsdata.ISO8601Interval() # ISO8601Interval | Range for arrival time (optional)
    created = pynwsdata.ISO8601Interval() # ISO8601Interval | Range for creation time (optional)
    published = pynwsdata.ISO8601Interval() # ISO8601Interval | Range for publish time (optional)
    station = 'station_example' # str | Station identifier (optional)
    type = 'type_example' # str | Record type (optional)
    feed = 'feed_example' # str | Originating product feed (optional)
    resolution = 56 # int | Resolution version (optional)

    try:
        api_response = await api_instance.radar_queue(host, limit=limit, arrived=arrived, created=created, published=published, station=station, type=type, feed=feed, resolution=resolution)
        print("The response of DefaultApi->radar_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->radar_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| LDM host | 
 **limit** | **int**| Record limit | [optional] 
 **arrived** | [**ISO8601Interval**](.md)| Range for arrival time | [optional] 
 **created** | [**ISO8601Interval**](.md)| Range for creation time | [optional] 
 **published** | [**ISO8601Interval**](.md)| Range for publish time | [optional] 
 **station** | **str**| Station identifier | [optional] 
 **type** | **str**| Record type | [optional] 
 **feed** | **str**| Originating product feed | [optional] 
 **resolution** | **int**| Resolution version | [optional] 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_server**
> object radar_server(id, reporting_host=reporting_host)



Returns metadata about a given radar server

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    id = 'id_example' # str | Server ID
    reporting_host = 'reporting_host_example' # str | Show records from specific reporting host (optional)

    try:
        api_response = await api_instance.radar_server(id, reporting_host=reporting_host)
        print("The response of DefaultApi->radar_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->radar_server: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Server ID | 
 **reporting_host** | **str**| Show records from specific reporting host | [optional] 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_servers**
> object radar_servers(reporting_host=reporting_host)



Returns a list of radar servers

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    reporting_host = 'reporting_host_example' # str | Show records from specific reporting host (optional)

    try:
        api_response = await api_instance.radar_servers(reporting_host=reporting_host)
        print("The response of DefaultApi->radar_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->radar_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reporting_host** | **str**| Show records from specific reporting host | [optional] 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_station**
> object radar_station(station_id, reporting_host=reporting_host, host=host)



Returns metadata about a given radar station

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Radar station ID
    reporting_host = 'reporting_host_example' # str | Show RDA and latency info from specific reporting host (optional)
    host = 'host_example' # str | Show latency info from specific LDM host (optional)

    try:
        api_response = await api_instance.radar_station(station_id, reporting_host=reporting_host, host=host)
        print("The response of DefaultApi->radar_station:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->radar_station: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Radar station ID | 
 **reporting_host** | **str**| Show RDA and latency info from specific reporting host | [optional] 
 **host** | **str**| Show latency info from specific LDM host | [optional] 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_station_alarms**
> object radar_station_alarms(station_id)



Returns metadata about a given radar station alarms

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Radar station ID

    try:
        api_response = await api_instance.radar_station_alarms(station_id)
        print("The response of DefaultApi->radar_station_alarms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->radar_station_alarms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Radar station ID | 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **radar_stations**
> object radar_stations(station_type=station_type, reporting_host=reporting_host, host=host)



Returns a list of radar stations

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_type = ['station_type_example'] # List[str] | Limit results to a specific station type or types (optional)
    reporting_host = 'reporting_host_example' # str | Show RDA and latency info from specific reporting host (optional)
    host = 'host_example' # str | Show latency info from specific LDM host (optional)

    try:
        api_response = await api_instance.radar_stations(station_type=station_type, reporting_host=reporting_host, host=host)
        print("The response of DefaultApi->radar_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->radar_stations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_type** | [**List[str]**](str.md)| Limit results to a specific station type or types | [optional] 
 **reporting_host** | **str**| Show RDA and latency info from specific reporting host | [optional] 
 **host** | **str**| Show latency info from specific LDM host | [optional] 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **satellite_thumbnails**
> bytearray satellite_thumbnails(area)



Returns a thumbnail image for a satellite region. Image services in API are deprecated.

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    area = 'area_example' # str | .

    try:
        api_response = await api_instance.satellite_thumbnails(area)
        print("The response of DefaultApi->satellite_thumbnails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->satellite_thumbnails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **area** | **str**| . | 

### Return type

**bytearray**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An image file |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sigmet**
> SigmetGeoJson sigmet(atsu, var_date, time)



Returns a specific SIGMET/AIRMET

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.sigmet_geo_json import SigmetGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    atsu = 'atsu_example' # str | ATSU identifier
    var_date = '2013-10-20' # date | Date (YYYY-MM-DD format)
    time = 'time_example' # str | Time (HHMM format). This time is always specified in UTC (Zulu) time.

    try:
        api_response = await api_instance.sigmet(atsu, var_date, time)
        print("The response of DefaultApi->sigmet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sigmet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atsu** | **str**| ATSU identifier | 
 **var_date** | **date**| Date (YYYY-MM-DD format) | 
 **time** | **str**| Time (HHMM format). This time is always specified in UTC (Zulu) time. | 

### Return type

[**SigmetGeoJson**](SigmetGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/vnd.noaa.uswx+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sigmet_query**
> SigmetCollectionGeoJson sigmet_query(start=start, end=end, var_date=var_date, atsu=atsu, sequence=sequence)



Returns a list of SIGMET/AIRMETs

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.sigmet_collection_geo_json import SigmetCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start time (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End time (optional)
    var_date = '2013-10-20' # date | Date (YYYY-MM-DD format) (optional)
    atsu = 'atsu_example' # str | ATSU identifier (optional)
    sequence = 'sequence_example' # str | SIGMET sequence number (optional)

    try:
        api_response = await api_instance.sigmet_query(start=start, end=end, var_date=var_date, atsu=atsu, sequence=sequence)
        print("The response of DefaultApi->sigmet_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sigmet_query: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| Start time | [optional] 
 **end** | **datetime**| End time | [optional] 
 **var_date** | **date**| Date (YYYY-MM-DD format) | [optional] 
 **atsu** | **str**| ATSU identifier | [optional] 
 **sequence** | **str**| SIGMET sequence number | [optional] 

### Return type

[**SigmetCollectionGeoJson**](SigmetCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sigmets_by_atsu**
> SigmetCollectionGeoJson sigmets_by_atsu(atsu)



Returns a list of SIGMET/AIRMETs for the specified ATSU

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.sigmet_collection_geo_json import SigmetCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    atsu = 'atsu_example' # str | ATSU identifier

    try:
        api_response = await api_instance.sigmets_by_atsu(atsu)
        print("The response of DefaultApi->sigmets_by_atsu:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sigmets_by_atsu: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atsu** | **str**| ATSU identifier | 

### Return type

[**SigmetCollectionGeoJson**](SigmetCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sigmets_by_atsuby_date**
> SigmetCollectionGeoJson sigmets_by_atsuby_date(atsu, var_date)



Returns a list of SIGMET/AIRMETs for the specified ATSU for the specified date

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.sigmet_collection_geo_json import SigmetCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    atsu = 'atsu_example' # str | ATSU identifier
    var_date = '2013-10-20' # date | Date (YYYY-MM-DD format)

    try:
        api_response = await api_instance.sigmets_by_atsuby_date(atsu, var_date)
        print("The response of DefaultApi->sigmets_by_atsuby_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sigmets_by_atsuby_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **atsu** | **str**| ATSU identifier | 
 **var_date** | **date**| Date (YYYY-MM-DD format) | 

### Return type

[**SigmetCollectionGeoJson**](SigmetCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **station_observation_latest**
> ObservationGeoJson station_observation_latest(station_id, require_qc=require_qc)



Returns the latest observation for a station

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.observation_geo_json import ObservationGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Observation station ID
    require_qc = True # bool | Require QC (optional)

    try:
        api_response = await api_instance.station_observation_latest(station_id, require_qc=require_qc)
        print("The response of DefaultApi->station_observation_latest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->station_observation_latest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Observation station ID | 
 **require_qc** | **bool**| Require QC | [optional] 

### Return type

[**ObservationGeoJson**](ObservationGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.uswx+xml, application/vnd.noaa.obs+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An observation record. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **station_observation_list**
> ObservationCollectionGeoJson station_observation_list(station_id, start=start, end=end, limit=limit)



Returns a list of observations for a given station

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.observation_collection_geo_json import ObservationCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Observation station ID
    start = '2013-10-20T19:20:30+01:00' # datetime | Start time (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End time (optional)
    limit = 56 # int | Limit (optional)

    try:
        api_response = await api_instance.station_observation_list(station_id, start=start, end=end, limit=limit)
        print("The response of DefaultApi->station_observation_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->station_observation_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Observation station ID | 
 **start** | **datetime**| Start time | [optional] 
 **end** | **datetime**| End time | [optional] 
 **limit** | **int**| Limit | [optional] 

### Return type

[**ObservationCollectionGeoJson**](ObservationCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of observation records. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **station_observation_time**
> ObservationGeoJson station_observation_time(station_id, time)



Returns a single observation.

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.observation_geo_json import ObservationGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Observation station ID
    time = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of requested observation

    try:
        api_response = await api_instance.station_observation_time(station_id, time)
        print("The response of DefaultApi->station_observation_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->station_observation_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Observation station ID | 
 **time** | **datetime**| Timestamp of requested observation | 

### Return type

[**ObservationGeoJson**](ObservationGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/vnd.noaa.uswx+xml, application/vnd.noaa.obs+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An observation record. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **taf**
> object taf(station_id, var_date, time)



Returns a single Terminal Aerodrome Forecast.

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Observation station ID
    var_date = '2013-10-20' # date | Date (YYYY-MM-DD format)
    time = 'time_example' # str | Time (HHMM format). This time is always specified in UTC (Zulu) time.

    try:
        api_response = await api_instance.taf(station_id, var_date, time)
        print("The response of DefaultApi->taf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->taf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Observation station ID | 
 **var_date** | **date**| Date (YYYY-MM-DD format) | 
 **time** | **str**| Time (HHMM format). This time is always specified in UTC (Zulu) time. | 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.wmo.iwxxm+xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tafs**
> object tafs(station_id)



Returns Terminal Aerodrome Forecasts for the specified airport station.

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    station_id = 'station_id_example' # str | Observation station ID

    try:
        api_response = await api_instance.tafs(station_id)
        print("The response of DefaultApi->tafs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->tafs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station_id** | **str**| Observation station ID | 

### Return type

**object**

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zone**
> ZoneGeoJson zone(type, zone_id, effective=effective)



Returns metadata about a given zone

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.nws_zone_type import NWSZoneType
from pynwsdata.models.zone_geo_json import ZoneGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    type = pynwsdata.NWSZoneType() # NWSZoneType | Zone type
    zone_id = 'zone_id_example' # str | NWS public zone/county identifier
    effective = '2013-10-20T19:20:30+01:00' # datetime | Effective date/time (optional)

    try:
        api_response = await api_instance.zone(type, zone_id, effective=effective)
        print("The response of DefaultApi->zone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->zone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**NWSZoneType**](.md)| Zone type | 
 **zone_id** | **str**| NWS public zone/county identifier | 
 **effective** | **datetime**| Effective date/time | [optional] 

### Return type

[**ZoneGeoJson**](ZoneGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zone_forecast**
> ZoneForecastGeoJson zone_forecast(type, zone_id)



Returns the current zone forecast for a given zone

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.zone_forecast_geo_json import ZoneForecastGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    type = 'type_example' # str | Zone type
    zone_id = 'zone_id_example' # str | NWS public zone/county identifier

    try:
        api_response = await api_instance.zone_forecast(type, zone_id)
        print("The response of DefaultApi->zone_forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->zone_forecast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Zone type | 
 **zone_id** | **str**| NWS public zone/county identifier | 

### Return type

[**ZoneForecastGeoJson**](ZoneForecastGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zone_list**
> ZoneCollectionGeoJson zone_list(id=id, area=area, region=region, type=type, point=point, include_geometry=include_geometry, limit=limit, effective=effective)



Returns a list of zones

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.area_code import AreaCode
from pynwsdata.models.nws_zone_type import NWSZoneType
from pynwsdata.models.region_code import RegionCode
from pynwsdata.models.zone_collection_geo_json import ZoneCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    id = ['id_example'] # List[str] | Zone ID (forecast or county) (optional)
    area = [pynwsdata.AreaCode()] # List[AreaCode] | State/marine area code (optional)
    region = [pynwsdata.RegionCode()] # List[RegionCode] | Region code (optional)
    type = [pynwsdata.NWSZoneType()] # List[NWSZoneType] | Zone type (optional)
    point = 'point_example' # str | Point (latitude,longitude) (optional)
    include_geometry = True # bool | Include geometry in results (true/false) (optional)
    limit = 56 # int | Limit (optional)
    effective = '2013-10-20T19:20:30+01:00' # datetime | Effective date/time (optional)

    try:
        api_response = await api_instance.zone_list(id=id, area=area, region=region, type=type, point=point, include_geometry=include_geometry, limit=limit, effective=effective)
        print("The response of DefaultApi->zone_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->zone_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**List[str]**](str.md)| Zone ID (forecast or county) | [optional] 
 **area** | [**List[AreaCode]**](AreaCode.md)| State/marine area code | [optional] 
 **region** | [**List[RegionCode]**](RegionCode.md)| Region code | [optional] 
 **type** | [**List[NWSZoneType]**](NWSZoneType.md)| Zone type | [optional] 
 **point** | **str**| Point (latitude,longitude) | [optional] 
 **include_geometry** | **bool**| Include geometry in results (true/false) | [optional] 
 **limit** | **int**| Limit | [optional] 
 **effective** | **datetime**| Effective date/time | [optional] 

### Return type

[**ZoneCollectionGeoJson**](ZoneCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zone_list_type**
> ZoneCollectionGeoJson zone_list_type(type, id=id, area=area, region=region, type2=type2, point=point, include_geometry=include_geometry, limit=limit, effective=effective)



Returns a list of zones of a given type

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.area_code import AreaCode
from pynwsdata.models.nws_zone_type import NWSZoneType
from pynwsdata.models.region_code import RegionCode
from pynwsdata.models.zone_collection_geo_json import ZoneCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    type = pynwsdata.NWSZoneType() # NWSZoneType | Zone type
    id = ['id_example'] # List[str] | Zone ID (forecast or county) (optional)
    area = [pynwsdata.AreaCode()] # List[AreaCode] | State/marine area code (optional)
    region = [pynwsdata.RegionCode()] # List[RegionCode] | Region code (optional)
    type2 = [pynwsdata.NWSZoneType()] # List[NWSZoneType] | Zone type (optional)
    point = 'point_example' # str | Point (latitude,longitude) (optional)
    include_geometry = True # bool | Include geometry in results (true/false) (optional)
    limit = 56 # int | Limit (optional)
    effective = '2013-10-20T19:20:30+01:00' # datetime | Effective date/time (optional)

    try:
        api_response = await api_instance.zone_list_type(type, id=id, area=area, region=region, type2=type2, point=point, include_geometry=include_geometry, limit=limit, effective=effective)
        print("The response of DefaultApi->zone_list_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->zone_list_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**NWSZoneType**](.md)| Zone type | 
 **id** | [**List[str]**](str.md)| Zone ID (forecast or county) | [optional] 
 **area** | [**List[AreaCode]**](AreaCode.md)| State/marine area code | [optional] 
 **region** | [**List[RegionCode]**](RegionCode.md)| Region code | [optional] 
 **type2** | [**List[NWSZoneType]**](NWSZoneType.md)| Zone type | [optional] 
 **point** | **str**| Point (latitude,longitude) | [optional] 
 **include_geometry** | **bool**| Include geometry in results (true/false) | [optional] 
 **limit** | **int**| Limit | [optional] 
 **effective** | **datetime**| Effective date/time | [optional] 

### Return type

[**ZoneCollectionGeoJson**](ZoneCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zone_obs**
> ObservationCollectionGeoJson zone_obs(zone_id, start=start, end=end, limit=limit)



Returns a list of observations for a given zone

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.observation_collection_geo_json import ObservationCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    zone_id = 'zone_id_example' # str | NWS public zone/county identifier
    start = '2013-10-20T19:20:30+01:00' # datetime | Start date/time (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End date/time (optional)
    limit = 56 # int | Limit (optional)

    try:
        api_response = await api_instance.zone_obs(zone_id, start=start, end=end, limit=limit)
        print("The response of DefaultApi->zone_obs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->zone_obs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| NWS public zone/county identifier | 
 **start** | **datetime**| Start date/time | [optional] 
 **end** | **datetime**| End date/time | [optional] 
 **limit** | **int**| Limit | [optional] 

### Return type

[**ObservationCollectionGeoJson**](ObservationCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zone_stations**
> ObservationStationCollectionGeoJson zone_stations(zone_id, limit=limit, cursor=cursor)



Returns a list of observation stations for a given zone

### Example

* Api Key Authentication (userAgent):

```python
import pynwsdata
from pynwsdata.models.observation_station_collection_geo_json import ObservationStationCollectionGeoJson
from pynwsdata.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of all supported configuration parameters.
configuration = pynwsdata.Configuration(
    host = "https://api.weather.gov"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: userAgent
configuration.api_key['userAgent'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['userAgent'] = 'Bearer'

# Enter a context with an instance of the API client
async with pynwsdata.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pynwsdata.DefaultApi(api_client)
    zone_id = 'zone_id_example' # str | NWS public zone/county identifier
    limit = 500 # int | Limit (optional) (default to 500)
    cursor = 'cursor_example' # str | Pagination cursor (optional)

    try:
        api_response = await api_instance.zone_stations(zone_id, limit=limit, cursor=cursor)
        print("The response of DefaultApi->zone_stations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->zone_stations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **str**| NWS public zone/county identifier | 
 **limit** | **int**| Limit | [optional] [default to 500]
 **cursor** | **str**| Pagination cursor | [optional] 

### Return type

[**ObservationStationCollectionGeoJson**](ObservationStationCollectionGeoJson.md)

### Authorization

[userAgent](../README.md#userAgent)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A collection of observation stations. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |
**0** | An error response. |  * X-Correlation-Id -  <br>  * X-Request-Id -  <br>  * X-Server-Id -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

