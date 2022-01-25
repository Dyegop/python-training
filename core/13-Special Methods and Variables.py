"""
OVERLOADING BUILT-IN FUNCTIONS:
-It is possible for us to change the default behavior of Python's built-in functions.
-To overload a function, we must define it in our class in the __overloadedFunction:__ format.
-Anytime we pass an object of our class to the overloaded function, the result will be obtained by calling our custom
defined function.


MAGIC METHODS:
-Magic methods follow the next structure: __MagicMethod__.
-Magic methods don't need to be invoked directly.
-There are a lot of magicc methods: __init__, __name__, __str__, etc.


__INIT, __NEW__:
-__init__ method will be called to initialize the object.
-__new__ method will be called when an object is created.

__REPR__
-__repr__ represents a class's objects as a string

__CALL__
-__call__ enables Python programmers to write classes where the instances behave and can be called like functions.
-x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).

__STR__:
-It returns a string representation of an object, giving the instance of the object a readable name.

__ADD__, __SUB__
-Magic methods for the "+" and "-" operators.

__GETITEM, __SETITEM__, __DELITEM__
-__getitem__ is called to implement evaluation of self[key], i.e var = data_obj[2]
-__setitem__ is called to implement assignment to self[key], i.e data_obj[2] = 4
-__delitem__ is called to implement deletion of self[key]
-This methods should only be implemented for mappings if the objects support changes to the values for keys, or if new
keys can be added, or for sequences if elements can be replaced

__NAME__:
-Whenever the Python interpreter reads a source file, it does two things:
  -it sets a few special variables like __name__.
  -it executes all of the code found in the file.
-Running your module as the main program, the interpreter will assign the hard-coded string "__main__"
to the __name__ variable.
-Running your module imported by another program, the interpreter will search for your imported py file
(along with searching for a few other variants) and, prior to executing imported py file, it will assign
its name to the __name__ variable.
-After the special variables are set up, the interpreter executes all the code in the module, one statement at a time.
-__Name__ is useful if you want to write a .py file that can be both used by other programs and/or libraries as a
module, and can also be run as the main program itself. For example:
    -Your module is a library, but you want to have a script mode where it runs some unit tests or a demo.
    -Your module is only used as a main program, but it has some unit tests, and the testing framework works by
    importing .py files like your script and running special test functions.
    -Your module is mostly used as a main program, but it also provides a programmer-friendly API for advanced users.

__DIR__:
-It tries to return a list of valid attributes of the object
-If the object has __dir__() method, the method will be called and return the list of attributes.
-If the object doesn't have __dir__() method, this method tries to find information from the __dict__ attribute
(if defined), and from type object.

__NEXT__, __ITER__
-__next__ returns the next item for an iteration.
-__iter__ is like a factory method that returns a new iterator for this specific iterable.
"""



# -----------------OVERLOADING BUILT-IN FUNCTION-----------------
# Overloading built-in functions example:
class Purchase:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        return len(self.basket)

purchase = Purchase(['pen', 'book', 'pencil'], 'Python')
# len() now returns the length of Purchase object, instead of an integer
print(len(purchase))






# -----------------SPECIAL METHODS EXAMPLES-----------------

# __new__:
class A(object):
    def __new__(cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)

    # It is not called
    def __init__(self):
        print("Init is called")

class B(object):
    def __new__(cls):
        print("Creating instance")

    # It is not called
    def __init__(self):
        print("Init is called")

A()
print(B())



# __call__:
class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self):
        print("Instance is called via special method")

e = Example()
e()



# __str__ and __repr__:
class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} (quantity: {self.quantity})"

    def __repr__(self):
        return f"Name: {self.name} - Quantity: {self.quantity}"

a_product = Product("Iphone X", 12)
print(a_product)  # Iphone X (quantity: 12)



# __add__, __sub__ example:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1+p2)
print(p2-p1)



# __getitem__, __setitem__, __delitem__ example:
class Counter(object):
    def __init__(self, floors):
        self._floors = [None] * floors

    def __setitem__(self, floor_number, data):
        self._floors[floor_number] = data

    def __getitem__(self, floor_number):
        return self._floors[floor_number]

    def __delitem__(self, floor_number):
        del self._floors[floor_number]

index = Counter(4)
index[0] = 'ABCD'
index[1] = 'EFGH'
index[2] = 'IJKL'
index[3] = 'MNOP'
print(index[2])
del index[2]



# __name__:
print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")

# Code execution:
# 1- It prints the string "before import" (without quotes).
# 2- It loads the math module and assigns it to a variable called math.
# 3- It prints the string "before functionA".
# 4- It executes the def block, creating a function object, then assigning that function object to a variable functionA.
# 5- It prints the string "before functionB".
# 6- It executes the second def block, creating another function object, then assigning it to a variable functionB.
# 7- It prints the string "before __name__ guard".
# 8- if your module is the main program -> it will see that __name__ was indeed set to "__main__" and it calls and
# executes the two functions
# 8- if your module is imported by another program -> __name__ will be renamed to the the imported module and it'll
# skip the body of the if statement
# 9- It will print the string "after __name__ guard" in both situations.



# __dir__:
class Person:
    def __dir__(self):
        return ['age', 'name', 'salary']

teacher = Person()
print(dir(teacher))



# __next__, __iter__
class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    # Return next object of a generator if object < 100
    def __next__(self):
        if self.number < 100:
            self.number += 1
            return self.number
        else:
            raise StopIteration()

    # Return list object as iterator
    def __iter__(self):
        return self
