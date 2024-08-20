
import ujson
from pynwsdata.api_base import Enum, EnumInterface
from pynwsdata.models.alert_certainty import AlertCertainty
import pynwsdata.models.api


def verify_enum(etype: type[Enum]):
    obj = EnumInterface(etype)
    for name, val in etype._member_map_.items():
        from_parsed = obj.from_json_parsed(name)
        from_str = obj.from_json_str(ujson.dumps(name, ensure_ascii=False))
        assert from_str is from_parsed
        assert from_parsed is val

        as_str = obj.to_json_parsed(from_parsed)
        assert as_str == val.value
        as_json = obj.to_json_str(from_str)
        assert as_json == ujson.dumps(as_str, ensure_ascii=False)


# def test_once():
#     verify_enum(AlertCertainty)

def test_model_enums():
    for binding in vars(pynwsdata.models.api).values():
        if isinstance(binding, Enum):
            verify_enum(binding)


if __name__ == "__main__":
    # test_once()
    test_model_enums()
