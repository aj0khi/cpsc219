def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: The temperature in degrees Celsius.

    Returns:
        The equivalent temperature in degrees Fahrenheit.
    """
    return celsius * 9 / 5 + 32


def describe_temperature(celsius: float) -> str:
    """Return a plain-language description of a temperature.

    Args:
        celsius: The temperature in degrees Celsius.

    Returns:
        A string: 'dangerously cold', 'cold', 'cool', or 'warm'.
    """
    if celsius < -20:
        return "dangerously cold"
    elif celsius < 0:
        return "cold"
    elif celsius < 15:
        return "cool"
    else:
        return "warm"


def average(values: list[float]) -> float:
    """Compute the arithmetic mean of a list of values.

    Args:
        values: A non-empty list of numeric values.

    Returns:
        The arithmetic mean.
    """
    return sum(values) / len(values)