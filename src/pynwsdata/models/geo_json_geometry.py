
from collections.abc import Mapping
import sys
from typing import TYPE_CHECKING, Any, ClassVar, Self
from pynwsdata.api_object import ApiObject, ApiConst
from importlib.util import find_spec, module_from_spec

GeometryTypes: dict[str, tuple[str, str]] = {
    # mapping from class names to submodules of __package__
    "Point": ("GeoJSONPoint", "geo_json_point"),
    "Polygon": ("GeoJSONPolygon", "geo_json_polygon"),
    "LineString":  ("GeoJSONLineString", "geo_json_line_string"),
    "MultiPolygon": ("GeoJSONMultiPolygon", "geo_json_multi_polygon"),
    "MultiLineString": ("GeoJSONMultiLineString", "geo_json_multi_line_string"),
    "MultiPoint": ("GeoJSONMultiPoint", "geo_json_multi_point")
}


class GeoJsonGeometry(ApiObject):
    # abstract base class
    """
    A GeoJSON geometry object. Please refer to IETF RFC 7946 for information on the GeoJSON format.
    """
    if TYPE_CHECKING:
        # value from the enum 'type' property of the actual implementation class,
        # referencing the original openapi.yaml
        type_code: ClassVar[str]

    # an effective enumeration of implementing classes
    subtypes: ClassVar[dict[str, type[Self]]] = dict()


    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        try:
            tc = cls.type_code
        except AttributeError:
            pass
        else:
            tc = sys.intern(tc)
            cls.type_code = tc
            GeoJsonGeometry.subtypes[tc] = cls

    @classmethod
    def get_subtype(cls, type_code: str) -> type[Self]:
        try:
            return cls.subtypes[sys.intern(type_code)]
        except KeyError:
            pass

        try:
            clsname, submodule = GeometryTypes[type_code]
        except KeyError:
            raise ValueError("Unrecognized subtype", type_code, cls)

        # deferred import
        mname = ".".join((__package__, submodule))
        spec = find_spec(mname)
        if spec is None:
            raise RuntimeError("Submodule not found", spec)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        clsname = sys.intern(clsname)
        scls = getattr(module, clsname)
        cls.subtypes[clsname] = scls
        return scls

    @classmethod
    def from_json_map(cls, mapping: Mapping[str, Any]) -> Self:
        try:
            tc: str = mapping[ApiConst.TYPE]
        except KeyError:
            raise ValueError("Type code not provided",
                             mapping, cls) from None

        subcls = cls.get_subtype(tc)
        return subcls.from_json_map(mapping)

    @classmethod
    def from_json_parsed(cls, mapping: dict[str, Any]) -> Self:
        if cls is GeoJsonGeometry:
            try:
                tc: str = mapping[ApiConst.TYPE]
            except KeyError:
                raise ValueError("Type code not provided",
                                 mapping, cls) from None

            subcls = cls.get_subtype(tc)
            return subcls.from_json_parsed(mapping)
        else:
            return super().from_json_parsed(mapping)
