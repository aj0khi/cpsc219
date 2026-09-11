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