# Stubs for sqlalchemy.dialects.postgresql.json (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ... import types as sqltypes

class JSONPathType(sqltypes.JSON.JSONPathType):
    def bind_processor(self, dialect): ...
    def literal_processor(self, dialect): ...

class JSON(sqltypes.JSON):
    astext_type = ...  # type: Any
    def __init__(self, none_as_null: bool = ..., astext_type: Optional[Any] = ...) -> None: ...
    class Comparator(sqltypes.JSON.Comparator):
        @property
        def astext(self): ...
    comparator_factory = ...  # type: Any

class JSONB(JSON):
    __visit_name__ = ...  # type: str
    class Comparator(JSON.Comparator):
        def has_key(self, other): ...
        def has_all(self, other): ...
        def has_any(self, other): ...
        def contains(self, other, **kwargs): ...
        def contained_by(self, other): ...
    comparator_factory = ...  # type: Any
