def average(*values:float) -> float: #computes the average of a list of values
    if not values:
        return 0.0
    return sum(values) / len(values)

a=average(1,2,3,4,5)
print(a)

def log_event(event: str, **metadata) -> None:
    print(f"Event: {event}")
    for key, value in metadata.items():
        print(f"{key}: {value}")
log_event("Temperature reading", location="Lab", value=23.5, unit="C")