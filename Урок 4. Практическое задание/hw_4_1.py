"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # Генератор списков работает быстрее всех, поэтому применила именно его
    new_arr = [el for el in nums if el % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = list(filter(lambda x: x % 2 == 0, nums))  # функции map и filter в целом работают сильно быстре
    return new_arr  # но скорость сильно падает из-за list


def func_4(nums):
    new_arr = list(map(lambda x: x % 2 == 0, nums))
    return new_arr


lst = [1, 2, 3, 4, 5, 6]
print(timeit("func_1(lst)", globals=globals()))
print(timeit("func_2(lst)", globals=globals()))
print(timeit("func_3(lst)", globals=globals()))
print(timeit("func_4(lst)", globals=globals()))
