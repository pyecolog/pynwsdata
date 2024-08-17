

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from pynwsdata.models.glossary200_response_glossary_inner import Glossary200ResponseGlossaryInner
from pynwsdata.models.json_ld_context import JsonLdContext
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class Glossary200Response(ApiObject):
    """
    Glossary200Response
    """

    context: Optional[JsonLdContext] = ApiField(default=None, alias="@context")
    glossary: Optional[list[Glossary200ResponseGlossaryInner]] = ApiField(default=None, description="""A list of glossary terms""")


