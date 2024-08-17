

from typing import Any, ClassVar, Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing import Optional
from pynwsdata.api_object import ApiObject, ApiField
from typing_extensions import Self


class Glossary200ResponseGlossaryInner(ApiObject):
    """
    Glossary200ResponseGlossaryInner
    """

    term: Optional[str] = ApiField(default=None, description="""The term being defined""")
