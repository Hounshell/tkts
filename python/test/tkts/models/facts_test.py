import sys
import pytest
from tkts.models import facts


@pytest.mark.parametrize("cls", [
    facts.Fact,
    facts.RepeatedFact,
    facts._StringFactMixin,
    facts._IntegerFactMixin,
])
def test_abstract_classes_are_abstract(cls):
  with pytest.raises(TypeError):
    f = cls('A')


@pytest.mark.parametrize("cls", [
    facts.StringFact,
    facts.IntegerFact,
    facts.RepeatedStringFact,
    facts.RepeatedIntegerFact,
])
def test_fact_basics(cls):
  fact = cls("A")
  assert fact.name == "A"
  assert fact.code_name == "a"


@pytest.mark.parametrize("cls, value", [
    (facts.StringFact, "Hello world"),
    (facts.RepeatedStringFact, "a"),
    (facts.IntegerFact, 7),
    (facts.RepeatedIntegerFact, 1),
])
def test_single_value_roundtrip(cls, value):
  fact = cls(str(cls))
  storage = fact.convert_single_value_to_storage(value)
  result = fact.convert_single_value_from_storage(storage)

  assert value == result


@pytest.mark.parametrize("cls, value", [
    (facts.RepeatedStringFact, ["a", "b", "c"]),
    (facts.RepeatedIntegerFact, [1, 2, 3, 4]),
])
def test_multiple_values_roundtrip(cls, value):
  fact = cls(str(cls))
  storage = fact.convert_multiple_values_to_storage(value)
  result = fact.convert_multiple_values_from_storage(storage)

  assert value == result


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))


