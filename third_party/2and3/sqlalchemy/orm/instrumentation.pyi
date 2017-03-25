# Stubs for sqlalchemy.orm.instrumentation (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class ClassManager(dict):
    MANAGER_ATTR = ...  # type: Any
    STATE_ATTR = ...  # type: Any
    deferred_scalar_loader = ...  # type: Any
    original_init = ...  # type: Any
    factory = ...  # type: Any
    class_ = ...  # type: Any
    info = ...  # type: Any
    new_init = ...  # type: Any
    local_attrs = ...  # type: Any
    originals = ...  # type: Any
    def __init__(self, class_) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    @property
    def is_mapped(self): ...
    def manage(self): ...
    def dispose(self): ...
    def manager_getter(self): ...
    def state_getter(self): ...
    def dict_getter(self): ...
    def instrument_attribute(self, key, inst, propagated: bool = ...): ...
    def subclass_managers(self, recursive): ...
    def post_configure_attribute(self, key): ...
    def uninstrument_attribute(self, key, propagated: bool = ...): ...
    mapper = ...  # type: Any
    def unregister(self): ...
    def install_descriptor(self, key, inst): ...
    def uninstall_descriptor(self, key): ...
    def install_member(self, key, implementation): ...
    def uninstall_member(self, key): ...
    def instrument_collection_class(self, key, collection_class): ...
    def initialize_collection(self, key, state, factory): ...
    def is_instrumented(self, key, search: bool = ...): ...
    def get_impl(self, key): ...
    @property
    def attributes(self): ...
    def new_instance(self, state: Optional[Any] = ...): ...
    def setup_instance(self, instance, state: Optional[Any] = ...): ...
    def teardown_instance(self, instance): ...
    def has_state(self, instance): ...
    def has_parent(self, state, key, optimistic: bool = ...): ...
    def __bool__(self): ...
    __nonzero__ = ...  # type: Any

class _SerializeManager:
    class_ = ...  # type: Any
    def __init__(self, state, d) -> None: ...
    def __call__(self, state, inst, state_dict): ...

class InstrumentationFactory:
    def create_manager_for_cls(self, class_): ...
    def unregister(self, class_): ...

instance_state = ...  # type: Any

instance_dict = ...  # type: Any

manager_of_class = ...  # type: Any

def register_class(class_): ...
def unregister_class(class_): ...
def is_instrumented(instance, key): ...
