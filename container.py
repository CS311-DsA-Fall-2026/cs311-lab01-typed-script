"""
Lab 1: The Typed Script -- TypedContainer starter.

Complete TypedContainer below. See the assignment, Part B,
for the full requirements. Do not rename the class or its methods --
test_container.py imports them by name.
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class TypedContainer(Generic[T]):
    """A strictly-typed key-value container. Keys must always be str."""

    def __init__(self) -> None:
        # TODO: set up your internal storage (e.g. a dict).
        raise NotImplementedError

    def set(self, key: str, value: T) -> None:
        """
        Store `value` under `key`.

        Must raise TypeError immediately if `key` is not a str --
        no silent coercion. See Part A, Question 3, for why.
        """
        # TODO
        raise NotImplementedError

    def get(self, key: str) -> T:
        """
        Return the value stored under `key`.

        Must raise TypeError immediately if `key` is not a str.
        """
        # TODO
        raise NotImplementedError

    def __contains__(self, key: str) -> bool:
        # TODO: support the `in` operator.
        raise NotImplementedError

    def __len__(self) -> int:
        # TODO: support len(container).
        raise NotImplementedError
