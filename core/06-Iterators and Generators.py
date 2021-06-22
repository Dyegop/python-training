"""
GENERATORS:
-A generator is a function that remembers the state it’s in, in between executions.
-Generators give us an easier way to create python iterators, using yield keyword instead of return.
-Generators are best for calculating large sets of results saving memory.

ITERATORS:
-Iterators are containers for objects so that you can loop over the objects.
-An iterable can be any object that has an __iter__ method defined. For example, lists are iterators.
"""



# -----------------BASIC CONCEPTS-----------------

# Creating a generator
def genfibon(n):
    # Generate a fibonnaci sequence up to n
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b
for num in genfibon(10):
    print(num)

# next() -> access the next element in a sequence
def simple_gen():
    for x in range(3):
        yield x
g = simple_gen()
print(next(g))

# iter() -> create an object which can be iterated one element at a time. Useful to iterate over strings
s_iter = iter('hello')
print(next(s_iter))
