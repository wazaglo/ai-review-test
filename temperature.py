"""Temperature conversion utilities with input validation and tests."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Temperature:
    """A temperature value stored internally in Celsius."""

    celsius: float

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        return cls(celsius=(fahrenheit - 32) * 5 / 9)

    @classmethod
    def from_kelvin(cls, kelvin: float) -> "Temperature":
        if kelvin < 0:
            raise ValueError("Kelvin cannot be below absolute zero")
        return cls(celsius=kelvin - 273.15)

    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self) -> float:
        kelvin = self.celsius + 273.15
        if kelvin < 0:
            raise ValueError("Result below absolute zero")
        return kelvin
