# Stubs for sqlalchemy.dialects.firebird.kinterbasdb (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .base import FBDialect as FBDialect, FBExecutionContext as FBExecutionContext
from ... import types as sqltypes

class _kinterbasdb_numeric(object):
    def bind_processor(self, dialect): ...

class _FBNumeric_kinterbasdb(_kinterbasdb_numeric, sqltypes.Numeric): ...
class _FBFloat_kinterbasdb(_kinterbasdb_numeric, sqltypes.Float): ...

class FBExecutionContext_kinterbasdb(FBExecutionContext):
    @property
    def rowcount(self): ...

class FBDialect_kinterbasdb(FBDialect):
    driver = ...  # type: str
    supports_sane_rowcount = ...  # type: bool
    supports_sane_multi_rowcount = ...  # type: bool
    execution_ctx_cls = ...  # type: Any
    supports_native_decimal = ...  # type: bool
    colspecs = ...  # type: Any
    enable_rowcount = ...  # type: Any
    type_conv = ...  # type: Any
    concurrency_level = ...  # type: Any
    retaining = ...  # type: Any
    def __init__(self, type_conv: int = ..., concurrency_level: int = ..., enable_rowcount: bool = ..., retaining: bool = ..., **kwargs) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def do_execute(self, cursor, statement, parameters, context: Optional[Any] = ...): ...
    def do_rollback(self, dbapi_connection): ...
    def do_commit(self, dbapi_connection): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect = ...  # type: Any