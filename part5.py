# best practices in python
# behind the scenes there are types for everything
number = 123 # behind the scenes this is an integer
# in java/C#/C++/etc. i would have to specify int number = 123;
# String, int, double, float

# we can actually provide "hints" for the types to be passed in
# good practice 1: to provide the types of variables or return values
def celsisus_to_fehrenheit(celsius: float) -> float:
  # good practice 2: doc strings - comments that explain what your code does
  """Convert a temperature from Celsius to F.
  
  Args:
    celsius: Temp in C
  
  Return:
    Equiv value in F
  """
  # java equiv of javadocs/docstring
  # /**
  #  * This program does... arg...
  # */
  
  # Good practice 3 - follow good convention/style
  # variables - lowercase_with_underscores - snake_case
  # in Java and other languages - lowercaseWithCaptialLettersForWords
  # it's not important for the program itself - but good for convention
  # if someone is looking at a java program, then they know when they see
  # lowercaseWithCapital - they are looking at a variable
  
  # in python - variables are the lowercase_with_underscores
  # constants: ALL_CAPS_WITH_UNDERSCORES
  # PEP 8 - official style guide for python
  
  # celsius is now a int
  print("hi")
  return 12.9

# types are: int, float, str, bool, list, dict, None

celsisus_to_fehrenheit(12.9)

# Beginner mistake
# comparing conditionals to explicit values

# e.g., bad
is_cold = True
 
if is_cold == True:
  print('it is cold')
  
# correct
if is_cold:
  print('it is cold')
  
# mistake 2: comparing None with ==
# wrong:
if value == None:
# right:
if value is None:

# mistake 3: not using enumerate when you need index and value
# bad:
for i in range(len(readings)):
  print(i, readings[i])
  
# pythonic - means good python practice
for i, temp in enumerate(readings):
  print(i, temp)
  
# when i use version control - i'll be using vscode
# or github desktop?
# pycharm - I'll try to make that available for lab exams, but no guarantee
# vscode will be used in class and tutorials

# launch.json - to make programming easier, make sure your familiar with that
# if cspc 217 content is shakey do review - code bootcamps
# practice using type hints - : type or the -> type
#   if you don't know what a type is: int, bool, float, review from 217
# docstrings - follow good style and conventions for explaining your code
# Modules - imports etc.
# == True, == None, manually indexing instead of enumerate
# pythonic - writing good python code

# how is python different from other languages
# java/c/c++/C#
# syntax - rules of a language are different
# {} - to identify scope - python does this with indentations
# python uses '#' comments, other languages require '//', or '/* ... */'
# other languages require types to be used: int, float
# in java/others there is a difference between int, Integer, float, Float, bool, Boolean
# in python your fine with just knowing what an integer, float, etc. is
# int, float, list

# 
