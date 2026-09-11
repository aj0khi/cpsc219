from utils import describe_temperature
import sys

def main():
    print(describe_temperature(-12.0))
    print(describe_temperature(unit="F", celsius=-12.4))


if __name__ == "__main__":
    main()
    sys.exit(0)