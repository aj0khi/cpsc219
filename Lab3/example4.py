fahrenheit = []#slightly outdated, but still works
readings = [0, 20, 37, 100]
for c in readings:
    fahrenheit.append(c * 9 / 5 + 32)
print(fahrenheit)
fahrenheit = [c * 9 / 5 + 32 for c in readings] #list comprehension, can replace with just this one line
print(fahrenheit)


above_zero = [c for c in readings if c > 0] #list comprehension with a filter
print(above_zero)

station_temp = {name: temp * 9 /5 + 32 for name, temp in raw.items()} #dictionary comprehension, can replace with just this one line