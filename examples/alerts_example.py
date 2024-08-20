# example: Weather station alerts

from pynwsdata.configuration import Configuration
from pynwsdata.api_client import ApiClient
from pynwsdata.api.geo_api import GeoApi
from pynwsdata.exceptions import ApiException

from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of supported configuration parameters.
configuration = Configuration(
    host="https://api.weather.gov"
)


def run_exmaple():
    global configuration

    with GeoApi.client_scope() as api_instance:

        try:
            api_response = api_instance.alerts_active()
            print("The response of DefaultApi->alerts_active:\n")
            pprint(api_response)
            return api_response
        except ApiException as e:
            print("Exception when calling DefaultApi->alerts_active: %s\n" % e)

if __name__ == "__main__":
    api_response = run_exmaple()

