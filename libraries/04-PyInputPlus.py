"""
PYINPUTPLUS:
-A module that contains functions similar to input() for several kinds of data: numbers, dates,
email addresses and more.
"""

import pyinputplus as pyip


# -----------------PYINPUTPLUS-----------------

# Functions to detect different inputs
# inputStr()      -> similar to input() but you can also pass a custom validation function to it
# inputNum()      -> ensures the user enters a number and returns an int or float
# inputChoice()   -> ensures the user enters one of the provided choices, and return selected
# choice as string
# inputMenu()     -> similar to inputChoice(), but provides a menu with numbered or lettered
# options
# inputDatetime() -> ensures the user enters a date and time
# inputYesNo()    -> ensures the user enters a yes/no response
# inputBool()     -> similar to inputYesNo(), but takes a True/False response and returns a
# Boolean value
# inputEmail()    -> ensures the user enters a valid email address
# inputFilepath() -> ensures the user enters a valid file path and filename, and can optionally
# check that file exists
# inputPassword() -> similar the built-in input(), but displays * characters as the user types so
# that passwords,
# or other sensitive information, aren’t displayed on the screen

# Arguments for inputNum()
# min/max              -> ensures input to be a min/max value
# greaterThan/lessThan -> ensures input to be greater or less than a value
response1 = pyip.inputNum('Enter num: ', min=4)
response2 = pyip.inputNum('Enter num: ', greaterThan=4)

# Arguments for any function
# limit=int         -> limit the number of tries to enter valid input before the default value
# is returned
# timeout=int/float -> limit the number of seconds to enter a valid input
# default=str/None  -> default value to use should the user time out or exceed the number of tries
# blank=True        -> allow you to use blank inputs
# allowRegexes      -> limit input to a list of regular expression strings
# blockRegexes      -> block a list of regular expression strings to be accepted as an input
response3 = pyip.inputNum(limit=2, default='N/A')
response4 = pyip.inputNum(timeout=10, default='N/A')
response5 = pyip.inputNum(blank=True)
response6 = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response7 = pyip.inputNum(blockRegexes=[r'[02468]$'])

# You can write a function to perform your own custom validation logic by passing the function
# to inputCustom()
def adds_uptoten(numbers):
    numberslist = list(numbers)
    for i, digit in enumerate(numberslist):
        numberslist[i] = int(digit)
    if sum(numberslist) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numberslist)))
    return int(numbers)  # Return an int form of numbers

response8 = pyip.inputCustom(adds_uptoten)
