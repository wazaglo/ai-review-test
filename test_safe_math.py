import pytest

from safe_math import safe_divide


def test_divide():
    assert safe_divide(10, 2) == 5


def test_zero_guard():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)
