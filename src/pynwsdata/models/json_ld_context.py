
import ujson
from typing import Any, Union, Self
from pynwsdata.api_object import ApiObject, ApiConst

# JSONLDCONTEXT_ANY_OF_SCHEMAS = ["list[object]", "object"]

class JsonLdContext(ApiObject):
    """
    JsonLdContext
    """

    # hybrid of a namespace mapping and an RDF graph, approximately
    #
    # data field is not present in the original API specification
    data: dict[str, dict[str, str]]


    @classmethod
    def from_json_str(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        return cls.from_json_parsed(ujson.loads(json_str))

    @classmethod
    def from_json_parsed(cls, values: Union[list, dict[str, Any]]) -> Self:
        if isinstance(values, list):
            # most common, for how the server is encoding this object in responses
            if __debug__:
                n_elts = len(values)
            data = dict([values])
            if __debug__:
                assert n_elts / 2 == len(data)
            return cls(data = data)
        else:
            return super().from_json_parsed(values)

    def to_json_parsed(self):
        return self.data


    def to_json_str(self) -> str:
        """Returns the JSON representation of the actual instance"""
        try:
            data = self.data
        except AttributeError:
            return ApiConst.NULL
        else:
            return ujson.dumps(data, ensure_ascii=False)
