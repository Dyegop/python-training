"""
Implement an @access_control decorator that can be used like this:
@access_control(access_level)
def delete_some_file(filename):
    # perform the deletion operation
    print('{} is deleted!'.format(filename))
Your decorator should meet the following requirements:
- It takes in an argument `access_level` and would compare the current user's role with the
access level.
- You can get the current user's role, represented by an integer, by calling the
`get_current_user_role()` function.
    You don't need to implement this function, we will take care of it for you.
- You may assume smaller access level value would have higher privilege. For example,
0 - admin, 1 - user, 2 - guest.
- If the user has the proper access level, we allow the user to call the function (that has
this decorator).
- If the user does not have a proper access level, we raise a `PermissionError`
- The decorator should be generic
- Your decorator should keep the original function's `__name__` and `__doc__` strings.
"""

import functools



def get_user_role() -> int:
    # return the current user's role, represented by an int
    # for example, 0 - admin, 1 - user, 2 - guest
    # You don't need to change this function, we will replace it with a real function that
    # returns the user's role
    return 2

def access_control(access_level: int):
    def decorator(func):
        @functools.wraps(func)
        def check_user_role(*arg, **kwargs):
            if get_user_role() <= access_level:
                return func(*arg, **kwargs)
            else:
                raise PermissionError('You do not have the proper access level.')
        return check_user_role
    return decorator

@access_control(1)
def delete_some_file(filename):
    # perform the deletion operation
    print('{} is deleted!'.format(filename))

delete_some_file("Documents")
