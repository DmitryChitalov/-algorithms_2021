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
from timeit import timeit

setup = """
from __main__ import func_1, func_2, func_3, func_4
from random import randint
nums = [i for i in range(100)]
"""


def func_1(nums):
    """Сложность O(n)"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """Сложность O(n)"""
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    """Сложность O(n)"""
    new_arr = []
    for i in enumerate(nums):
        if i[1] % 2 == 0:
            new_arr.append(i[0])
    return new_arr


def func_4(nums):
    new_arr = list(filter(even_fn, nums))
    return new_arr


def even_fn(x):
    return x % 2 == 0


print("Исходная функция   ", timeit("func_1(nums)", setup, number=1000))
print("List Comprehension ", timeit("func_2(nums)", setup, number=1000))
print("Enumerate          ", timeit("func_3(nums)", setup, number=1000))
print("Filter             ", timeit("func_4(nums)", setup, number=1000))


"""
Проведены замеры времени.
В качестве дополнительного решения поставленной задачи выбрана встроенная функция filter.
Результаты:

Исходная функция    0.026812399999999986
List Comprehension  0.025412600000000007
Enumerate           0.0434957
Filter              0.038406300000000004
"""
