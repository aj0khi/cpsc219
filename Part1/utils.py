#if all i write in here is functions then I don't have to worry about the main guard

def f1():
    print("I am in f1")
def f2():
    x = 2

# because this has no main guard if you import utils in any other file and run the other file,
# then it will execute when we run that other file.

# use the main guard any time we have code that will execute when any other file runs this particular file.
def main():

print("__name__ in another .py")
print(__name__)


if __name__ == "__main__":
    main()

# when I run utils.py as an import in another file the __name__ variable is
# filled as utils. When I run utils.py as a script the __name__ variable is filled as __main__.