from typing import TypeVar, Dict, List, Type, ParamSpec, Optional, Callable, Iterator

T = TypeVar("T")
P = ParamSpec("P")
_INSTANCES: Dict[Type[T], List[T]] = dict()


class InstanceCollector:
    @staticmethod
    def collect(
            cls: Callable[P, Type[T]],
            # filter_fn: Optional[Callable[P, bool]] = None,
    ) -> Type[T]:
        """
        Decorator to collect instances of a class and store them.
        """

        def wrapper(cls, *args: P.args, **kwargs: P.kwargs) -> T:
            """
            Override the creation of instances.

            :return: New instance of the class.
            """
            instance: T = object.__new__(cls)
            instance.__init__(*args, **kwargs)
            if cls not in _INSTANCES:
                _INSTANCES[cls] = []
            _INSTANCES[cls].append(instance)
            return instance

        cls.__new__ = wrapper

        return cls

    @staticmethod
    def iter(
            cls: Type[T],
            filter_fn: Optional[Callable[P, bool]] = None,
    ) -> Iterator[T]:
        """
        Iterate over instances of a class.

        :param cls: class to iterate over instances.
        :param filter_fn: Optional filter function to apply on instances.

        :return: Iterator yielding instances of the specified class.
        """
        for instance in _INSTANCES.get(cls, []):
            if filter_fn and not filter_fn(instance):
                continue

            yield instance


__all__ = ("InstanceCollector",)