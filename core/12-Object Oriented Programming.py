"""
OBJECTS:
-Everything in Python is an object, even functions and classes.
-Object: instance of a class. Objects have two characteristics:
    -Attributes -> characteristics of the object. They have the following properties:
        *They can be accessed/modified without using get/set methods.
        *There are not private attributes.
        *Attributes are formed with the key word self (self.attribute).
    -Methods -> behaviour associated to an object. They have the following properties:
        *There is not abstract methods.
        *Every method passes self as argument (my_method(self, *args)).
        *Declaration order is not important, since all methods belong to a class.
        *Methods that don't apply to the object are static, and need to be decorated with
        @staticmethod.

CLASSES:
-Class: blueprint of an object, containing all the attributes and methods. When class is defined,
only the description for the object is defined (no memory or storage is allocated).
-Self keyword: self is a reference to the instance itself and gives the object access to the
attributes and methods in the class.
-Class attributes: it's an attribute of the class, rather than an attribute of an instance of a
class. All objects of the class have access to class attributes. You should use class attributes
to do the following:
    -Storing constants.
    -Defining default values.
    -Tracking all data across all instances of a given class.
    -Performance.
-Class methods: a method that is bound to a class rather than its object.
    -It doesn't require creation of a class instance, much like staticmethod.
    -It works with the class since its parameter is always the class itself, while statics methods
    do not know anything about the class.
    -Class method can be called both by the class and its object: Class.classmethod() or
    Class().classmethod().



NAMESPACES:
-Python classes and instances of classes each have their own distinct namespaces: MyClass.__dict__
and instance_of_MyClass.__dict__, respectively.
-When you try to access an attribute from an instance of a class, it first looks at its instance
namespace. If it finds the attribute, it returns the associated value. If not, it then looks in
the class namespace.
-The instance namespace takes supremacy over the class namespace.

__INIT__:
-A special method that Python runs automatically whenever we create a new instance.
-It defines attributes for the objects of a class.
-We can pass arguments to __init__ method, assigning them to object attributes.

INHERITANCE:
-It refers to defining a new class with little or no modification to an existing class.
-The new class is called derived (or child) class. The one from which it inherits is called the
base (or parent) class.
-Derived class inherits attributes and functions from the parent class.
-New attributes and functions can be added to derived class.
-After the base class's __init__ ran, the derived object has the attributes set there as it's the
very same object as the self in the derived class' __init__.
-You can and should just use self.some_var everywhere. Super() is only for accessing stuff from
base classes, but instance variables are (as the name says) part of an instance, not part of that
instance's class.

MULTIPLE INHERITANCE
-Python allows to inherit from multiple classes.
-Add more information...

METHOD RESOLUTION ORDER:
-The method resolution order (or MRO) tells Python how to search for inherited methods.
-MRO tells you exactly where Python will look for a method you’re calling with super() and in
what order.
-Every class has an .__mro__ attribute that allows us to inspect the order.

ENCAPSULATION:
-Protected members: prefixing the name of the member by a single underscore '_'.
-Private members: there is no existence of Private instance variables that cannot be accessed
except inside a class.
However, to define a private member, prefix the member name with double underscore “__”.
-Python’s private and protect member can be accessed outside the class through python name
mangling.

POLYMORPHISM:
-Polymorphism is an ability in OOP to use a common interface for multiple forms (data types).
-It allows us to define methods in the child class with the same name as defined in their parent
class.
-You can re-implement method in the child class. This process is known as Method Overriding.
-You can access overridden method of the parent class in the child class, by using the super()
function.

ABSTRACT CLASS AND INTERFACES
-An abstract class can be considered as a blueprint for other classes.
-Abstract classes allows you to create a set of methods and attributes that must be implemented
or override within any child classes built from it.
-Abstract classes can't be instantiated, they must be inhereted by another class.
-Abstract classes do not need to implement all their functionalities. You can leave some of them
as abstract so that your subclasses must implement them.
-The difference with interfaces is that they only allows you to define a functionality, not
implement it.
-Python comes with a module that provides the base for defining Abstract Base classes(ABC)
called ABC.
-ABC works by decorating methods of the base class as abstract and then registering concrete
classes as implementations of the abstract base.

PYTHON PROPERTY
-Python @property decorator turns a method into a “getter” for a read-only attribute
-A property object has getter, setter, and deleter methods usable as decorators that create a
copy of the property with the corresponding accessor function set to the decorated function.
"""

from abc import ABCMeta, abstractmethod
from typing import final
from inspect import Signature, Parameter



# -----------------PYTHON OOP BASICS-----------------

class Person:
    # These are class attributes.
    age = 29
    sex = 'man'

    # This is a class method
    @classmethod
    def status(cls):
        print(cls.age, cls.sex)

    # This is a statitc method
    @staticmethod
    def static():
        print("Hello, I don't take arguments!")

    # Methods can be overriden, but we can use @final to avoid this
    @final
    def finalFunc(self):
        return "This can't be overriding"

    # This initializes the object’s class
    # Attributes can have a constant value or getting it as a parameter
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.species = 'homo sapiens'

    # This is an object method
    def greet(self):
        print('Hello', self.name)

    # Order of declaration is not important
    # See how we use check_age before its definition
    def welcome(self):
        self.greet()
        self.check_age()

    def check_age(self):
        print(f'Age of {self.name} is: {Person.age}')


# Creating an object of a class
boy = Person('Diego', 'Spain')

# Accessing/deleting attributes of an object
print(boy.name, '-', boy.country)
# del boy.name

# Executing class methods (different syntaxes)
boy.greet()
boy.check_age()
# Person.greet(boy)
# Person.check_age(boy)






# -----------------INHERITANCE-----------------

# Parent class Rectangle, with its attributes and methods
class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    # We define constructor for the child class
    def __init__(self, length, **kwargs):
        # super() alone returns a temporary object of the superclass
        # This object allows you to call that superclass’s methods and attributes
        # We must call the constructor of the parent class with its parameters
        super().__init__(length=length, width=length, **kwargs)
        # After the base class's __init__ ran, the derived object attributes are set as part of
        # its own __init__
        # So, we should just use self.some_var everywhere
        # Super is for accessing stuff from base classes
        # For example, here we should use self.area() to get the area of a Square object
        self.area = self.area()

# Cube class inherits from Square, which inherits from Rectangle
class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

# New parent class, Triangle
class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height

    def tri_area(self):
        return 0.5 * self.base * self.height

# Rightpyramid inherits from Square and Triangle
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

pyramid = RightPyramid(2, 4)
print(RightPyramid.__mro__)
print(pyramid.area())
print(pyramid.area_2())


# Another inheritance example using **kwargs
class Shape:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self, radius: float, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    # __signature__ attribute is a typing.Signature object that describes the arguments that the
    # class expects.
    __signature__ = Signature(
        parameters=[
            Parameter('radius', Parameter.POSITIONAL_OR_KEYWORD, annotation=float),
            Parameter('x', Parameter.POSITIONAL_OR_KEYWORD, annotation=float),
            Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, annotation=float),
        ]
    )






# -----------------ENCAPSULATION-----------------

class Base:
    def __init__(self):
        # Protected member
        self._a = 2
        # Private member
        self.__c = "GeeksforGeeks"

class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected and private member of base class: ")
        print(self._a)
        print(self.__c)

obj1 = Derived()
obj2 = Base()

# Calling protected member outside class will result in attributeError
# print(obj2.a)
# print(obj2.c)






# -----------------POLYMORPHISM-----------------

# Explore function has the same name in both class A and B, but it performs different
# Class C uses super() function to access overwritten methods
class A:
    def explore(self):
        print("explore() method from class A")

class B(A):
    def explore(self):
        print("explore() method from class B")

class C(A):
    def explore(self):
        super().explore()  # calling the parent class explore() method
        print("explore() method from class C")

b_obj = B()
a_obj = A()
c_obj = C()
b_obj.explore()
a_obj.explore()
c_obj.explore()






# -----------------ABSTRACT BASE CLASS-----------------

# Main abstract Animal class that defines a blueprint for any animal that inherits from it
class Animal(metaclass=ABCMeta):
    def walk(self):
        print(f'{self} is walking...')

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def num_legs(self):
        pass


# Class Dog and Monkey that inhertis from Animal
# All abstract methods in the main abstract class must be implemented for every children by
# overriding them
class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 4

    def eat(self):
        print("Dogs eat meat")

class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2

    def eat(self):
        print("Monkeys don't eat meat")


animals = [Dog("Rolf"), Monkey("Bob")]
for a in animals:
    print(a.num_legs())
    print(a.eat())






# -----------------PYTHON PROPERTY-----------------

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """I'm a property"""
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        """I'm a setter"""
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        """I'm a deleter"""
        print('Deleting name')
        del self._name

p = Person('Adam')
print('The name is:', p.name)  # Return property name of p object
p.name = 'John'                # Assign a new value for to p.name
del p.name                     # Delete property p.name
