
from aenum import StrEnum, EnumType
from typing import cast, TYPE_CHECKING, Any, ClassVar, Self


class MetaApiEnum(EnumType):
    def __getitem__(self, key: str) -> Self:
        return self._members_[key]


class ApiEnum(StrEnum, metaclass=MetaApiEnum):
    if TYPE_CHECKING:
        value: str
        name: str
        _member_map_: ClassVar[dict[str, Self]]
        _value2member_map_: ClassVar[dict[str, Self]]

    def __hash__(self) -> int:
        try:
            return self._hash
        except AttributeError:
            pass
        _h = hash(self.value)
        self._hash = _h
        return _h

    def __eq__(self, value) -> bool:
        return hash(self) == hash(value)


class MetaCategoricalEnum(MetaApiEnum):
    _all_members_: dict[str, "CategoricalEnum"]

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self._all_members_ = self._member_map_.copy()

    def __getitem__(self, key: str) -> Self:
        return self._all_members_[key]

    def __getattr__(self, name: str) -> Any:
        try:
            return self[name]
        except KeyError:
            return super().__getattr__(name)


class CategoricalEnum(ApiEnum, metaclass=MetaCategoricalEnum):
    if TYPE_CHECKING:
        _all_members_: ClassVar[dict[str, Self]]

    @classmethod
    def __init_subclass__(cls) -> None:
        super().__init_subclass__()
        for base in cls.__bases__:
            if CategoricalEnum in base.__bases__:
                cast(CategoricalEnum, base)._all_members_.update(
                    cls._member_map_)


if __name__ == "__main__":
    #
    # ad hoc tests
    #

    class ApiTest(ApiEnum):
        A = "a"
        B = "b"

    class CatTest(CategoricalEnum):
        pass

    class CatTestA(CatTest):
        C = "c"
        D = "d"

    class CatTestB(CatTest):
        E = "e"
        F = "f"

    def test_api_enum():
        assert ApiTest.A == "a"
        assert ApiTest.B != ApiTest.A

    def test_cat_enum():
        assert CatTest.C is CatTestA.C
        assert CatTest.E is CatTestB.E
        assert CatTest['D'] is CatTest.D
        assert CatTest['F'] is CatTest.F

    test_api_enum()
    test_cat_enum()
