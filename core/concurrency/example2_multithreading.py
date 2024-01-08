import queue
import random
import time
from threading import Thread



counter = 0
counter_queue = queue.Queue()  # a queue of the amounts in counter
job_queue = queue.Queue()      # a queue of objects to be printed out


def increment_manager():
    global counter
    while True:
        # Get element in counter_queue
        # Waits until an item is available and locks the queue
        increment = counter_queue.get()
        time.sleep(random.random())
        # Increment counter
        counter += increment
        time.sleep(random.random())
        # Add result to output queue
        job_queue.put((f'New counter value {counter}', '------------'))
        time.sleep(random.random())
        # Unlock the queue
        counter_queue.task_done()

def increment_counter():
    # Add integer 1 to the queue
    counter_queue.put(1)
    counter_queue.put(3)
    time.sleep(random.random())

def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        # Unlock the queue
        job_queue.task_done()


# Declare threads object
# daemon=True allows threads to run continuously
manager_thread = Thread(target=increment_manager, daemon=True)
printer_thread = Thread(target=printer_manager, daemon=True)
worker_threads = [Thread(target=increment_counter) for thread in range(10)]

"""
If we would use ThreadPoolExecute instead of worker_threads
with ThreadPoolExecutor(max_workers=10) as pool:
    [pool.submit(increment_counter) for x in range(10)]
"""


# Start threads
manager_thread.start()  # execute increment_manager() continuously
printer_thread.start()  # execute printer_manager() continuously


for thread in worker_threads:
    time.sleep(random.random())
    thread.start()
    thread.join()  # wait for it to finish


# Block until all items in the Queue have been gotten and processed and queue is empty
counter_queue.join()
job_queue.join()
