"""
BASIC CONCEPTS:
-Concurrency is when two or more tasks can start, run, and complete in overlapping time periods. It doesn't necessarily
mean they'll ever both be running at the same instant. For example, multitasking on a single-core machine.
-Parallelism is when tasks literally run at the same time, e.g., on a multicore processor.
-concurrent.futures module provides a high-level interface for asynchronously executing callables for both
multithreading and multiprocessing


PYTHON GIL:
-Each Python process creates a key resource, so only one thread can run in a process at a time.
-The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold
the control of the Python interpreter.


PROGRAMMING RESOURCES (CPU-I/O-Memory/Cache):
-A program is CPU-bound if the rate at which process progresses is limited by the speed of the CPU.
    -Example: a task that performs calculations on a small set of numbers, like multiplying small matrices.
-A program is I/O-bound if the rate at which a process progresses is limited by the speed of the I/O subsystem.
    -Example: a task that processes data from disk, like counting the number of lines in a file.
-A program is memory-bound if the rate at which a process progresses is limited by the amount memory available and
the speed of that memory access.
    -Example: a task that processes large amounts of in memory data, like multiplying large matrices.
-A program is cache-bound if the rate at which a process progress is limited by the amount and speed of the cache.
    -Example: a task that simply processes more data than fits in the cache will be cache bound.


THREADS
-A Thread is an execution unit that is part of a process.
-Do not kill threads, it can end in a deadlock (see 03-Advanced multithreading.py for more information)


LIBRARIES FOR MULTITHREADED PROGRAMMING
-threading module constructs higher-level threading interfaces on top of the lower level _thread module.
(See also the queue module.)
-ThreadPoolExecutor (in concurrent.futures package) is an Executor subclass that uses a pool of threads to execute
calls asynchronously.
"""

import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor



# DATA
def ask_user():
    start_time = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print('ask_user: ', time.time() - start_time)


def complex_calculation():
    start_time = time.time()
    print('Started calculating...')
    calculation = [x ** 2 for x in range(20000000)]
    print(f'Complex_calculation: {time.time() - start_time}')
    return calculation






# ----------------- THREADS EXAMPLE -----------------

# Single-threaded execution
start = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}\n\n')


# Multithreaded execution
start = time.time()

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Two thread total time: {time.time() - start}')


# Multithreaded execution using concurrent.futures
start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)
    # All this does is we don't have to call pool.shutdown()

print(f'Two thread total time: {time.time() - start}')
