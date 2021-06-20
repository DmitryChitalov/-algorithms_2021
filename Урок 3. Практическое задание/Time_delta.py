from time import time


def time_delta(func):
    def g(n):
        start = time()
        r = func(n)
        stop = time()
        return r, f'Время выполнения: {stop - start}'

    return g
