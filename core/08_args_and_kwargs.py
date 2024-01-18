"""
args:
-It allows you to pass multiple arguments to a function by using the unpacking operator (*).
-Using args is just a convention, any name can be used instead.

kwargs:
-It allows you to pass multiple keyword args to a function by using the unpacking operator (**).
-Instead of accepting positional arguments it accepts keyword (or named) arguments.
-Using **kwargs is just a convention, any name can be used instead.
"""


# -----------------HANDING MULTIPLE ARGUMENTS-----------------

# args example:
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result
print(my_sum(1, 2, 3))


# kwargs example:
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result
print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))






# -----------------ARGUMENT UNPACKING-----------------

# Argument unpacking example
accounts = {'checking': 1958.00, 'savings': 3695.50}
transactions = [(-180.67, 'checking'), (-220.00, 'checking'), (220.00, 'savings')]
def add_balance(amount, name):
    accounts[name] += amount
    return accounts[name]

for t in transactions:
    """Without argument unpacking"""
    add_balance(t[0], t[1])

for t in transactions:
    """With argument unpacking - Each element of t is passed as argument"""
    add_balance(*t)
