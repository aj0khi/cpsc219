stations = {
    "Rooftop": -12.5,
    "North Tower": -8.2,
    "South Terrace": -4.1,
    "Basement": 2.3,
}

fahrenheit = {name: (temp * 9 / 5) + 32 for name, temp in stations.items()}
print(fahrenheit)
