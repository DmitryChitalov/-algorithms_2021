from memory_profiler import memory_usage
from timeit import default_timer


def decor(func):
    """Декоратор, для получения занимамой памяти и времени."""
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        t1 = default_timer()
        res = func(*args, **kwargs)
        t2 = default_timer()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = t1 - t2
        print(f"Время работы функции {func.__name__}, составило: {time_diff:0.8f} сек.")
        print(f"Выполнение функции {func.__name__}, заняло: {mem_diff} Mib.")
        return res
    return wrapper