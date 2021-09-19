from more_itertools import islice_extended, ilen
from pympler import asizeof
import memory_profiler




def decorator(func):
    def wrapper(*args, **kwargs):
        mem_1 = memory_profiler.memory_usage()
        res = func(*args, **kwargs)
        mem_2 = memory_profiler.memory_usage()
        mem_diff = mem_2[0] - mem_1[0]
        return res, mem_diff

    return wrapper



@decorator
def fun():
    """
    Подсчет значений кратное 3-м
    """
    print(ilen(x for x in range(1000000) if x % 3 == 0))



@decorator
def fun2():
    """
    Подсчет значений кратное 3-м
    """
    print(len(x for x in range(1000000) if x % 3 == 0))


res, mem_diff = fun()
print(f"Выполнение заняло {mem_diff} Mib")
print(asizeof.asizeof(res))


res, mem_diff = fun2()
print(f"Выполнение заняло {mem_diff} Mib")
print(asizeof.asizeof(res))

"""
333334
Выполнение заняло 0.00390625 Mib
16

333334
Выполнение заняло 1.1796875 Mib
16

Первая функция - fun оказалась намного экономней по памяти, чем первая.
"""