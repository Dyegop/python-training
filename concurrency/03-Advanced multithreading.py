"""
LOCKS
-A Lock is an object that acts as a permit and will be assigned to only one thread at a time.
-The other threads will wait for the lock owner to complete its task and return it.
-Thanks to the Lock mechanism, it is possible to control the competition between the various threads, ensuring that
each one of them performs its activities without the unwanted interference of the other threads.
-There are a number of functions for using locks within a program. The acquire() and release() functions, for example,
have the task of having the lock acquired and released.
-If the thread with the lock will never release it, the program will remain locked and it will cause a deadlock.
-Deadlocks normally occur in one of the following cases:
    -A bad implementation of threads where a Lock is not released properly
    -A problem in the design scheme of a program that does not correctly foresee all the possible calls from the
    blocked threads waiting for the lock, and that are necessary for the completion of the thread with the lock.


SHARED STATE IN THREADS
-Atomic operations in concurrent programming are program operations that run completely independently of any other
processes, so they can not be interrupted during the operation.
-To deal with shared state in multithreading, we can use the queue module.
-The queue module implements multi-producer, multi-consumer queues:
    -A queue is a linear data structure that stores items in First In First Out (FIFO) manner.
    -To create a queue object, we can use the queue.Queue construct.


"""

import time
import queue
import random
from threading import Lock, Thread
from concurrent.futures import ThreadPoolExecutor



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






# ----------------- QUEUE THREADS EXAMPLE -----------------

# See example3.py
