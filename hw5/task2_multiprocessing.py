import multiprocessing
from hw4.task2_context_manager import timer

N = 300000000


def simple_iteration():
    res = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


def several_for_loops():
    res = 0
    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    return res


def iterate_over_fifteen():
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    return res


def math_formula():
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    res = threes + fives - fifteens
    return res


def wrapper(func, queue):
    with timer(func.__name__):
        result = func()
        queue.put(result)


def run_all_calculations_in_parallel():
    tasks = [simple_iteration, several_for_loops, iterate_over_fifteen, math_formula]
    procs = []
    results = multiprocessing.Queue()
    for task in tasks:
        proc = multiprocessing.Process(target=wrapper, args=(task, results))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()


if __name__ == '__main__':
    run_all_calculations_in_parallel()
