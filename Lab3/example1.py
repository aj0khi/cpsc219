def describe_temperature(celsius: float, unit: str = "C") -> str:
    if celsius < -20:
        label = "dangerously cold"
    elif celsius < 0:
        label = "cold"
    else:
        label = "warm"
    return f"{celsius:.1f}{unit}--{label}"

print(describe_temperature(-12.5)) #default unit
print(describe_temperature(12.5, unit="C")) #keyword
print(describe_temperature(unit = "F", celsius=12.5)) #order doesn't matter