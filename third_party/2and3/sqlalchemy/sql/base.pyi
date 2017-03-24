# Stubs for sqlalchemy.sql.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import collections
from sqlalchemy import util
from .visitors import ClauseVisitor as ClauseVisitor

PARSE_AUTOCOMMIT = ...  # type: Any
NO_ARG = ...  # type: Any

class Immutable:
    def unique_params(self, *optionaldict, **kwargs): ...
    def params(self, *optionaldict, **kwargs): ...
    def _clone(self) -> Immutable: ...

class _DialectArgView(collections.MutableMapping):
    obj = ...  # type: Any
    def __init__(self, obj) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...
    def __len__(self): ...
    def __iter__(self): ...

class _DialectArgDict(collections.MutableMapping):
    def __init__(self) -> None: ...
    def __len__(self): ...
    def __iter__(self): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __delitem__(self, key): ...

class DialectKWArgs:
    @classmethod
    def argument_for(cls, dialect_name, argument_name, default): ...
    def dialect_kwargs(self): ...
    @property
    def kwargs(self): ...
    def dialect_options(self): ...

class Generative: ...

class Executable(Generative):
    supports_execution = ...  # type: bool
    def execution_options(self, **kw): ...
    def execute(self, *multiparams, **params): ...
    def scalar(self, *multiparams, **params): ...
    @property
    def bind(self): ...

class SchemaEventTarget: ...

class SchemaVisitor(ClauseVisitor):
    __traverse_options__ = ...  # type: Any

class ColumnCollection(util.OrderedProperties):
    def __init__(self, *columns) -> None: ...
    def replace(self, column): ...
    def add(self, column): ...
    def __delitem__(self, key): ...
    def __setattr__(self, key, object): ...
    def __setitem__(self, key, value): ...
    def clear(self): ...
    def remove(self, column): ...
    def update(self, iter): ...
    def extend(self, iter): ...
    __hash__ = ...  # type: Any
    def __eq__(self, elements, other): ...
    def __contains__(self, other): ...
    def contains_column(self, col): ...
    def as_immutable(self): ...

class ImmutableColumnCollection(util.ImmutableProperties, ColumnCollection):
    def __init__(self, data, all_columns) -> None: ...
    extend = ...  # type: Any
    remove = ...  # type: Any

class ColumnSet(util.ordered_column_set):
    def contains_column(self, col): ...
    def extend(self, cols): ...
    def __add__(self, other): ...
    def __eq__(self, elements, other): ...
    def __hash__(self): ...
