# example: Weather station alerts

import asyncio as aio
from pynwsdata.configuration import Configuration
from pynwsdata.api_client import ApiClient
from pynwsdata.api.default_api import DefaultApi
from pynwsdata.exceptions import ApiException

from pprint import pprint

# Defining the host is optional and defaults to https://api.weather.gov
# See configuration.py for a list of supported configuration parameters.
configuration = Configuration(
    host="https://api.weather.gov"
)


def run_exmaple():
    global configuration

    with ApiClient(configuration) as api_client:
        api_instance = DefaultApi(api_client)
        limit = 10

        try:
            api_response = api_instance.alerts_active(limit=limit)
            print("The response of DefaultApi->alerts_active:\n")
            pprint(api_response)
            return api_response
        except ApiException as e:
            print("Exception when calling DefaultApi->alerts_active: %s\n" % e)

if __name__ == "__main__":
    api_response = run_exmaple()

