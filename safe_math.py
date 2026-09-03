"""Safe number helpers."""


def safe_divide(a: float, b: float) -> float:
    """Divide with explicit zero guard."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
