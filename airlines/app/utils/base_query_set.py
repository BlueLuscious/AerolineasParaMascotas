from typing import TypeVar, Generic, Callable
T = TypeVar("T")


class BaseQuerySet(Generic[T]):
    def __init__(self, data: list[T]):
        self._data = data

    def filter(self, **criteria: Callable[[T], bool]) -> "BaseQuerySet":
        result = self._data
        for attr, value in criteria.items():
            result = [obj for obj in result if getattr(obj, attr, None) == value]
        return self.__class__(result)

    def all(self):
        return self._data

    def first(self):
        return self._data[0] if self._data else None

    def last(self):
        return self._data[-1] if self._data else None

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)
