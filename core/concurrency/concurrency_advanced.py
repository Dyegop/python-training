"""
LOCKS
-A Lock is an object that acts as a permit and will be assigned to only one thread at a time.
-The other threads will wait for the lock owner to complete its task and return it.
-Thanks to the Lock mechanism, it is possible to control the competition between the various
threads, ensuring that each one of them performs its activities without the unwanted interference
of the other threads.
-There are a number of functions for using locks within a program. The `acquire` and `release`
functions, for example, have the task of having the lock acquired and released.
-If the thread with the lock will never release it, the program will remain locked, and it will
cause a deadlock.
-Deadlocks normally occur in one of the following cases:
    -A bad implementation of threads where a Lock is not released properly
    -A problem in the design scheme of a program that does not correctly foresee all the possible
    calls from the blocked threads waiting for the lock, and that are necessary for the completion
     of the thread with the lock.


SHARED STATE IN THREADS
-Atomic operations in concurrent programming are program operations that run completely
independently of any other processes, so they can not be interrupted during the operation.
-To deal with shared state in multithreading, we can use the queue module.
-The queue module implements multi-producer, multi-consumer queues:
    -A queue is a linear data structure that stores items in "First In First Out" (FIFO) manner.
    -To create a queue object, we can use the queue.Queue construct.


COROUTINES
-Coroutines are a more generalized form of subroutines.
-While subroutines are entered at one point and exited at another point, coroutines can be
entered, exited, and resumed at many different points.
-They can be implemented with the async def statement.
-Coroutines (a central feature of async IO) can be scheduled concurrently, but they are not
inherently concurrent.


ASYNCIO
-Asyncio is a library to write concurrent code using the async/await syntax.
-Async IO is a single-threaded, single-process design that uses cooperative multitasking.
-With asyncio you can create asynchronous routines are able to “pause” while waiting on their
ultimate result and let other routines run in the meantime.
-Basic keywords:
    -async:
        -The syntax async def introduces either a native coroutine or an asynchronous generator.
        -The expressions async with and async for are also valid, and you’ll see them later on.
    -await:
        -The keyword await passes function control back to the event loop (It suspends the
        execution of the surrounding coroutine).
        -When you call await, the function you're in gets suspended while whatever you asked to
        wait on happens, and then when it's finished, the event loop will wake the function up
        again and resume it from the await call, passing any result out.
-There’s also a strict set of rules around when and how you can and cannot use async/await.
    -A function that you introduce with async def is a coroutine. It may use await, return, or
    yield, but all of these are optional.
        -Using await and/or return creates a coroutine function.
        -To call a coroutine function, you must await it to get its results.
        -It is less common (and only recently legal in Python) to use yield in an async def block.
        This creates an asynchronous generator, which you iterate over with async for.
        -Anything defined with async def may not use yield from, which will raise a SyntaxError.
    -Just like it’s a SyntaxError to use yield outside a def function, it is a SyntaxError to use
    await outside an async def coroutine.
"""

import time
import asyncio
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from types import coroutine


# ----------------- LOCKS EXAMPLE -----------------

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = Lock()

    def update(self, name):
        print(f"Thread {name} is reading the DB value")
        with self._lock:
            print(f"Thread {name} has received the lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f"Thread {name} has modified the DB value")
            print(f"Thread {name} is releasing the lock")

database = FakeDatabase()

with ThreadPoolExecutor(max_workers=3) as executor:
    for index in range(3):
        executor.submit(database.update, index + 1)

print(f"DB Value is {database.value}")




# ----------------- COROUTINES -----------------

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')

friend_upper().send("hello")




# ----------------- ASYNCIO -----------------

"""
The execution will be as it follows:
1- When we execute main() function, it reaches result.
2- main() function pauses and gives back control to the event loop, which sees that get_chat_id 
needs to run.
3- Event loop calls get_chat_it and then that calls await and gets suspended with a marker to 
resume it in 3 seconds.
4- Once it resumes, get_chat_id completes and returns a result.
5- That makes main() ready to run again and the event loop resumes it with the returned value.
"""

async def get_chat_id(name):
    await asyncio.sleep(3)
    return f"chat-{name}"

async def main():
    result = await get_chat_id("django-framework")
    print(result)
