def temperature_range(*readings: float) -> float | tuple[int, int]:
    """Return the spread between the highest and lowest reading.

    If fewer than two readings are provided, return (0.0).
    """
    if len(readings) < 2:
        return 0.0

    return max(readings) - min(readings)


print(temperature_range(10, 12, 14, 18))
print(temperature_range(3.5, 9.2))
print(temperature_range(42))
print(temperature_range())
 