# API model types

from aenum import StrEnum
from abc import ABC, ABCMeta
from collections.abc import Callable, Mapping
from importlib.util import find_spec, module_from_spec
from pyfields.core import (
    NativeField, EMPTY, UNKNOWN, Symbols, FieldError
)
import sys
from types import MappingProxyType
from typing import (
    cast, TYPE_CHECKING, Any, Annotated, Generic,
    Self, ClassVar, TypeVar, Literal, Optional, Union,
    TypeAlias
)
from typing_extensions import (
    dataclass_transform,
    get_args, get_origin,
    get_type_hints
)
from warnings import warn

from pynwsdata.api_base import (
    Ti, To, DEFERRED, TransportInterface, NONETYPE,
    get_type_interface
)

if TYPE_CHECKING:
    from pynwsdata.models.pagination_info import PaginationInfo


EMPTY_MAP: Mapping[str, Any] = MappingProxyType(dict())

Tm = TypeVar("Tm", bound="ApiObject")


class UnboundField(FieldError):
    pass


class ApiConst(StrEnum):
    NULL = "null"
    TYPE = "type"


class Constraint(StrEnum):
    GE = "ge"
    LE = "le"
    GT = "gt"
    MIN_LENGTH = "min_length"


class ApiField(NativeField, Generic[Tm, Ti, To]):
    # pyfields.Field subclass for ApiObject
    #
    # Overview:
    #
    # - Field subclass defined after Pydantic integration in the
    #   original generated sources
    #
    # - portable with the sources produced with OpenAPI Generator
    #
    # - no immediate field validation
    #
    # Implementation Notes:
    #
    # - server response fields are trusted to be valid at source
    #   and after processing
    #
    # - client request fields are expected to be valid in implementation
    #
    # - field constraints from the generated sources have been retained,
    #   where present in the original generated sources

    __slots__ = "alias", "constraints", "interface", "interface_type", "can_encode"

    if TYPE_CHECKING:
        alias: str
        constraints: Mapping[str, Any]
        interface: TransportInterface[Ti, To]
        interface_type: Optional[type] # ? FIXME rename => parse_type

    def get_field_interface(self, type_hint: Any,
                            label: Optional[str] = None,
                            field: Union[Self, Symbols.UNKNOWN] = UNKNOWN) -> TransportInterface[Ti, To]:
        try:
            # override the type hint if self.interface_type is bound
            ityp = self.interface_type
        except AttributeError:
            ityp = type_hint

        label: str = self.field_id if label is None else label
        if field is UNKNOWN:
            field = self
        elif field is EMPTY:
            field = None

        return get_type_interface(ityp, label, field=field)

    def bind_interface(self) -> TransportInterface[Ti, To]:
        try:
            return self.interface
        except AttributeError:
            pass
        ocls = self.owner_cls
        if isinstance(ocls, type):
            ocls = ocls.__name__
        impl = self.get_field_interface(self.type_hint)
        self.interface = impl
        return impl

    def field_is_set(self, instance: To) -> bool:
        try:
            return instance.__dict__[self.name]
        except KeyError:
            return False
        else:
            return True

    def field_can_encode(self, instance: To) -> bool:
        return self.can_encode

    def __init__(self, default: Union[To, Symbols.EMPTY] = EMPTY, *,
                 default_factory: Optional[Callable[[Tm], To]] = None,
                 type_hint: Any = EMPTY,
                 interface_type: Optional[type] = None,
                 interface: Optional[TransportInterface[Ti, To]] = None,
                 can_encode: bool = True,
                 description: Optional[str] = None,
                 alias: Optional[str] = None,
                 ge: Optional[int] = None,
                 gt: Optional[int] = None,
                 le: Optional[int] = None,
                 min_length: Optional[int] = None,
                 ):
        super().__init__(default, default_factory, type_hint, UNKNOWN, description)
        self.can_encode = can_encode
        if interface_type is not None:
            self.interface_type = interface_type
        if interface is not None:
            self.interface = interface
        if alias is not None:
            self.alias = alias
        # constraints
        # - parameters for request linting
        # - constraints processed from the openapi.json file
        constraints = dict()
        if ge is not None:
            constraints[Constraint.GE] = ge
        if gt is not None:
            constraints[Constraint.GT] = gt
        if le is not None:
            constraints[Constraint.LE] = le
        if min_length is not None:
            constraints[Constraint.MIN_LENGTH] = min_length

        if constraints:
            self.constraints = MappingProxyType(constraints)
        else:
            self.constraints = EMPTY_MAP

        # if type_hint is not EMPTY:
        #     self.bind_implementation(type_hint)

    @property
    def field_id(self) -> str:
        owner_cls = self.owner_cls
        if isinstance(owner_cls, type):
            clsname = owner_cls.__name__
        else:
            clsname = str(owner_cls)
        slname = self.name
        return ".".join((clsname, slname))

    def __set_name__(self, scope: type[To], name: str):
        name = sys.intern(name)
        if get_origin(scope.__annotations__.get(name, None)) is ClassVar:
            return
        super().__set_name__(scope, name)
        # set nonable, assuming self.type hint
        # will now be avaialble
        th = self.type_hint
        if self.nonable is Symbols.UNKNOWN:
            th_origin = get_origin(th)
            self.nonable = th_origin is Union and NONETYPE in get_args(th)
        # set alias if not initialized
        try:
            self.alias
        except AttributeError:
            self.alias = self.name
        # update name and scope attrs
        if self.name is None:
            self.name = name
        if self.owner_cls is None:
            self.owner_cls = scope
        # ensure self.interface is initialized
        try:
            self.interface
        except AttributeError:
            pass
        else:
            return
        if th is None or th is EMPTY:
            warn(UserWarning("%s: No type hint" % self.field_id), stacklevel=3)
        else:
            try:
                icls = self.interface_type
            except AttributeError:
                icls = None
            if icls is None and isinstance(th, type):
                self.interface_type = th
            if __debug__:
                origin = get_origin(th)
                if origin is ClassVar:
                    warn(UserWarning("%s: Field initialized for ClassVar" %
                         self.field_id, th))
            self.bind_interface()

    def __set__(self, instance: Tm, value: To):
        vars(instance)[self.name] = value

    def __delete__(self, instance) -> Union[To, Literal[Symbols.UNKNOWN]]:
        return vars(instance).pop(self.name, UNKNOWN)

    def require_value(self, instance: Tm) -> To:
        try:
            return vars(instance)[self.name]
        except KeyError:
            raise UnboundField(self, instance)

    def set_from_json_parsed(self, parsed: Ti, instance: Tm):
        value = self.interface.from_json_parsed(parsed)
        self.__set__(instance, value)

    def get_to_json_parsed(self, instance: Tm) -> Ti:
        value = self.__get__(instance, instance.__class__)
        return self.interface.to_json_parsed(value)


class ApiType(ABCMeta):
    #
    # metaclass for ApiObject
    #

    if TYPE_CHECKING:
        fields: dict[str, ApiField]
        alias_fields: dict[str, ApiField]

    def __new__(mcls, clsname: str, bases: tuple[type, ...], ns: dict[str, Any]):
        try:
            annotations = ns["__annotations__"]
        except KeyError:
            pass
        else:
            for aname, ahint in annotations.items():
                if aname.startswith("_"):
                    continue
                origin = get_origin(ahint)
                if origin is not ClassVar:
                    try:
                        aval = ns[aname]
                    except KeyError:
                        aval = EMPTY

                    if not isinstance(aval, ApiField) or aval is EMPTY:
                        if origin is Annotated:
                            ahint, afield = get_args(aval)
                            afield.type_hint = ahint
                        else:
                            afield = ApiField(aval, type_hint=ahint)
                        ns[aname] = afield

        new_cls = super().__new__(mcls, clsname, bases, ns)
        annot = get_type_hints(new_cls)

        fields = dict()
        for aname, aval in vars(new_cls).items():
            if isinstance(aval, ApiField):
                th_base = annot.get(aname, None)
                # avoid re-adding any field aliased with a ClassVar
                # in the defining class, e.g join_field in PagedApiObject
                if get_origin(th_base) is not ClassVar:
                    fields[aname] = aval
        new_cls.fields = fields
        new_cls.alias_fields = {sys.intern(
            field.alias): field for field in fields.values()}

        API_TYPES[sys.intern(clsname)] = new_cls

        return new_cls


API_TYPES: dict[str, ApiType] = dict()
BASE_API_TYPES: frozenset[str] = frozenset(("ApiObject", "AbstractApiObject", "PagedApiObject"))

@dataclass_transform(kw_only_default=True)
class ApiObject(ABC, metaclass=ApiType):
    __slots__ = "unmapped_fields"

    #
    # Base class for API interface objects
    #
    # This class provides initialization and general protocol methods
    # for JSON-serialized API objects

    if TYPE_CHECKING:
        fields: ClassVar[dict[str, ApiField]]
        alias_fields: ClassVar[dict[str, ApiField]]
        model_interface: ClassVar["ModelInterface[Self]"]
        # overflow for field names without a representation in
        # cls.fields / cls.alias_fields
        #
        # This would probably denote an issue in the type modeling
        # for this API
        #
        # Pursuant to futher testing, this attribute will receive
        # any effecive field names not implemented in the defining
        # class.
        #
        # this attribute is not initilalized until used for
        # storing any field name. see also: get_unmapped_fields()
        unmapped_fields: set[str]

    def get_unmapped_fields(self) -> set[str]:
        # deferred initialization for self.unmapped_fields
        try:
            return self.unmapped_fields
        except AttributeError:
            pass
        fieldset = set()
        self.unmapped_fields = fieldset
        return fieldset

    def __init__(self, **kw) -> None:
        if kw:
            cls = cast(type[Self], self.__class__)
            fields = cls.fields
            for name, val in kw.items():
                try:
                    field = fields[sys.intern(name)]
                except KeyError:
                    warn(UserWarning("Unknown field name for class", name, cls.__name__),
                         stacklevel=2)
                else:

                    field.__set__(self, val)

    @classmethod
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        if cls.__name__ not in BASE_API_TYPES:
            try:
                interface = cls.model_interface
            except AttributeError:
                pass
            else:
                return
            interface = cls.create_model_interface()
            cls.model_interface = interface

    @classmethod
    def create_model_interface(cls) -> "ModelInterface[Self]":
        return get_type_interface(cls, cls.__name__)

    @staticmethod
    def intern(value: str) -> str:
        # convenience method
        return sys.intern(value)

    @classmethod
    def from_json_parsed(cls, values: dict[str, Any]) -> Self:
        fields = cls.alias_fields
        inst = cls()
        if isinstance(values, list):
            if __debug__:
                n_elts = len(values)
            values = dict([values])
            if __debug__:
                # a precaution for the shortcut:
                # ensure the dict parse of the list
                # provides all of the values from the
                # original list
                assert n_elts / 2 == len(values)

        for name, value in values.items():
            try:
                field = fields[name]
            except KeyError:
                if __debug__:
                    warn(UserWarning("Unknown field: %s.%s" %
                         (cls.__name__, name)), stacklevel=2)
                setattr(inst, name, value)
                inst.get_unmapped_fields().add(name)
                continue
            as_value = field.interface.from_json_parsed(value)
            if as_value is None:
                continue
            field.__set__(inst, as_value)
        return inst

    def to_json_parsed(self) -> dict[str, Any]:
        fields = self.fields
        out = dict()
        cls = self.__class__
        for name, field in fields.items():
            if field.field_is_set(self) and field.field_can_encode(self):
                out[name] = field.__get__(self, cls)

        try:
            unmapped = self.unmapped_fields
        except AttributeError:
            unmapped = None
        if unmapped:
            out.update(unmapped)
        return out


    def __repr__(self):
        clsname = self.__class__.__name__
        vals = dict()
        for name, field in self.fields.items():
            try:
                vals[name] = field.require_value(self)
            except UnboundField:
                continue
        return "%s(%s)" % (clsname, ", ".join(map(lambda elt: "%s=..." % elt, vals.keys())))

    def to_str(self) -> str:
        clsname = self.__class__.__name__
        vals = dict()
        for name, field in self.fields.items():
            try:
                vals[name] = field.require_value(self)
            except UnboundField:
                continue
        return "%s(%s)" % (clsname, ", ".join(map(lambda elt: "%s=%r" % elt, vals.keys())))

    @classmethod
    def from_json_str(cls, json_str: str) -> Self:
        # overridden in JsonLdcontext
        return cls.model_interface.from_json_str(json_str)

    def to_json_str(self) -> str:
        # overridden in JsonLdcontext
        return self.model_interface.to_json_str(self)


# mapping of string 'Type' codes to (class, module) names
#
# This type appears in a Classvar attribute for each
# AbstractApiObject type. The values in the mapping
# will denote the subclass for each corresponding,
# string 'type' code. The mapping is used mainly
# for intializing and registering each subclass,
# when not previously initialized through module
# imports
SubtypeMap: TypeAlias = dict[str, tuple[str, str]]

class AbstractApiType(ApiType):
    if TYPE_CHECKING:
        base_type: Self

    def __new__(mcls, clsname: str, bases: tuple[type, ...], ns: dict[str, Any]):
        new_cls = super().__new__(mcls, clsname, bases, ns)
        try:
            abstract_base = AbstractApiObject
        except NameError:
            # probably initializing AbstractApiObject, here
            return new_cls
        #
        # if AbstractApiObject is in the class bases, it's assumed
        # that the class is an abstract base class
        #
        if abstract_base in bases:
            new_cls.base_type = new_cls
        return new_cls

class AbstractApiObject(ApiObject, metaclass=AbstractApiType):
    if TYPE_CHECKING:
        base_type: ClassVar[type[Self]]
        # type_code: class-scoped representation for the value
        # from the 'type' property of each implementation class,
        # referencing the original openapi.yaml
        type_code: ClassVar[str]

    # an effective enumeration of implementing classes,
    # once initialized
    subtypes: ClassVar[dict[str, type[Self]]] = dict()

    # mapping from 'type' strings to class names and submodules of __package__
    #
    # see notes for the SubtypeMap type alias
    #
    subtype_map: ClassVar[SubtypeMap]

    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        try:
            tc = cls.type_code
        except AttributeError:
            pass
        else:
            tc = sys.intern(tc)
            cls.type_code = tc
            cls.base_type.subtypes[tc] = cls

    @classmethod
    def get_subtype(cls, type_code: str) -> type[Self]:
        try:
            return cls.subtypes[sys.intern(type_code)]
        except KeyError:
            pass

        try:
            clsname, submodule = cls.base_type.subtype_map[type_code]
        except KeyError:
            raise ValueError("Unrecognized subtype", type_code, cls)

        # deferred import
        pkg = cls.__module__.rsplit(".", 1)[0]
        mname = ".".join((pkg, submodule))
        spec = find_spec(mname)
        if spec is None:
            raise RuntimeError("Submodule not found", mname, type_code)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        clsname = sys.intern(clsname)
        scls = getattr(module, clsname)
        cls.subtypes[clsname] = scls
        return scls


    @classmethod
    def from_json_parsed(cls, mapping: dict[str, Any]) -> Self:
        if cls is cls.base_type:
            # locate the matching subclass, from any
            # 'type' value in the mapping
            try:
                tc: str = mapping[ApiConst.TYPE]
            except KeyError:
                raise ValueError("Type code not provided",
                                 mapping, cls) from None

            subcls = cls.get_subtype(tc)
            # create and return an instance of the
            # matching subclass
            return subcls.from_json_parsed(mapping)
        else:
            # called from a subclass of the abstract
            # base class
            return super().from_json_parsed(mapping)


class ModelInterface(TransportInterface[dict, Tm], Generic[Tm]):
    def __init__(self, model_type: type[Tm], field: Optional[ApiField] = None):
        super().__init__(dict[str, Any], model_type, model_type, field)

    def from_json_parsed(self, values: Union[list, dict[str, Any], None]) -> Tm:
        if values:
            return self.interface_class.from_json_parsed(values)

    def to_json_parsed(self, inst: Tm) -> dict:
        return inst.to_json_parsed()

# initialize attributes of the deferred singleton
DEFERRED.API_OBJECT = ApiObject
DEFERRED.MODEL_INTERFACE = ModelInterface


class PagedApiObject(ApiObject):
    if TYPE_CHECKING:
        # e.g AlertCollectionGeoJson.features
        pagination: Optional[PaginationInfo]
        join_field: ClassVar[ApiField]
