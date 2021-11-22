"""
PROCESSES
-A Process is an execution unit in concurrent programming and can have multiple threads, all executing at the same time.
-Due to the way Windows forks processes, you must make sure that the code that starts a process is surrounded by
if __name__ == "__main__".
-Some key differences between Processes and Threads:
	-Process means a program is in execution - Thread means a segment of a process.
	-Processes are not lightweight - Threads are Lightweight
	-Processes take more time to terminate and for creation - Threads take less time for both.
	-Processes likely take more time for context switching - Threads take less time.
	-Processes are mostly isolated - Threads share memory.
	-Processes do not share data - Threads share data with each other.


LIBRARIES FOR MULTIPROCESSING PROGRAMMING
-multiprocessing is a package that supports spawning processes using an API similar to the threading module.
	-The multiprocessing package offers both local and remote concurrency, effectively side-stepping the GIL by using
	subprocesses instead of threads.
-ProcessPoolExecutor (in concurrent.futures package) class is an Executor subclass that uses a pool of processes to
execute calls asynchronously.
	-ProcessPoolExecutor uses the multiprocessing module, which allows it to side-step the Global
	Interpreter Lock but also means that only picklable objects can be executed and returned.
"""

import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor



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
