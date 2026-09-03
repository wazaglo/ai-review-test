import math

import pytest

from temperature import Temperature


def test_boiling_point():
    assert Temperature(100).to_fahrenheit() == 212


def test_from_fahrenheit_roundtrip():
    t = Temperature.from_fahrenheit(98.6)
    assert math.isclose(t.celsius, 37.0, rel_tol=1e-9)


def test_kelvin_below_absolute_zero_rejected():
    with pytest.raises(ValueError):
        Temperature.from_kelvin(-1)


def test_to_kelvin_floor():
    assert Temperature.from_kelvin(0).to_kelvin() == pytest.approx(0)
