"""
See https://docs.python.org/3/library/typing.html for more information.

GENERICS:
    -Since type information about objects kept in containers cannot be statically inferred in a
    generic way, many container classes in the standard library support subscription to denote
    the expected types of container elements.
    -Generics is a mechanism with which you to define functions, classes, or methods that can
    operate on multiple types while maintaining type safety.
    -With the implementation of Generics it is possible to write reusable code that can be used
    with different data types.
    -Generics in Python are implemented using type hints.
"""

# Example of Python Generics with deque

from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.elements: deque[T] = deque()

    def push(self, element: T) -> None:
        self.elements.append(element)

    def pop(self) -> T:
        return self.elements.popleft()
