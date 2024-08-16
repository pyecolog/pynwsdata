# Alert

An object representing a public alert message. Unless otherwise noted, the fields in this object correspond to the National Weather Service CAP v1.2 specification, which extends the OASIS Common Alerting Protocol (CAP) v1.2 specification and USA Integrated Public Alert and Warning System (IPAWS) Profile v1.0. Refer to this documentation for more complete information. http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html http://docs.oasis-open.org/emergency/cap/v1.2/ipaws-profile/v1.0/cs01/cap-v1.2-ipaws-profile-cs01.html https://alerts.weather.gov/#technical-notes-v12 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the alert message. | [optional] 
**area_desc** | **str** | A textual description of the area affected by the alert. | [optional] 
**geocode** | [**AlertGeocode**](AlertGeocode.md) |  | [optional] 
**affected_zones** | **List[str]** | An array of API links for zones affected by the alert. This is an API-specific extension field and is not part of the CAP specification.  | [optional] 
**references** | [**List[AlertReferencesInner]**](AlertReferencesInner.md) | A list of prior alerts that this alert updates or replaces. | [optional] 
**sent** | **datetime** | The time of the origination of the alert message. | [optional] 
**effective** | **datetime** | The effective time of the information of the alert message. | [optional] 
**onset** | **datetime** | The expected time of the beginning of the subject event of the alert message. | [optional] 
**expires** | **datetime** | The expiry time of the information of the alert message. | [optional] 
**ends** | **datetime** | The expected end time of the subject event of the alert message. | [optional] 
**status** | [**AlertStatus**](AlertStatus.md) |  | [optional] 
**message_type** | [**AlertMessageType**](AlertMessageType.md) |  | [optional] 
**category** | **str** | The code denoting the category of the subject event of the alert message. | [optional] 
**severity** | [**AlertSeverity**](AlertSeverity.md) |  | [optional] 
**certainty** | [**AlertCertainty**](AlertCertainty.md) |  | [optional] 
**urgency** | [**AlertUrgency**](AlertUrgency.md) |  | [optional] 
**event** | **str** | The text denoting the type of the subject event of the alert message. | [optional] 
**sender** | **str** | Email address of the NWS webmaster. | [optional] 
**sender_name** | **str** | The text naming the originator of the alert message. | [optional] 
**headline** | **str** | The text headline of the alert message. | [optional] 
**description** | **str** | The text describing the subject event of the alert message. | [optional] 
**instruction** | **str** | The text describing the recommended action to be taken by recipients of the alert message.  | [optional] 
**response** | **str** | The code denoting the type of action recommended for the target audience. This corresponds to responseType in the CAP specification.  | [optional] 
**parameters** | **Dict[str, List[object]]** | System-specific additional parameters associated with the alert message. The keys in this object correspond to parameter definitions in the NWS CAP specification.  | [optional] 

## Example

```python
from pynwsdata.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


