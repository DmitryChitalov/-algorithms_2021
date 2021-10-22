import copy
from numpy import array
from random import randint
from functools import wraps
from memory_profiler import memory_usage, profile
from pympler import asizeof
import timeit
import json

# Первый скрипт

# 1
random_num = [el + randint(0, 10) for el in range(10000)]

# 2
random_num_array = array([el + randint(0, 10) for el in range(10000)])

# 3
random_num_map = list(map(int, [el + randint(0, 10) for el in range(10000)]))

print(f'Без дополнительных функций: {asizeof.asizeof(random_num)}')
print(f'Использование c array: {asizeof.asizeof(random_num_array)}')
print(f'Использование с map: {asizeof.asizeof(random_num_map)}')
print()

# При использовании array видно, что объем используемой памяти значительно уменьшился.
# При использовании map, эта разницы почти нет, но всё же снизился объем используемой памяти.
# 402328
# 40120
# 402168


# Второй скрипт

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        func(*args, **kwargs)
        m2 = memory_usage()
        return m2[0] - m1[0]
    return wrapper


@decorator
def with_list(list_arg):
    new_list = [item**2 for item in list_arg]
    return new_list


@decorator
def with_generator(list_arg):
    for item in list_arg:
        yield item**2


list_to_test = list(range(1000))
print(f'Использование с функцией list: {with_list(list_to_test)}')
print(f'Использование с генератора: {with_generator(list_to_test)}')

'''
Вывод
Декоратор memory_decorator считает количество памяти которую использует переданная ему функция.
Итак, функция которая генерирует новый список и возвращает его занимает определенный объем памяти.
При старте скрипта видно, что функции которая использует генератор достаточно выделенной памяти.
Из этого сделует, что функция с генератором потребляет меньше памяти, поэтому лучше использовать её.
0.0390625
0.0
'''

# Третий скрипт

@profile
def func_1(list_arg):
    original_list = [item * 2 for item in list_arg]
    new_list = original_list
    del original_list
    return new_list


list_to_test_2 = list(range(100000))
func_1(list_to_test_2)

'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    83     23.4 MiB     23.4 MiB           1   @profile
    84                                         def func_1(list_arg):
    85     28.3 MiB      4.9 MiB      100003       original_list = [item * 2 for item in list_arg]
    86     28.3 MiB      0.0 MiB           1       new_list = original_list
    87     28.3 MiB      0.0 MiB           1       del original_list
    88     28.3 MiB      0.0 MiB           1       return new_list
'''


@profile
def func_2(list_arg):
    original_list = [item * 2 for item in list_arg]
    new_list = original_list
    del original_list
    del new_list
    new_list = []
    return new_list


func_2(list_to_test_2)

'''
Вывод:
В данном результате видим что при удаленние всех ссылок на один и тот же объект память освобождается.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   106     24.4 MiB     24.4 MiB           1   @profile
   107                                         def func_2(list_arg):
   108     28.3 MiB  -2793.4 MiB      100003       original_list = [item * 2 for item in list_arg]
   109     28.3 MiB      0.0 MiB           1       new_list = original_list
   110     28.3 MiB      0.0 MiB           1       del original_list
   111     25.0 MiB     -3.3 MiB           1       del new_list
   112     25.0 MiB      0.0 MiB           1       new_list = []
   113     25.0 MiB      0.0 MiB           1       return new_list
'''
