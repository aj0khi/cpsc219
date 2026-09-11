from utils import add_reading_wrong, describe_temperature, format_reading
import sys

def main():
    print(describe_temperature(-12.0))
    print(describe_temperature(unit="F", celsius=-12.4))
    print(format_reading(-12.5, label = "Airport", unit = "C", decimal = 3))
    print(add_reading_wrong(1.0))
    print(add_reading_wrong(2.0))
    print(add_reading_wrong(3.0))
if __name__ == "__main__":
    main()
    sys.exit(0)