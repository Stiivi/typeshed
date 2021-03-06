# Stubs for sqlalchemy.orm.base (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .. import exc as sa_exc
from ..sql import expression as expression

PASSIVE_NO_RESULT = ...  # type: Any
ATTR_WAS_SET = ...  # type: Any
ATTR_EMPTY = ...  # type: Any
NO_VALUE = ...  # type: Any
NEVER_SET = ...  # type: Any
NO_CHANGE = ...  # type: Any
CALLABLES_OK = ...  # type: Any
SQL_OK = ...  # type: Any
RELATED_OBJECT_OK = ...  # type: Any
INIT_OK = ...  # type: Any
NON_PERSISTENT_OK = ...  # type: Any
LOAD_AGAINST_COMMITTED = ...  # type: Any
NO_AUTOFLUSH = ...  # type: Any
PASSIVE_OFF = ...  # type: Any
PASSIVE_RETURN_NEVER_SET = ...  # type: Any
PASSIVE_NO_INITIALIZE = ...  # type: Any
PASSIVE_NO_FETCH = ...  # type: Any
PASSIVE_NO_FETCH_RELATED = ...  # type: Any
PASSIVE_ONLY_PERSISTENT = ...  # type: Any
DEFAULT_MANAGER_ATTR = ...  # type: str
DEFAULT_STATE_ATTR = ...  # type: str
EXT_CONTINUE = ...  # type: Any
EXT_STOP = ...  # type: Any
ONETOMANY = ...  # type: Any
MANYTOONE = ...  # type: Any
MANYTOMANY = ...  # type: Any
NOT_EXTENSION = ...  # type: Any

def manager_of_class(cls): ...

instance_state = ...  # type: Any
instance_dict = ...  # type: Any

def instance_str(instance): ...
def state_str(state): ...
def state_class_str(state): ...
def attribute_str(instance, attribute): ...
def state_attribute_str(state, attribute): ...
def object_mapper(instance): ...
def object_state(instance): ...
def class_mapper(class_, configure: bool = ...): ...

class InspectionAttr(object):
    is_selectable = ...  # type: bool
    is_aliased_class = ...  # type: bool
    is_instance = ...  # type: bool
    is_mapper = ...  # type: bool
    is_property = ...  # type: bool
    is_attribute = ...  # type: bool
    is_clause_element = ...  # type: bool
    extension_type = ...  # type: Any

class InspectionAttrInfo(InspectionAttr):
    def info(self): ...

class _MappedAttribute(object): ...
