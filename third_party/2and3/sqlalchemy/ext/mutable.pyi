# Stubs for sqlalchemy.ext.mutable (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..orm.attributes import flag_modified as flag_modified
from ..orm import mapper as mapper, object_mapper as object_mapper, Mapper as Mapper
from ..util import memoized_property as memoized_property

class MutableBase(object):
    @classmethod
    def coerce(cls, key, value): ...

class Mutable(MutableBase):
    def changed(self): ...
    @classmethod
    def associate_with_attribute(cls, attribute): ...
    @classmethod
    def associate_with(cls, sqltype): ...
    @classmethod
    def as_mutable(cls, sqltype): ...

class MutableComposite(MutableBase):
    def changed(self): ...

class MutableDict(Mutable, dict):
    def __setitem__(self, key, value): ...
    def setdefault(self, key, value): ...
    def __delitem__(self, key): ...
    def update(self, *a, **kw): ...
    def pop(self, *arg): ...
    def popitem(self): ...
    def clear(self): ...
    @classmethod
    def coerce(cls, key, value): ...

class MutableList(Mutable, list):
    def __setitem__(self, index, value): ...
    def __setslice__(self, start, end, value): ...
    def __delitem__(self, index): ...
    def __delslice__(self, start, end): ...
    def pop(self, *arg): ...
    def append(self, x): ...
    def extend(self, x): ...
    def insert(self, i, x): ...
    def remove(self, i): ...
    def clear(self): ...
    def sort(self): ...
    def reverse(self): ...
    @classmethod
    def coerce(cls, index, value): ...

class MutableSet(Mutable, set):
    def update(self, *arg): ...
    def intersection_update(self, *arg): ...
    def difference_update(self, *arg): ...
    def symmetric_difference_update(self, *arg): ...
    def add(self, elem): ...
    def remove(self, elem): ...
    def discard(self, elem): ...
    def pop(self, *arg): ...
    def clear(self): ...
    @classmethod
    def coerce(cls, index, value): ...
    def __reduce_ex__(self, proto): ...
