"""
ERROR HANDLING:
-Errors can be handled with try and except statements.
    -Try: the code that could potentially have an error is put in a try clause.
    -Except: the program execution executes the code inside except clause if an error happens.
    -Finally: the code that runs whether an exception happens or not.
    -Else: the code that runs if an exception is not raise.
-There are a lot of different exceptions.

RAISING EXCEPTIONS:
-Raise keyword allows you to raise your own exceptions.
-If no expressions are present, raise re-raises the last exception that was active in the current
scope further up the call stack.
-A raise statement must include the following elements:
    -The raise keyword.
    -A call to the Exception() function.
    -A string with a helpful error message passed to the Exception() function.

ASSERTIONS:
-Assertions helps to detect problems early in your program, where the cause is clear.
-The program to test a condition, and immediately trigger an error if the condition is false.
-The syntax will be -> assert condition.
-If an assert fails, your program should crash.

LOGGING:
-Python’s logging module makes it easy to create a record of custom messages that you write.
-These log messages will describe when the program execution has reached the logging function.
call and list any variables you have specified at that point in time.
"""

import sys
import traceback
import logging


# -----------------EXCEPTION HANDLING-----------------

# Exception handling example
def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')
    finally:
        print("I will always be executed")

def check(x):
    try:
        x > 3
    except ValueError:
        print("Something went wrong")
    else:
        print("Nothing went wrong")

print(check(5))
print(spam(0))

# Raising exception example
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
        # We can add raise keyword to reraise the current exception
        raise

# Getting traceback as a string
try:
    raise Exception('This is the error message.')
except:
    with open('errorInfo.txt', 'w') as e:
        e.write(traceback.format_exc())
    print('The traceback info was written to errorInfo.txt.')




# -----------------ASSERTIONS-----------------

# Creating assertions
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age


# Assertion example
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

switchLights(market_2nd)




# -----------------LOGGING-----------------

# Set basic configuration for log file
# filename -> set filename to save log
# format   -> set logging treshold (the least logging level that will be logged)
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s -  %(message)s')

# Add filename paramater to log to a file instead of console
logging.basicConfig(filename='myProgramLog.txt', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s -  %(message)s')

# Logging levels provide a way to categorize your log messages by importance
# To debug data, use of the following functions according to the level you want to use
# logging.debug()    -> logs a DEBUG msg. Used for small details.
# logging.info()     -> logs a INFO msg. Used to record information on general event
# logging.warning()  -> logs a WARNING msg. Used to indicate a problem but the program still works
# logging.error()    -> logs a ERROR msg. Used to record an error that caused the program to fail
# logging.critical() -> logs a CRITICAL msg. Used to indicate a fatal error
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

# logging.disable() -> suppress all log messages at that level or lower
logging.disable(logging.CRITICAL)


# Handling logs
# getLogger()   -> create log object
# StreamHandler -> class to create an object to handle log output
root_logger = logging.getLogger()
console_handler = logging.StreamHandler(sys.stdout)

# Set logging parameters
# setLevel()     -> set log level
# setFormatter() -> set log format
root_logger.setLevel(logging.ERROR)
console_handler.setFormatter(logging.Formatter('%(message)s'))

# Add handler to log object
root_logger.addHandler(console_handler)


# Loggin example:
logging.info('Start of program')
def factorial(n):
    logging.debug('Start of factorial(%s%%)' % n)
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % n)
    return total

print(factorial(5))
logging.info('End of program')
