"""
Includes the Fact class and all sub-classes.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterable


class Fact(ABC):
  """Provides information about a field that can be attached to a ticket."""

  def __init__(self, name: str):
    self._name = name
    self._code_name = name.lower()

  @property
  def name(self) -> str:
    """Gets the original name used when creating the fact."""
    return self._name

  @property
  def code_name(self) -> str:
    """Gets the code-safe name for this fact."""
    return self._code_name


class BaseStringFact(Fact, ABC):
  """Base class for string-shaped facts."""

  @abstractmethod
  def _convert_to_string_list(self, value: object) -> list[str]:
    """Converts the value to a list of strings."""


class StringFact(BaseStringFact):
  """Fact that stores a single string value."""

  def _convert_to_string_list(self, value: object) -> list[str]:
    return [str(value)]


class RepeatedStringFact(StringFact):
  """Fact that stores a list of string values."""

  def _convert_to_string_list(self, value: Iterable[object]) -> list[str]:
    return [str(x) for x in value]


class BaseIntegerFact(Fact, ABC):
  """Fact that stores an integer value."""

  @abstractmethod
  def _convert_to_integer_list(self, value: object) -> list[int]:
    """Converts the value to a list of integers."""


class IntegerFact(BaseIntegerFact):
  """Fact that stores a single integer value."""

  def _convert_to_integer_list(self, value: object) -> list[int]:
    return [int(value)]


class RepeatedIntegerFact(BaseIntegerFact):
  """Fact that stores a list of string values."""

  def _convert_to_integer_list(self, value: Iterable[object]) -> list[int]:
    return [int(x) for x in value]
