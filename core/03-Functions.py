# -----------------BUILT-IN FUNCTIONS-----------------

# Data
mylist = [0, 1, 2, 3, 6, 7]
string = 'This is an example, an example of a string'
a = 10.5
b = 10, 2, 3, 'example'
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')


# abs() –> return the absolute value of a number
# len() –> return the length (number of items) of an object
# min() -> return the smallest item in an iterable or several arguments
# max() -> return the largest item in an iterable or several arguments
print(abs(10.5))
print(len(mylist))
print(max(mylist))
print(min(mylist))

# type() -> return the type of an object
print(type(mylist))

# int()/float()/str()         –> convert a value into int/float/string
# list()/dict()/tuple()/set() -> create a list/dictionary/tuple/set from an iterable
print(int(a))
print(list(b))

# lower()      -> return the lowercase version of the string
# upper()      -> return the uppercase version of the string
# capitalize() -> return a copy of the str with first character capitalized, rest lowercased
print(string.lower())
print(string.upper())
print(string.capitalize())

# find()  –> return the lowest index of the substring if it is found in given string
# join()  -> join elements in the given list together using a string as the delimiter
# split() -> return a list of substrings separated by the given delimiter (blankspace by default)
print(string.find('an'))
print('---'.join(['aaa', 'bbb', 'ccc']))
print(string.split(','))

# any(iterable) -> return True if any the elements evaluate to True
# all(iterable) -> return True if all the elements evaluate to True
print(any(mylist))  # Return True, since all elements except 0 evaluates to True
print(all(mylist))  # Return False, since 0 evaluates to False

# count(substring, start=n, stop=n) –> return the number of times the substr is in the given str
# start - optional, initial value where the function begins (0 by default)
# stop  - optional, initial value where the function ends (1 by default)
print(string.count('s', 4, 10))

# enumerate(iterable, start=n) –> take a collection and return it as an enumerate object
# output must be converted to a collection (list, tuple...) in order to print it
# start - optional, initial value where the function begins (0 by default)
print(list(enumerate(mylist)))

# filter(function, iterable) -> constructs an iterator from elements of an iterable for which a
# function returns true
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filterVowels(letter):
    if letter in string:
        return True
    else:
        return False
filteredVowels = filter(filterVowels, letters)

# map(function, iterable) -> execute a specified function for each item in an iterable and
# return an iterator. To print results, cast map as a list
def myfunc(n):
    return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))

# zip(*iterable) -> takes iterables, aggregates them in a tuple, and return it
# We can convert result to be a list or dictionary
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]
print(list(zip(friends, time_since_seen)))
print(dict(zip(friends, time_since_seen)))

# range(start=n, stop=n, step=n) –> return a sequence of numbers
# start - optional, initial value where the function begins (0 by default)
# stop  - optional, initial value where the function ends (1 by default)
# step  - optional, incremental value (1 by default)
range(0, 10, 2)

# replace('old_str', 'new_str', n) -> return a string where all occurrences of old_str have been
# replaced by new_str
# n - optional, set how many occurrences are replaced (all by default)
print(string.replace('example', 'test', 1))

# reversed(seq) -> return an iterator that accesses the given sequence in the reverse order
# output must be converted to a collection (list, tuple...) in order to print it
print(list(reversed(seq_tuple)))

# round(float, n) -> return a floating point number that is a rounded version of the given number
# n - optional, the number of decimals to use when rounding the number (0 by default)
print(round(17.24563, 2))

# sum(iterable, start=n) -> return the sum of all items in an iterable
# start - optional, initial value where the function begins (0 by default)
print(sum(mylist))

# startswith/endswith(string, start=n, stop=n) –> return TRUE if the string starts/ends with the
# given string
# start - optional, initial value where the function begins (0 by default)
# stop  - optional, initial value where the function ends (1 by default)
string.startswith('T', 10)

# strip('char') -> return a string with leading and trailing whitespace removed
# char - optional, specify the set of characters to be removed
print(string.strip('a'))

# delattr() -> deletes an attribute of an object
# dir()     -> attempt to return a list of valid attributes of an object
class Coordinate:
    x = 10
    y = -5
    z = 0
point1 = Coordinate()
delattr(Coordinate, 'z')  # remove attribute z
print(dir(point1))






# -----------------DATA TYPE FUNCTIONS-----------------

# Data
mylist = [1, 2, 3, 6, 7, 'hello']
mylist2 = [1, 5, 'goodbye']
mytuple = (1, 'home', 2.5, 6, 'cat')
myset = {1, 3, 5, 'cat', 'dog'}
myset2 = {1, 3, 5, 'bird', 'fish'}
mydict = {1: 'dog', 2: 'cat', 3: 'bird', 4: 'fish', 5: 'lizzard'}


# clear() –> remove all items
# Use with: list/set/dictionary
mylist.clear()
myset.clear()
mydict.clear()

# copy() -> return a shallow copy. Modifications in new object also affects old object
# Use with: list/set
mylist.copy()
myset.copy()

# count(value, start=n, stop=n) -> return the count of number of items passed as an argument
# index(value, start=n, stop=n) -> return the index of the first matched item
# start - optional, initial value where the function begins (0 by default)
# stop  - optional, initial value where the function ends (1 by default)
# Use with: list/tuple
mylist.count('hello')
mytuple.index('cat')

# pop() -> remove and return a value
# Use with: list/sets/dictionaries
# for lists, provide index of a value to be removed
# for sets, remove a random value
# for dicts, remove the item with key and return its value or default_value if key not found
mylist.pop()
mylist.pop(5)
myset.pop()
mydict.pop(2, 'default_value')

# remove() -> remove an item
# Use with: list/sets
mylist.remove(2)
myset.remove(3)



# List exclusive functions:
# append()  -> add an element to the end of the list
# extend()  -> add all elements of a list to another list
# insert()  -> insert an item at the defined index
# sort()    -> sort items in a list in ascending order
# reverse() -> reverse the order of items in the list
mylist.append(range(0, 5))
mylist.extend(mylist2)
mylist.insert(3, 'home')
mylist.sort()
mylist.reverse()



# Set exclusive functions:
# add()                         -> add the element given to the set
# difference(set_arg)           -> return elements that doesn't exist in set_arg
# discard()                     -> remove an element from the set if it is a member
# intersection(set_arg)         –> return the intersection (common values) of two sets as new set
# issubset(set_arg)             -> return True if another set contains this set
# issuperset(set_arg)           –> return True if this set contains another set
# symmetric_difference(set_arg) –> return the symmetric difference of two sets as a new set
# union(set_arg)                -> return the union of sets in a new set
# update(set_arg)               –> update the set with the union of itself and others
myset.add(102)
myset.difference(myset2)
myset.discard('cat')
myset.intersection(myset2)
myset.issubset(myset2)
myset.issuperset(myset2)
myset.symmetric_difference(myset2)
myset.union(myset2)
myset.update(myset2)



# Dictionary functions:
# fromkeys(seq, v)   –> return a new dictionary with keys from a sequence (seq) and an optional
# value (None by default)
# get(key, v)        –> return the value for the specified key. If key does not exit, it returns
# v (None by default)
# setdefault(key, v) –> if key exists, return its value. If not, insert key with a value v
# (None by default)
# items()            –> return a list of dictionary's (key, value) tuple pairs
# keys()             -> return a new view of dictionary's keys
# popitem()          -> remove and return an arbitary item (key, value)
# update(key, v)     –> update the dictionary with the key/value pairs overwriting them
# values()           –> return a new view of the dictionary's values
mydict.fromkeys((1, 2, 3), ('parrot', 'eagle', 'shark'))
mydict.get(2)
mydict.setdefault(6, 'animal')
mydict.items()
mydict.keys()
mydict.popitem()
mydict.update({7: 'reptile'})
mydict.values()
