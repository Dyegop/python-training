"""
BASIC FUNCTIONS CONCEPTS:
-Everything in Python are objects, so a function can be considered an object.
-If we do print(function_name), we will get the memory address for that object.
-Adding a pair of parentheses after a function gets the function executed.
-If we don’t put parentheses, a function can be passed around and assigned to other variables.

DECORATORS:
-A decorator takes in a function as parameter, adds some functionality and returns that function.
-This is also called metaprogramming (a part of the program tries to modify another part at compile time).
-A decorated function will take then name of the decorator function
-Built-in decorators:
    -@property       -> transform function into a property attribute. Only for methods that does not required parameteres.
    -@staticmethod   -> transform a method into a static method so it does not receive an implicit first argument
    -@final          -> restrict the use of inheritance and overriding
    -@classmethod    -> make function behave like a class method
    -@abstractmethod -> transforma a method into an abstract one
    -@memoized       -> caches a function's return value each time it is called and return that value if called later
"""

import functools



# -----------------DECORATORS BASICS-----------------

user1 = {'username': 'jose123', 'access_level': 'guest'}
user2 = {'username': 'bob', 'access_level': 'user'}

# Create a decorator
def user_has_permission(func):
    def secure_func():
        if user1.get('access_level') == 'admin':
            return func()
    return secure_func

# Create a function that we want to decorate
def my_function():
    return 'Password for admin panel is 1234.'

# Apply decorator to my function
my_secure_function = user_has_permission(my_function)

# Proper syntax
@user_has_permission
def my_function():
    """Allows us to retrieve the password for the admin panel"""
    return 'Password for admin panel is 1234.'

@user_has_permission
def another():
    pass


# If we print the function name, we can see that our function takes the name of the decorator
# We can use functools to keep the name of our functions
print(my_function.__name__)
print(another.__name__)

def user_has_permission_modified(func):
    @functools.wraps(func)
    def secure_func():
        if user1.get('access_level') == 'admin':
            return func()
    return secure_func






# -----------------DECORATORS WITH PARAMETERS-----------------

# To allow a decorator to accept parameters, we need to wrap our decorator with another function that takes parameters
# Create our main function with the parameters to pass
def user_has_permission(access_level):
    # Create the decorator
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user1.get('access_level') == access_level:
                return func(panel)
        return secure_func
    return my_decorator

@user_has_permission('user')
def my_function(panel):
    """Allows us to retrieve the password for the admin panel."""
    return f'Password for {panel} panel is 1234.'

print(my_function.__name__)
print(my_function('movies'))

# To make a decorator generic for any function, we can use *args and **kwargs
def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user1.get('access_level') == 'admin':
            return func(*args, **kwargs)
    return secure_func






# -----------------MULTIPLE DECORATORS IN ONE FUNCTION-----------------

# Example of multiple decorators
def user_name_starts_with_j(func):
    """This decorator only runs the function passed if the user's username starts with a j"""
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user1.get('username').startswith('j'):
            return func(*args, **kwargs)
        else:
            print("User's username did not start with 'j'.")
    return secure_func

def user_has_permission_multi(func):
    """This decorator only runs the function passed if the user's access_level is admin"""
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user1.get('access_level') == 'admin':
            return func(*args, **kwargs)
        else:
            print("User's access_level was not 'admin'.")
    return secure_func

@user_has_permission_multi
@user_name_starts_with_j
def double_decorator():
    return 'I ran.'

print(double_decorator())

"""
When `double_decorator()` runs, this chain of "functions" runs:
    user_has_permission -> user_name_starts_with_j -> double_decorator

That is because user_name_starts_with_j is the first decorator to be applied. 
It replaces double_decorator by the function it returns.
Then, user_has_permission is applied and replaces the function the other decorator returned by the function it returns.
"""
