import math
import sys
from pathlib import Path
from utils import celsius_to_fahrenheit, describe_temperature, average
# alternative
# from utils import *
# from utils import average
# import utils but then you have to specify utils.average
def main():
    print("I am in main!")
MAX = 600

# in java, they call functions - methods
# for this class, if i say method it just means function

# type hints, reading is a variable that is a list of floats
readings: list[float] = [-12.5, -8.0, 0.0, 4.5]

print(f"Average: {average(readings):.1f} C")

if __name__ == "__main__":
    main()  
    sys.exit(0)