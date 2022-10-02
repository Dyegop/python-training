"""
BASIC CONCEPTS:
-Concurrency is when two or more tasks can start, run, and complete in overlapping time periods. It doesn't necessarily
mean they'll ever both be running at the same instant, so no parallelism is implied.
-Parallelism consists of performing multiple operations at the same time.
-Multiprocessing entails spreading tasks over a computer’s central processing units (CPUs, or cores).
-Multithreading is a concurrent execution model whereby multiple threads take turns executing tasks.


PROCESSES AND THREADS
-Process:
    -A Process is an execution unit in concurrent programming and can have multiple threads, all executing at the same time.
    -Due to the way Windows forks processes, you must make sure that the code that starts a process is surrounded by
    if __name__ == "__main__".
-Threads:
    -A Thread is an execution unit that is part of a process.
    -Do not kill threads, it can end in a deadlock (see 02-Concurrency - advanced.py for more information)
-Some key differences between Processes and Threads:
    -Process means a program is in execution - Thread means a segment of a process.
    -Processes are not lightweight - Threads are Lightweight
    -Processes take more time to terminate and for creation - Threads take less time for both.
    -Processes likely take more time for context switching - Threads take less time.
    -Processes are mostly isolated - Threads share memory.
    -Processes do not share data - Threads share data with each other.


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


LIBRARIES FOR CONCURRENCY
-concurrent.futures: a module that provides a high-level interface for asynchronously executing callables for both
multithreading and multiprocessing
    -ThreadPoolExecutor (in concurrent.futures package) is an Executor subclass that uses a pool of threads to execute
    calls asynchronously.
    -ProcessPoolExecutor (in concurrent.futures package) is an Executor subclass that uses a pool of processes to
    execute calls asynchronously with the use of the multiprocessing module, which allows it to side-step the GIL but
    also means that only picklable objects can be executed and returned.
-threading: a module that constructs higher-level threading interfaces on top of the lower level _thread module.
(See also the queue module.)
-multiprocessing: a package that supports spawning processes using an API similar to the threading module. The
multiprocessing package offers both local and remote concurrency, effectively side-stepping the GIL by using
subprocesses instead of threads.
"""

import time
from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor



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






# -----------------PROCESS EXAMPLE-----------------

# Since process don't share resources, we can not use a process for ask_user() because that process won't be able to
# read from command-line
# Instead, we can execute multiple calls of complex_calculation() that will run at the same time faster than
# in single-processing

# Single-processed execution
start = time.time()
complex_calculation()
complex_calculation()
print(f'Single process total time: {time.time() - start}\n\n')


# Multiprocessed execution
start = time.time()
process1 = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)

process1.start()
process2.start()

process1.join()  # this waits for the process to finish
process2.join()

print(f'Two process total time: {time.time() - start}')


# Multiprocessing execution using concurrent.futures
with ProcessPoolExecutor(max_workers=2) as pool:
	pool.submit(complex_calculation)
	pool.submit(complex_calculation)

print(f'Two process total time: {time.time() - start}')
