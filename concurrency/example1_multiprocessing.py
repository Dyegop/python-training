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
