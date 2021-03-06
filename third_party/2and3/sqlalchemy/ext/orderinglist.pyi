# Stubs for sqlalchemy.ext.orderinglist (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def ordering_list(attr, count_from: Optional[Any] = ..., **kw): ...

class OrderingList(list):
    ordering_attr = ...  # type: Any
    ordering_func = ...  # type: Any
    reorder_on_append = ...  # type: Any
    def __init__(self, ordering_attr: Optional[Any] = ..., ordering_func: Optional[Any] = ..., reorder_on_append: bool = ...) -> None: ...
    def reorder(self): ...
    def append(self, entity): ...
    def insert(self, index, entity): ...
    def remove(self, entity): ...
    def pop(self, index: int = ...): ...
    def __setitem__(self, index, entity): ...
    def __delitem__(self, index): ...
    def __setslice__(self, start, end, values): ...
    def __delslice__(self, start, end): ...
    def __reduce__(self): ...
