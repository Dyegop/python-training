"""
BASIC CONCEPTS
-Concurrency is when two or more tasks can start, run, and complete in overlapping time periods. It doesn't necessarily
mean they'll ever both be running at the same instant. For example, multitasking on a single-core machine.
-Parallelism is when tasks literally run at the same time, e.g., on a multicore processor.

-CPU Bound means the rate at which process progresses is limited by the speed of the CPU. A task that performs
calculations on a small set of numbers, for example multiplying small matrices, is likely to be CPU bound.
-I/O Bound means the rate at which a process progresses is limited by the speed of the I/O subsystem. A task that
processes data from disk, for example, counting the number of lines in a file is likely to be I/O bound.
-Memory bound means the rate at which a process progresses is limited by the amount memory available and the speed of
that memory access. A task that processes large amounts of in memory data, for example multiplying large matrices, is
likely to be Memory Bound.
-Cache bound means the rate at which a process progress is limited by the amount and speed of the cache available.
A task that simply processes more data than fits in the cache will be cache bound.

-The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold
the control of the Python interpreter.


PYTHON LIBRARIES FOR MULTITHREADED PROGRAMMING
-concurrent.futures module provides a high-level interface for asynchronously executing callables
    -ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously.
    -The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes to execute calls
    asynchronously. ProcessPoolExecutor uses the multiprocessing module, which allows it to side-step the Global
    Interpreter Lock but also means that only picklable objects can be executed and returned.
-multiprocessing is a package that supports spawning processes using an API similar to the threading module.
The multiprocessing package offers both local and remote concurrency, effectively side-stepping the GIL by using
subprocesses instead of threads.
-threading module constructs higher-level threading interfaces on top of the lower level _thread module.
See also the queue module.

"""

import time
import multiprocessing



# EXAMPLE OF MULTIPROCESSING


start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'




if __name__ == '__main__':
    # Print number of CPUs
    print(multiprocessing.cpu_count())


    # Create a subprocess
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)


    # Create subprocess using for loop
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=(1.5,))
        # Start child process
        p.start()
        processes.append(p)

    # Wait until child process terminates
    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
