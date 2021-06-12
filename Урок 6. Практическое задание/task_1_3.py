import memory_profiler
from timeit import default_timer
from random import randint


def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return result, mem_usage, run_time
    return wrapper


@decor
def my_func_1():
    lst = [randint(-100, 100) for _ in range(1000000)]
    return lst


@decor
def my_func_2():
    for _ in range(1000000):
        yield randint(-100, 100)


result_1, memory_1, runtime_1 = my_func_1()
result_2, memory_2, runtime_2 = my_func_2()

print("Списковое включение")
print(f"Память: {memory_1} MiB, время: {runtime_1} сек")
print("Генератор")
print(f"Память: {memory_2} MiB, время: {runtime_2} сек")

"""
Списковое включение
Память: 23.578125 MiB, время: 1.6250658079999998 сек
Генератор
Память: 0.0 MiB, время: 0.10956155800000023 сек

Списковое включение проигрывает по занимаемой памяти генераторам, потому что 
при использовании генераторов мы получаем элементы только при обращении.
Генераторы выигрывают и по скорости.
"""