"""
ITERATORS:
-Reading items one by one is called iteration.
-Iterators are containers for objects so that you can loop over them.
-Technically, in Python, an iterator is an object which implements the iterator protocol, which
consist of the methods __iter__() and __next__().

GENERATORS:
-A generator is a function that remembers the state it’s in, in between executions.
-Generators do not store all the values in memory, they generate the values on the fly.
-Generators give us an easier way to create python iterators, using yield keyword instead of
return.
-Generators are best for calculating large sets of results saving memory.

YIELD:
-Generators are created using keyword yield.
-Yield is similar to return, except the function will return a generator.
-When you call a function that has yield, the code you have written in the function body only run
the first time.
-The second time, only yield statement will be executed.
-Using "yield from" we don't need to iterate over a generator, so we can use next() to print a
value without a loop.
-We can use yield to recieve data.


https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
"""

from collections import deque


# -----------------BASIC CONCEPTS-----------------

# Creating a generator
def genfibon(n):
    # Generate a fibonnaci sequence up to n
    a = 1
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        yield b

# If we print this, we will get the generator memory address instead of the returned value
print(f"-----------{genfibon(10)}-----------")

# To get returned values, we must iterate over the generator
# Generators are iterators, a kind of iterable you can only iterate over once.
for num in genfibon(10):
    print(num)


# next() -> access the next element in a sequence
def simple_gen():
    for x in range(3):
        yield x
g = simple_gen()
print(next(g))


# iter() -> create an object which can be iterated one element at a time
s_iter = iter('hello')
print(next(s_iter))




# -----------------BUILDING CUSTOM ITERATORS-----------------

class PowTwo:
    def __init__(self, max_value=0):
        self.max_value = max_value

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max_value:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

numbers = PowTwo(3)

# Create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
for _ in i:
    print(_)




# -----------------RECIEVING DATA WITH YIELD-----------------

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

# This function is called coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


def greet(gen):
    gen.send(None)
    while True:
        greeting = yield
        g.send(greeting)
    # Alternative
    # Yield from recieve data and forward it to another generator
    # yield from gen


greeter = greet(friend_upper())

greeter.send(None)  # Priming the generator
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')
