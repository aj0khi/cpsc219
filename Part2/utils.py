def describe_temperature(celsius: float, unit: str = "C") -> str:
    """
    Describes the temperature in a human-readable format.
    
    Args:
        celsius (float): The temperature in Celsius.
        unit (str): The unit of the temperature (default is "C").

    Returns:
        str: A string describing the temperature.
    """
    if celsius < -20:
        label = "Canadian lukewarm"
    elif celsius < 0:
        label = "Poor skating conditions"
    elif celsius < 15:
        label = "Shorts weather"
    else:
        label = "No skidooing"
    return f"{celsius:.1f}{unit}--{label}"


def other_function():
    value = 1


def format_reading(
    value: float,
    unit: str = "C",
    decimal: int = 1,
    label: str = "",
) -> str:
    """Format a numeric reading with an optional label and unit."""

    prefix = f"{label}: " if label else ""
    return f"{prefix}{value:.{decimal}f}{unit}"



def add_reading_wrong(value: float, readings: list = [float]| None == None) -> list[float]:
    """
    Add a reading to a list without sharing state between calls.

    Args:
        value (float): The reading value to add.
        readings (list): The list of readings (default is a new empty list).

    Returns:
        list: The updated list of readings.
    """
    if readings is None:
        readings = []
    readings.append(value)
    return readings