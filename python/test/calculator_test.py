import sys
import pytest
from python.src.calculator import add


def test_add_integers():
    assert add(5, 7) == 12

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_negatives():
    assert add(-3, -7) == -10
    assert add(-5, 5) == 0


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))


