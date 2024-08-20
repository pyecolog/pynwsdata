# pynwsdata: Client interface for the weather.gov Web API (unofficial)

## Introduction

[`pynwsdata`][gh] provides access to the [API Web Service][api] of the
[National Weather Service][nws].

API data coverage incldues:
- Weather alerts
- Significant Meteorological Advisory (SIGMET) information for aviation
- Weather Forecast Office (WFO) metadata
- Weather forecasts (2.5 km grid)
- Terminal Aerodrome Forecast (TAFS) information for aviation
- Weather headlines (News, WFO headlines)
- Information and textual data for specific text products
  - e.g [Hydrometeorological Automated Data System][hads], HADS reports ([raw JSON][hads-json])
- Weather observations (latest and historic)

## Getting Started

Examples are available in the `examples` source directory

## Availability

Source code is available at GitHub: [pyecolog/pynwsdata][gh]

## Requirements

`pynwsdata` is developed for Python 3.10 and subsequent

Dependencies include:
- [`httpcore`][httpcore]
  - For SOCKS proxy support, please install `httpcore[socks]`
- [`xarray`][xarray]
- [`pint`][pint]
- [`pint-xarray`][pint-xarray]
- [`geopy`][geopy]
- [`ujson`][ujson]
- [`pyfields`][pyfields]

## Installation & Usage

This project uses `pyproject.toml` and can be installed with [`setuptools`][setuptools], using `pip install`

## Tests

Tests have been provided with `pytest`

FIXME the tests from the generated sources have not been updated for recent source revisions

## Addtional Web Resources

- API discovery: https://www.weather.gov/documentation/services-web-api

- FAQ: https://weather-gov.github.io/api/general-faqs

- Discussion, Gridpoints in the API: https://weather-gov.github.io/api/gridpoints

- WMO Units of Measure: https://codes.wmo.int/common/unit
  - e.g `m` https://codes.wmo.int/common/unit/m



## Author

This project is developed by Sean Champ &lt;spchamp@users.noreply.github.com&gt;

## Support

[GitHub Issues][gh-support]

## Attrbutions

- This project is neither affiliated with nor endorsed by the National Weather Service

- This software includes information describing units of measure, derived from
  [WMO No. 306 Vol I.2 Common Code-table C-6 List of units for TDCFs][wmo-units]
  as published under the [Open Government License, version 3][opengov3]

## History

The Python source code for this package was originally generated using the
[OpenAPI Generator](https://openapi-generator.tech)

- API version: `1.13.1`
- Generator version: `7.7.0`
- Build package: `org.openapitools.codegen.languages.PythonClientCodegen`

OpenAPI schema availability: Please refer to the [api.weather.gov General FAQs][api-faq]

Proceeding from the generated sources, subsequent revisions have included:

- Adding a custom API object type, using [pyfields][pyfields] for API object fields.
  This was in lieu of the original dependency on [Pydantic][pydantic]

- Adding support for abstract API object types. In effect, this is an extension to
  the original OpenAPI description, for API object types with common fields and
  types appearing under a generalized base class in the formal API definition.

- Updating the API client model to suport server redirects and paged responses

- HTTP/2 for API access, using [HTTPCore][httpcore]

- [ujson][ujson] for JSON processing


Additional Features:

- Geolocation information with [GeoPy][geopy]

- Data management and analytical modeling with [Xarray][xarray] and [Pint][pint-xarray]

## Other Projects

A partial listing of other projects providing an API for weather information in Python:

- [MetPy][metpy]
- [Open-Meteo][openmeteo]

[gh]: https://github.com/pyecolog/pynwsdata/
[gh-support]: https://github.com/pyecolog/pynwsdata/issues
[api]: https://www.weather.gov/documentation/services-web-api
[api-faq]: https://weather-gov.github.io/api/general-faqs
[nws]: https://www.weather.gov/
[hads]: https://hads.ncep.noaa.gov/
[hads-json]: https://api.weather.gov/products/f90af8a8-dffe-4024-b08d-f26dc8acac03
[pyfields]: https://smarie.github.io/python-pyfields/
[setuptools]: https://setuptools.pypa.io/
[pydantic]: https://docs.pydantic.dev/
[httpcore]: https://www.encode.io/httpcore/
[ujson]: https://pypi.org/project/ujson/
[geopy]: https://geopy.readthedocs.io/
[xarray]: https://docs.xarray.dev/
[pint-xarray]: https://xarray.dev/blog/introducing-pint-xarray
[pint]: https://pint.readthedocs.io/
[wmo-units]: https://codes.wmo.int/common/unit
[opengov3]: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
[metpy]: https://unidata.github.io/MetPy/latest/index.html
[openmeteo]: https://open-meteo.com/

