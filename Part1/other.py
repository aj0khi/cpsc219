import sys
import utils


print("hello world")
print("__name__ in another .py")
print(__name__)

#if other.py is the primary file - the file i run
# other.py __name__ variable is set to __main__
#any other import will have it's name set to their file name.
#eg sys.py's __name__ variable is set to sys