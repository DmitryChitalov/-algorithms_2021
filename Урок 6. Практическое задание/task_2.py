"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
"""


from timeit import timeit
from numba import njit, prange
from memory_profiler import memory_usage
from pympler import asizeof
import cython_task_2


def memory_usage_decor(func):
    def wrapper(*args):
        mu_start = memory_usage()
        result = func(*args)
        mu_finish = memory_usage()
        mu_diff = mu_finish[0] - mu_start[0]
        return result, mu_diff
    return wrapper


@memory_usage_decor
def compose_list():
    multiplier = 10
    returned_value = []
    for index in range(100000):
        returned_value.append(index ** multiplier)
    return returned_value


base_cycle_result, mu_base_cycle = compose_list()
print(mu_base_cycle, asizeof.asizeof(base_cycle_result))

cython_cycle_result = cython_task_2.compose_list()

"""
Ниже приведен пример оптимизации времени заполнения массива с Numba. Понимаю, что не по теме, но для себя сохраню его 
здесь. Результаты:

Стандартный цикл: 0.7100344
Numba цикл:       0.17300879999999987
"""


def basic_func():
    result = []
    for i in range(10000000):
        result.append(i)


@njit(fastmath=True, cache=True,parallel=True)
def new_func():
    result = []
    for i in range(10000000):
        result.append(i)


# print(f'Стандартный цикл: {timeit("basic_func()", globals=globals(), number=1)}')
# print(f'Numba цикл: {timeit("new_func()", globals=globals(), number=1)}')
