def is_positive(value):
    """Return whether ``value`` is greater than zero."""
    if value is None:
        return False
    return value > 0

samples = [3.2, -1.5, 7.0]
for i in range(len(samples)):
    print(i, samples[i])