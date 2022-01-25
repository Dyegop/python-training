"""
COROUTINES
-Coroutines are a more generalized form of subroutines.
-While subroutines are entered at one point and exited at another point, coroutines can be entered, exited, and resumed
at many different points.
-They can be implemented with the async def statement.


"""



from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


"""async def greet(g):
    print('Starting...')
    await g
    print('Ending...')


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)
"""

friend_upper().send("hello")
