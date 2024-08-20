
from aenum import StrEnum, EnumMeta, extend_enum
import csv
import os
from pint import UnitRegistry
from pint_xarray import unit_registry

from pynwsdata.models.quantitative_value import QuantitativeValue

class UnitMeta(EnumMeta):
    def __getitem__(self, name: str):
        return self._member_map_[name]


class WmoUnit(StrEnum, metaclass=UnitMeta):

    def get_unit(self, registry: UnitRegistry):
        return registry.Unit(self.value)

    @classmethod
    def qv_pint(cls, qv: QuantitativeValue, registry: UnitRegistry):
        unit = qv.unit_code
        unit_ns, unit_name = unit.split(":")
        # assert unit_ns == "wmoUnit"
        value = qv.value
        return registry.Quantity(value, cls[unit_name].get_unit(reg))

    @classmethod
    def load_wmo_csv(cls, path: str):
        with open(path) as stream:
            sread = csv.reader(stream)
            hdr = {h: offset for (offset, h) in enumerate(next(sread))}
            id_offset = hdr['@id']
            notn_offset = hdr['skos:notation']
            for row in sread:
                id_direct = row[id_offset]
                # using the path basename for the id removed of "<>" delimiters
                id = os.path.basename(id_direct[1:-1])
                notn = row[notn_offset]
                extend_enum(WmoUnit, id, notn)

    @classmethod
    def initialize(cls):
        if not cls._member_map_:
            wmo_csv = os.path.join(os.path.dirname(__file__), "wmo.csv")        
            cls.load_wmo_csv(wmo_csv)
        return cls

if __name__ == "__main__":

    wmo_csv = os.path.join(os.path.dirname(__file__), "wmo.csv")
    WmoUnit.load_wmo_csv(wmo_csv)

    reg = UnitRegistry()

    # WmoUnit["km_h-1"] = reg.Unit("km h^-1")

    assert WmoUnit["km_h-1"].get_unit(reg) == reg.Unit("km h^-1")


def parse_unit(unit: str) -> str:
    global unit_registry
    if unit.startswith("wmo"):
        unit = unit.split(":", 1)[-1]
    # try to parse the unit name to a pint unit name
    try:
        unit = WmoUnit[unit]
    except KeyError:
        pass
    else:
        unit = str(unit_registry.Unit(unit))
    return unit

# TBD store the UnitRegistry instance as an application feature
#
# TBD integrating with xarray attributes and custom dataset methods
# - unit can be stored in some aspect of an xarray dimension ?
#   https://pint-xarray.readthedocs.io/en/stable/creation.html
