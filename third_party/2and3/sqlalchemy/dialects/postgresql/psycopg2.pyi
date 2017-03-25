# Stubs for sqlalchemy.dialects.postgresql.psycopg2 (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ...engine import result as _result
from ...sql import expression as expression
from ... import types as sqltypes
from .base import PGDialect as PGDialect, PGCompiler as PGCompiler, PGIdentifierPreparer as PGIdentifierPreparer, PGExecutionContext as PGExecutionContext, ENUM as ENUM, UUID as UUID
from .hstore import HSTORE as HSTORE
from .json import JSON as JSON, JSONB as JSONB
from uuid import UUID as _python_UUID

logger = ...  # type: Any

class _PGNumeric(sqltypes.Numeric):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _PGEnum(ENUM):
    convert_unicode = ...  # type: str
    def result_processor(self, dialect, coltype): ...

class _PGHStore(HSTORE):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class _PGJSON(JSON):
    def result_processor(self, dialect, coltype): ...

class _PGJSONB(JSONB):
    def result_processor(self, dialect, coltype): ...

class _PGUUID(UUID):
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...

class PGExecutionContext_psycopg2(PGExecutionContext):
    def create_server_side_cursor(self): ...
    def get_result_proxy(self): ...

class PGCompiler_psycopg2(PGCompiler):
    def visit_mod_binary(self, binary, operator, **kw): ...
    def post_process_text(self, text): ...

class PGIdentifierPreparer_psycopg2(PGIdentifierPreparer): ...

class PGDialect_psycopg2(PGDialect):
    driver = ...  # type: str
    supports_unicode_statements = ...  # type: bool
    supports_server_side_cursors = ...  # type: bool
    default_paramstyle = ...  # type: str
    supports_sane_multi_rowcount = ...  # type: bool
    execution_ctx_cls = ...  # type: Any
    statement_compiler = ...  # type: Any
    preparer = ...  # type: Any
    psycopg2_version = ...  # type: Any
    FEATURE_VERSION_MAP = ...  # type: Any
    engine_config_types = ...  # type: Any
    colspecs = ...  # type: Any
    server_side_cursors = ...  # type: Any
    use_native_unicode = ...  # type: Any
    use_native_hstore = ...  # type: Any
    use_native_uuid = ...  # type: Any
    supports_unicode_binds = ...  # type: Any
    client_encoding = ...  # type: Any
    def __init__(self, server_side_cursors: bool = ..., use_native_unicode: bool = ..., client_encoding: Optional[Any] = ..., use_native_hstore: bool = ..., use_native_uuid: bool = ..., **kwargs) -> None: ...
    def initialize(self, connection): ...
    @classmethod
    def dbapi(cls): ...
    def set_isolation_level(self, connection, level): ...
    def on_connect(self): ...
    def create_connect_args(self, url): ...
    def is_disconnect(self, e, connection, cursor): ...

dialect = ...  # type: Any