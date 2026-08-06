import sys
import pytest
from tkts.models import facts


def test_fact_basics():
  f = facts.Fact('A')
  assert f.name == "A"
  assert f.code_name == "a"


def test_string_fact_basics():
  f = facts.StringFact('A')
  assert f.name == "A"
  assert f.code_name == "a"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))


