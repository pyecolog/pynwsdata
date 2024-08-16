# GridpointForecastPeriodWindSpeed

Wind speed for the period. This property as an string value is deprecated. Future versions will express this value as a quantitative value object. To make use of the future standard format now, set the \"forecast_wind_speed_qv\" feature flag on the request. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | A measured value | [optional] 
**max_value** | **float** | The maximum value of a range of measured values | [optional] 
**min_value** | **float** | The minimum value of a range of measured values | [optional] 
**unit_code** | **str** | A string denoting a unit of measure, expressed in the format \&quot;{unit}\&quot; or \&quot;{namespace}:{unit}\&quot;. Units with the namespace \&quot;wmo\&quot; or \&quot;wmoUnit\&quot; are defined in the World Meteorological Organization Codes Registry at http://codes.wmo.int/common/unit and should be canonically resolvable to http://codes.wmo.int/common/unit/{unit}. Units with the namespace \&quot;nwsUnit\&quot; are currently custom and do not align to any standard. Units with no namespace or the namespace \&quot;uc\&quot; are compliant with the Unified Code for Units of Measure syntax defined at https://unitsofmeasure.org/. This also aligns with recent versions of the Geographic Markup Language (GML) standard, the IWXXM standard, and OGC Observations and Measurements v2.0 (ISO/DIS 19156). Namespaced units are considered deprecated. We will be aligning API to use the same standards as GML/IWXXM in the future.  | [optional] 
**quality_control** | **str** | For values in observation records, the quality control flag from the MADIS system. The definitions of these flags can be found at https://madis.ncep.noaa.gov/madis_sfc_qc_notes.shtml  | [optional] 

## Example

```python
from pynwsdata.models.gridpoint_forecast_period_wind_speed import GridpointForecastPeriodWindSpeed

# TODO update the JSON string below
json = "{}"
# create an instance of GridpointForecastPeriodWindSpeed from a JSON string
gridpoint_forecast_period_wind_speed_instance = GridpointForecastPeriodWindSpeed.from_json(json)
# print the JSON string representation of the object
print(GridpointForecastPeriodWindSpeed.to_json())

# convert the object into a dict
gridpoint_forecast_period_wind_speed_dict = gridpoint_forecast_period_wind_speed_instance.to_dict()
# create an instance of GridpointForecastPeriodWindSpeed from a dict
gridpoint_forecast_period_wind_speed_from_dict = GridpointForecastPeriodWindSpeed.from_dict(gridpoint_forecast_period_wind_speed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


