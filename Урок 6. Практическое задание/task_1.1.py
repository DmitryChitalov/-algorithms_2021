"""
Задание.
Создать список кубов нечетных чисел до 1000 (сделал больше в виду того чтобы
было более наглядно) но до 1000 выдает почти все нули.
"""
from task_1 import memory_time_profiler
from numpy import array


@memory_time_profiler
def num_1():           # цикл
    new_list_1 = []
    for i in range(1, 10000, 2):
        i = i ** 3
        new_list_1.append(i)
    return new_list_1


@memory_time_profiler
def num_2():            # list comprehension
    return [i ** 3 for i in range(1, 10000, 2)]


@memory_time_profiler
def num_3():        # использование array из библиотеки numpy
    return array([i ** 3 for i in range(1, 10000, 2)])


@memory_time_profiler
def num_4():        # использование встроенной функции map
    return list(map(int, [i ** 3 for i in range(1, 10000, 2)]))


print(num_3())
print(num_2())
print(num_1())
print(num_4())

"""
как показывают замеры использование map и array лучше при создании списков.
цикл - 'Использовано памяти: 0.29296875 , выполнено за: 0.11018460000000002'
lc - 'Использовано памяти: 0.125 , выполнено за: 0.10797129999999999'
array - 'Использовано памяти: 0.0 , выполнено за: 0.10996709999999998'
map - 'Использовано памяти: 0.125 , выполнено за: 0.10811739999999981'
не совсем понятно почему array дал "Использование памяти: 0.0"
"""
