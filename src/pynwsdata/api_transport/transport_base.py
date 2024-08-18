# API interface types

from aenum import Enum, EnumType
from abc import ABC, abstractmethod
from datetime import datetime
import ujson
from decimal import Decimal
import numpy as np
from pyfields.core import Field
from warnings import warn

from typing import (
    TYPE_CHECKING, Any, Generic,
    Literal, Optional, Union, TypeAlias, ClassVar,
    TypeVar, TypeVarTuple
)
from typing_extensions import (
    get_args, get_origin
)

if TYPE_CHECKING:
    # type alias declaration for aenum Enum
    Enum: TypeAlias = EnumType  # noqa: F811

NONETYPE: type = type(None)
UNIONTYPE: type = type(Union)


def is_union_type(spec: "TypeSpec") -> bool:
    origin = get_origin(spec)
    return origin is Union


def get_optional_type(type_hint: "TypeSpec") -> Optional["TypeSpec"]:
    if is_union_type(type_hint):
        gen = (arg for arg in get_args(type_hint) if arg is not NONETYPE)
        try:
            first = next(gen)
        except StopIteration:
            return None
        try:
            next(gen)
        except StopIteration:
            # Union type with one non-NoneType element => Optional type
            return first
        else:
            return None
    else:
        return None


if TYPE_CHECKING:
    UnionType: TypeAlias = Union.__class__
else:
    UnionType: TypeAlias = type(Union)

TypeSpec: TypeAlias = Union[type, UnionType, Literal.__class__, None]

Ti = TypeVar("Ti")
To = TypeVar("To")


class DeferredBase:
    # singleton type
    #
    # slots on DEFERRED will be initialized when the api_object model is imported to some module
    __slots__ = "__weakref__", "API_OBJECT", "MODEL_INTERFACE"
    if TYPE_CHECKING:
        from pynwsdata.api_object import ApiObject, ModelInterface
        API_OBJECT = ApiObject
        MODEL_INTERFACE = ModelInterface


DEFERRED = DeferredBase()


class TransportInterface(Generic[Ti, To], ABC):
    __slots__ = "__weakref__", "interface_type", "value_type", "interface_class", "interface_field"

    if TYPE_CHECKING:
        interface_type: Ti
        value_type: To
        interface_class: type[To]
        # generally a context for the interface, if not None
        interface_field: Optional[Field]

    def __init__(self,
                 interface_type: Union[type[Ti], TypeSpec],
                 value_type: Union[type[To], TypeSpec],
                 interface_class: Optional[type] = None,
                 field: Optional[Field] = None):
        self.interface_type = interface_type
        self.value_type = value_type
        if interface_class is not None:
            self.interface_class = interface_class
        self.interface_field = field

    @abstractmethod
    def from_json_parsed(self, value: Ti) -> To:
        raise NotImplementedError(self.from_json_parsed)

    @abstractmethod
    def to_json_parsed(self, instance: To) -> Ti:
        raise NotImplementedError(self.to_json_parsed)

    def from_json_str(self, value: str) -> To:
        return self.from_json_parsed(ujson.loads(value, precise_float=True))

    def to_json_str(self, object: To) -> str:
        return ujson.dumps(self.to_json_parsed(object), ensure_ascii=False)

    def can_parse(self, value: Any) -> bool:
        try:
            cls = self.interface_class
        except AttributeError:
            return False
        else:
            return isinstance(value, cls)


ValueType: TypeAlias = Union[str, int, float, bool, bytes, datetime]
ValueTypeMap: TypeAlias = dict[type, type[TransportInterface]]
VALUE_TYPES: ValueTypeMap = dict()

SeriesTypeSet: set[type] = {list, tuple, set, frozenset}
SeriesType: TypeAlias = Union[list, tuple, set, frozenset]

JsonObject: TypeAlias = Union[int, float, bool, str, dict[str, Any], None]

Tse = TypeVar("Tse")
Tv = TypeVar("Tv", bound=ValueType)
Ts = TypeVar("Ts", bound=SeriesType)
Te = TypeVar("Te", bound=Enum)
Tes = TypeVarTuple("Tes")  # ?? for the sinle enum union type in the server API


def get_type_class(type_hint: Union[TypeAlias, type], label: str = "Unknown"):
    # known limitations
    #
    # - no implementation for Literal types
    # - no implementation for Annotated types
    # - no support for forward-refernced types or type namespace
    #
    origin = get_origin(type_hint)
    if origin is None:
        origin = type_hint
    if isinstance(origin, type):
        return origin
    elif origin is Union:
        gen = filter(lambda arg: arg is not NONETYPE, get_args(type_hint))
        try:
            first = next(gen)
        except StopIteration:
            raise UnknownTypeClass(type_hint, label) from None
        nxt = next(gen, None)
        if nxt:
            # this Union type has no single type class
            raise UnknownTypeClass(type_hint, label)
        else:
            # this Union type is equivalent to Optional type hint
            return get_type_class(first, label)
    elif isinstance(origin, TypeVar):
        bound = origin.__bound__
        if bound is None:
            raise UnknownTypeClass(type_hint, label)
        else:
            return get_type_class(bound, label)
    elif isinstance(origin, ClassVar):
        first, *_ = get_args(type_hint)
        return get_type_class(first, label)
    else:
        raise UnknownTypeClass(type_hint, label)


def get_type_interface(type_hint: Any,
                       label: str = "Unknown",
                       value_type_map: Optional[ValueTypeMap] = None,
                       **kw) -> TransportInterface[Ti, To]:
    # ApiField utility function

    try:
        tc = get_type_class(type_hint, label)
    except UnknownTypeClass:
        origin = get_origin(type_hint)
        if origin is dict:
            return ValueInterface(type_hint, dict, dict, **kw)
        elif origin is Union:
            return UnionInterface(type_hint, type_hint, **kw)
        else:
            raise

    if issubclass(tc, DEFERRED.API_OBJECT):
        return DEFERRED.MODEL_INTERFACE(tc, **kw)
    elif issubclass(tc, Enum):
        return EnumInterface(tc, **kw)

    if value_type_map is None:
        value_type_map = VALUE_TYPES
    try:
        vtype = value_type_map[tc]
    except KeyError:
        pass
    else:
        return vtype(type_hint, tc, tc, **kw)

    if tc in SeriesTypeSet:
        # assumption: series element type will not include 'None' here ...
        #
        # regardless, the original type_hint might be a union type containing NoneType
        # as well as some series type, e.g list[str]
        optional = get_optional_type(type_hint)
        if optional is not None:
            type_hint = optional
        if is_union_type(type_hint):
            type_hint = get_args(type_hint[0])
        first, *rest = get_args(type_hint)
        if rest:
            warn(UserWarning("%s: Ambigous series element type" %
                             label, type_hint), stacklevel=3)
            return UnknownInterface(type_hint, tc, tc, **kw)
        else:
            elt_impl = get_type_interface(first, label, **kw)
        return SeriesInterface(tc, elt_impl, **kw)
    elif tc is dict:
        return ValueInterface(type_hint, tc, tc, **kw)
    elif isinstance(tc, type):
        return tc
    else:
        warn(UserWarning("%s: Unrecognized type hint" %
             label, type_hint), stacklevel=3)
        return UnknownInterface(type_hint, tc, tc, **kw)


class UnionInterface(TransportInterface[object, object]):
    __slots__ = "member_types", "unknown_interface"
    if TYPE_CHECKING:
        member_types: dict[TypeSpec, TransportInterface]
        unknown_interface: "UnknownInterface"

    def __init__(self, interface_type: UnionType,
                 value_type: UnionType,
                 field: Optional[Field] = None):
        super().__init__(interface_type, value_type, UNIONTYPE, field=field)
        if __debug__:
            if not is_union_type(interface_type):
                raise AssertionError("Not a Union type", interface_type)
        members = dict()
        label = str(self)
        for arg in get_args(interface_type):
            if arg is not NONETYPE:
                it = get_type_interface(arg, label, field=field)
                members[arg] = it
        self.member_types = members
        self.unknown_interface = UnknownInterface(
            object, object, object, field)

    def from_json_parsed(self, value: object) -> object:
        for it in self.member_types.values():
            if it.can_parse(value):
                return it.from_json_parsed(value)
        return self.unknown_interface.from_json_parsed(value)

    def to_json_parsed(self, instance: object) -> object:
        for it in self.member_types.values():
            if it.can_parse(instance):
                return it.to_json_parsed(instance)
        return self.unknown_interface.to_json_parsed(instance)


class ValueInterface(TransportInterface[Ti, Ti], Generic[Ti]):
    def from_json_parsed(self, value: Ti) -> Ti:
        cls = self.interface_class
        if value.__class__ is cls:
            return value
        else:
            return cls(value)

    def to_json_parsed(self, instance: Ti) -> Ti:
        return instance


class StrInterface(ValueInterface[str]):
    def from_json_parsed(self, value: str) -> str:
        return value

    def to_json_parsed(self, instance: str) -> str:
        return instance

##  unused in this API
# class BytesInterface(TransportInterface[str, bytes]):
#     def from_json_parsed(self, value: str) -> bytes:
#         return value.encode()
#
#     def to_json_parsed(self, instance: bytes) -> str:
#         return instance.decode()


class IntInterface(ValueInterface[int]):
    def from_json_parsed(self, value: int) -> int:
        return value

    def to_json_parsed(self, instance: int) -> int:
        return instance


class FloatInterface(TransportInterface[float, float]):
    # note: using ujson
    # see https://github.com/ultrajson/ultrajson/issues/371
    def from_json_parsed(self, value: float) -> Decimal:
        return value

    def to_json_parsed(self, instance: float) -> float:
        return instance


class BoolInterface(ValueInterface[bool]):
    def from_json_parsed(self, value: Union[bool, str]) -> bool:
        return bool(value)

    def to_json_parsed(self, instance: bool) -> str:
        return str(instance)


class DatetimeInterface(TransportInterface[str, datetime]):
    def from_json_parsed(self, value: str) -> Optional[datetime]:
        if value is None:
            return None
        try:
            # this may discard any fractional seconds,
            # but should retain any timezone ...
            return datetime.fromisoformat(value)
        except ValueError:
            pass
        # this will discard any timezone, however encoded in the value
        dt = np.datetime64(value, "ns")
        return datetime.fromtimestamp(dt.astype("int64"))

    def to_json_parsed(self, instance: datetime) -> str:
        return instance.isoformat()


VALUE_TYPES.update({
    str: StrInterface,
    int: IntInterface,
    float: FloatInterface,
    bool: BoolInterface,
    datetime: DatetimeInterface
})


class SeriesInterface(TransportInterface[Ts, Ts], Generic[Ts]):
    __slots__ = "element_iface",

    if TYPE_CHECKING:
        element_iface: TransportInterface

    def __init__(self, interface_type: type[Ts],
                 element_iface: TransportInterface,
                 field: Optional[Field] = None):
        super().__init__(interface_type, interface_type, interface_type, field)
        self.element_iface = element_iface

    def from_json_parsed(self, value: Ts) -> Ts:
        ef = self.element_iface
        gen = (ef.from_json_parsed(elt) for elt in value)
        return self.interface_type(gen)

    def to_json_parsed(self, instance: Ts) -> Ts:
        ef = self.element_iface
        gen = (ef.to_json_parsed(elt) for elt in instance)
        return self.interface_type(gen)


class EnumInterface(TransportInterface[str, Te], Generic[Te]):
    # ecoding: Generally, use the name of the enum member
    #
    # in all cases in this API, the name of the API enum member
    # would be equal to the value of the same
    #
    def __init__(self, value_type: type[Te], field: Optional[Field] = None):
        super().__init__(str, value_type, value_type, field)

    def from_json_parsed(self, value: str) -> Union[Te, str]:
        if value.__class__ is str:
            return self.value_type._value2member_map_[value]
        else:
            return value

    def to_json_parsed(self, instance: Union[str, Te]) -> str:
        if instance.__class__ is str:
            return instance
        elif isinstance(instance, Enum):
            return instance.value
        else:
            return str(instance)


class UnknownInterface(TransportInterface[object, object]):
    def __init__(self, interface_type: Union[type, TypeAlias],
                 value_type: Union[type, TypeAlias],
                 interface_class: Optional[type] = None, field: Optional[Field] = None):
        super().__init__(interface_type, value_type, interface_class, field)

    def from_json_parsed(self, value: object) -> object:
        return value

    def to_json_parsed(self, instance: object) -> object:
        return instance


class UnknownTypeClass(ValueError):
    pass


# ModelInterface: see api_object.py
