"""
Includes the Fact class and all sub-classes.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic


# Type hint types.
_V = TypeVar('_V')
_SingleT = TypeVar('_SingleT')
_FinalT = TypeVar('_FinalT')
_Storage = tuple[str, None] | tuple[None, int] | tuple[str, int]


class Fact(ABC, Generic[_SingleT, _FinalT]):
  """Information about a fact field on a ticket."""

  def __init__(
        self,
        name: str,
        code_name: str | None = None):
    self._name = name
    self._code_name = code_name or name.lower()


  @property
  def name(self) -> str:
    """Gets the original name used when creating the fact."""
    return self._name

  @property
  def code_name(self) -> str:
    """Gets the code-safe name for this fact."""
    return self._code_name

  @abstractmethod
  def convert_single_value_to_storage(self, value: _SingleT) -> _Storage:
    """Converts a value for storage as a tuple of string and integer."""

  @abstractmethod
  def convert_single_value_from_storage(self, value: _Storage) -> _SingleT:
    """Converts a value from a tuple of string and integer, from storage."""


class RepeatedFact(Fact[_V, list[_V]], Generic[_V]):
  """Fact that stores repeated values."""

  def convert_multiple_values_to_storage(self, values: list[_V]) -> list[_Storage]:
    """Converts a list of values for storage."""
    return [self.convert_single_value_to_storage(v) for v in values]

  def convert_multiple_values_from_storage(self, values: list[_Storage]) -> list[_V]:
    """Converts a list of values from storage."""
    return [self.convert_single_value_from_storage(v) for v in values]


class _StringFactMixin:
  def convert_single_value_to_storage(self, value: str) -> _Storage:
    """Mixin that overrides method in Fact."""
    return (value, None)

  def convert_single_value_from_storage(self, value: _Storage) -> str:
    """Mixin that overrides method in Fact."""
    assert value[0] is not None
    return value[0]


class StringFact(_StringFactMixin, Fact[str, str]):
  """Fact that stores a single string value."""


class RepeatedStringFact(_StringFactMixin, RepeatedFact[str]):
  """Fact that stores a list of string values."""


class _IntegerFactMixin:
  def convert_single_value_to_storage(self, value: int) -> _Storage:
    """Mixin that overrides method in Fact."""
    return (None, value)

  def convert_single_value_from_storage(self, value: _Storage) -> int:
    """Mixin that overrides method in Fact."""
    assert value[1] is not None
    return value[1]


class IntegerFact(_IntegerFactMixin, Fact[int, int]):
  """Fact that stores a single integer value."""


class RepeatedIntegerFact(_IntegerFactMixin, RepeatedFact[int]):
  """Fact that stores a list of string values."""

