def add_reading(value:float, readings: list = []) -> list: #incorrect
    readings.append(value)
    return readings

def add_reading(value: float, readings: list[float] | None = None) -> list[float]: #correct
    if readings is None:
        readings = []
    readings.append(value)
    return readings