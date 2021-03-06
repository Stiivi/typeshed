# Stubs for sqlalchemy.dialects.sybase.mxodbc (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from sqlalchemy.dialects.sybase.base import SybaseDialect
from sqlalchemy.dialects.sybase.base import SybaseExecutionContext
from sqlalchemy.connectors.mxodbc import MxODBCConnector

class SybaseExecutionContext_mxodbc(SybaseExecutionContext): ...

class SybaseDialect_mxodbc(MxODBCConnector, SybaseDialect):
    execution_ctx_cls = ...  # type: Any

dialect = ...  # type: Any
