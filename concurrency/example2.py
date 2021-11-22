"""
concurrent.futures module is a simpler interface that works very much the same regardless of whether you use multiple
threads or multiple processes as the underlying parallelization gimmick.

Executor objects: class concurrent.futures.Executor
An abstract class that provides methods to execute calls asynchronously. It should not be used directly, but through
its concrete subclasses.

"""

import time
import concurrent.futures



# EXAMPLE OF CONCURRENT FUTURES

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'




if __name__ == '__main__':

    # Initializes a new ProcessPoolExecutor instance
    with concurrent.futures.ProcessPoolExecutor() as executor:
        p1 = executor.submit(do_something, 1)  # 1 second as parameter seconds
        p2 = executor.submit(do_something, 5)  # 5 second as parameter seconds

        for f in concurrent.futures.as_completed([p1, p2]):
            print(f.result())

        # Creating process with list comprehension
        # results = [executor.submit(do_something, 1) for _ in range(17)]
        # as_completed(f) - An iterator over the given futures that yields each as it completes
        # for f in concurrent.futures.as_completed(results):
        #    print(f.result())
        print("\n")


        # Creating process using map function
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)
        for result in results:
            print(result)
        print("\n")


    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
