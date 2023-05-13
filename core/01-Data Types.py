"""
BASIC CONCEPTS:
-Time-complexity: aka "Big O" or "Big Oh", it is the computational complexity that describes the
amount of computer time it takes to run an algorithm.
    -See https://wiki.python.org/moin/TimeComplexity for information about time-complexity in
    every Python operation.
    -See https://en.wikipedia.org/wiki/Time_complexity#Table_of_common_time_complexities for
    general information.

-Hash table: a hash table is a structure that is designed to store a list of key-value pairs,
without compromising on speed and efficiency of manipulating and searching the structure.
    -The effectiveness of the hash table is derived from the hash function, a function that
    computes the index of the key-value pair.
    -In python, dictionaries and sets are implemented using a hash table.
    -Hash collisions are when two pieces of data in a hash table share the same hash value.
    -Hash collisions are practically unavoidable when hashing a random subset of a large set of
    possible keys.
    -Python uses open addressing to resolve hash coliisions.


PYTHON DATATYPES:
-Basic datatypes: int, float, string
-Basic containers: list, tuple, set, dictionary

STRINGS:
-Properties:
    -Immutable: elements cannot be changed or replaced.
    -Concatenation: strings can be concatenated using "+".
    -Indexing: access individual values.
    -Slicing: access a range of values
    -Strings can be iterated over, but are not iterable objects.

LISTS:
-Properties:
    -Mutable: their elements can be changed.
    -Concatenation: lists can be concatenated using "+".
    -Indexing: access individual values.
    -Slicing: access a range of values
    -Items are ordered and not unique.
    -Items can be of any kind, even lists, tuples, etc.

TUPLES:
-Properties:
    -Immutable: elements cannot be changed or replaced.
    -Concatenation: tuples can be concatenated using "+".
    -Indexing: access individual values.
    -Slicing: access a range of values
    -Items are ordered and not unique.
    -Items can be of any kind, even lists, tuples, etc.

SETS:
-Properties:
    -Mutable: their elements can be changed.
    -Items are unordered and unique.
    -Items in a set must be immutable, so we can't use lists, sets, dictionaries.
    -Duplicated items will not be presented.
    -Items can be of any kind, even lists, tuples, etc.

DICTIONARIES:
-Properties:
    -Mutable: their elements can be changed.
    -Items are unordered and not unique.
    -Values can be retrieved using keys that must be immutable (string, number, tuple with
    immutable elements) and unique.
"""



# -----------------STRINGS-----------------

# Create a string
myString1 = ["text"]
myString2 = ['text']

# Indexing - my_string[n]
new_string1 = myString1[3]
new_string2 = myString1[-1]  # return the last character

# Slicing - my_string[start:stop:step]
# start - optional value, included (0 by default)
# stop  - mandatory value, not included (1 by default)
# step  - optional incremental value (1 by default)
new_string3 = myString1[1:3]  # return characters 1, 2

# String formatting with % Operator
# %s    -> character substitute for strings or any object with a string repr, like numbers
# %d    -> character substitute for integers
# %f    -> character substitute for floats, use %.<number of digits>f for a fixed amount
# %x/%X -> character substitute integers in hex representation (lowercase/uppercase)
print('Hello %s' % 'Diego')
print('Hello %s, are you %d?' % ('Diego', 29))

# String formatting with format()
# Syntax -> 'String here {} then also {}'.format('something1','something2')
print('This is a string with an {}'.format('insert'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('First Object: {a}, Second Object: {b}'.format(a=12.3, b='Two'))
print('A {p} saved is a {p} earned.'.format(p='penny'))

# String formatting with f-strings (since Python 3.6)
# Syntax -> f'String here {value:{width}.{precision}}'
name = 'Fred'
print(f"He said his name is {name}.")
print(f"He said his name is {name!r}")
print(f"{5:02}")  # Print "5" with leading zeros up to a two-digit number - output: 05
i = 1827
print(f"{26:0{len(str(i))}}")  # Print "26" with leading zeros up to length of i - output: 0026






# -----------------LISTS-----------------

# Create a list
myList = [1, 2, 3, 4, 5]

# Retrieve data in a list
print(myList[2])
print(myList[0:3])

# List comprehension
# Syntax: myList = [expression for_loop_1 ... for_loop_n if_statement(optional)]
myList2 = [2 ** x for x in range(10) if x > 5]
myList3 = [x+y for x in ['Python ', 'C '] for y in ['Language', 'Programming']]






# -----------------TUPLES-----------------

# Create a tuple
myTuple = (3, 4.6, 'dog', 'cat', 'home')
myTuple2 = 3, 4.6, 'dog', 6

# Retrieve data in a tuple
print(myTuple[4])
print(myTuple[-1])

# Tuple unpacking
a = ('MNNIT Allahabad', 5000, 'Engineering')
(college, student, type_ofcollege) = a
print(college, student, type_ofcollege)






# -----------------SETS-----------------

# Create a set
mySet = {1, 2, 3, 4, 5}

# Set operations
# union                -> (setA | setB)
# intersection         -> (setA & setB)
# difference           -> (setA – setB)
# symmetric difference -> (setA ^ setB)

# Frozenset: a set which elements cannot be changed once assigned (immutable set)
# To create a frozenset, use the function frozenset()
my_frozenset = frozenset([1, 2, 3, 4])






# -----------------DICTIONARIES-----------------

# Create a dictionary
myDictionary1 = {'A': 7, 'B': 8, 'C': 4, 'D': 17, 'H': [5, 13]}
myDictionary2 = {'B': 23, 'E': 8, 'D': 'value3', 'K': 2}

# Retrieve data in a dictionary
print(myDictionary1['A'])
print(myDictionary1['H'][0])

# Join two dictionaries
# Python 3.9+
joined_dict1 = myDictionary1 | myDictionary2
# Python 3.5+
joined_dict2 = {**myDictionary1, **myDictionary2}
# Python 3.4 or lower
joined_dict3 = myDictionary1.copy()
joined_dict3.update(myDictionary2)
