def format_sensor_output(value: float | int, decimals: int = 2, unit: str = "C") -> str:
    return f"{value:.{decimals}f} {unit}"


print(format_sensor_output(12.345))
print(format_sensor_output(12.345, 3))
print(format_sensor_output(value=12.345, unit="F", decimals=1))
