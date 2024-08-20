
from aenum import StrEnum, EnumType
from typing import cast, TYPE_CHECKING, Any, ClassVar, Self

from ecolog.util.const import StrConst, MetaConst


class ApiEnum(StrConst): pass

class MetaCategoricalEnum(MetaConst):
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
