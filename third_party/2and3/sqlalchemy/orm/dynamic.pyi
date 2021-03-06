# Stubs for sqlalchemy.orm.dynamic (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from . import strategies
from . import attributes
from ..sql import operators as operators
from . import util as orm_util, exc as orm_exc
from .query import Query as Query

class DynaLoader(strategies.AbstractRelationshipLoader):
    is_class_level = ...  # type: bool
    def init_class_attribute(self, mapper): ...

class DynamicAttributeImpl(attributes.AttributeImpl):
    uses_objects = ...  # type: bool
    accepts_scalar_loader = ...  # type: bool
    supports_population = ...  # type: bool
    collection = ...  # type: bool
    target_mapper = ...  # type: Any
    order_by = ...  # type: Any
    query_class = ...  # type: Any
    def __init__(self, class_, key, typecallable, dispatch, target_mapper, order_by, query_class: Optional[Any] = ..., **kw) -> None: ...
    def get(self, state, dict_, passive: Any = ...): ...
    def get_collection(self, state, dict_, user_data: Optional[Any] = ..., passive: Any = ...): ...
    def fire_append_event(self, state, dict_, value, initiator, collection_history: Optional[Any] = ...): ...
    def fire_remove_event(self, state, dict_, value, initiator, collection_history: Optional[Any] = ...): ...
    def set(self, state, dict_, value, initiator: Optional[Any] = ..., passive: Any = ..., check_old: Optional[Any] = ..., pop: bool = ..., _adapt: bool = ...): ...
    def delete(self, *args, **kwargs): ...
    def set_committed_value(self, state, dict_, value): ...
    def get_history(self, state, dict_, passive: Any = ...): ...
    def get_all_pending(self, state, dict_, passive: Any = ...): ...
    def append(self, state, dict_, value, initiator, passive: Any = ...): ...
    def remove(self, state, dict_, value, initiator, passive: Any = ...): ...
    def pop(self, state, dict_, value, initiator, passive: Any = ...): ...

class AppenderMixin(object):
    query_class = ...  # type: Any
    instance = ...  # type: Any
    attr = ...  # type: Any
    def __init__(self, attr, state) -> None: ...
    session = ...  # type: Any
    def __iter__(self): ...
    def __getitem__(self, index): ...
    def count(self): ...
    def extend(self, iterator): ...
    def append(self, item): ...
    def remove(self, item): ...

class AppenderQuery(AppenderMixin, Query): ...

def mixin_user_query(cls): ...

class CollectionHistory(object):
    unchanged_items = ...  # type: Any
    added_items = ...  # type: Any
    deleted_items = ...  # type: Any
    def __init__(self, attr, state, apply_to: Optional[Any] = ...) -> None: ...
    @property
    def added_plus_unchanged(self): ...
    @property
    def all_items(self): ...
    def as_history(self): ...
    def indexed(self, index): ...
    def add_added(self, value): ...
    def add_removed(self, value): ...
