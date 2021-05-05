"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""

from timeit import default_timer, timeit
from random import randint

our_test_line = [randint(-1000, 1000) for _ in range(20)]


def time_it(func):
    def wrapper(args):
        start_time = default_timer()
        func(args)
        print(default_timer() - start_time)

    return wrapper


@time_it
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@time_it  # Тестирование и замеры с истпользованием list comprehension.
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


@time_it  # Тестирование и замеры с использованием функции enumerate.
def func_3(nums):
    return [i for i, j in enumerate(nums) if j % 2 == 0]


func_1(our_test_line)
func_2(our_test_line)
func_3(our_test_line)

"""
Вывод и аналитика:

Использовал различные варианты для оптимизации выполнения задания с помощью встроенных инструментов языка Python.
Вариант с использованием list comprehension оказался существенно быстрее остальных двух.
А вариант с использованием функции enumerate оказался по моим замерам самым медленным. 
"""