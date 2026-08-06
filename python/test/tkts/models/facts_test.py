import sys
import pytest
from tkts.models import facts


def test_fact_basics():
  f = facts.Fact('A')
  assert f.name == "A"
  assert f.code_name == "a"


def test_base_string_fact_abstract():
  with pytest.raises(TypeError):
    f = facts.BaseStringFact('A')


def test_string_fact_basics():
  f = facts.StringFact('A')
  assert f.name == "A"
  assert f.code_name == "a"
  assert f._convert_to_string_list(7) == ["7"]


def test_repeated_string_fact_basics():
  f = facts.RepeatedStringFact('A')
  assert f.name == "A"
  assert f.code_name == "a"
  assert f._convert_to_string_list([7, 8]) == ["7", "8"]


def test_base_integer_fact_abstract():
  with pytest.raises(TypeError):
    f = facts.BaseIntegerFact('A')


def test_integer_fact_basics():
  f = facts.IntegerFact('A')
  assert f.name == "A"
  assert f.code_name == "a"
  assert f._convert_to_integer_list(7) == [7]


def test_repeated_integer_fact_basics():
  f = facts.RepeatedIntegerFact('A')
  assert f.name == "A"
  assert f.code_name == "a"
  assert f._convert_to_integer_list([7, 8]) == [7, 8]


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))


