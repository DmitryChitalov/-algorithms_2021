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
# Замеры сделаны, потренировано несколько вариантов, смысл понятен. В качестве оптимизации проход по всему списку
# заменили на list comprehension с функциец enumerate, стало быстрее, но попытка еще упростить потерпела фиаско,
# filter от enumerate оставляет список кортежей, чтобы получить чистый список индексов, придется заворачивать все
# в дополнительный map и доставать первый элемент из каждой пары, что добавит еще времени.

from random import randint
from timeit import timeit, repeat, default_timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [number for number, el in enumerate(nums) if el % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = list(filter(lambda x: x if x[1] % 2 == 0 else None,  enumerate(nums)))
    return new_arr


nums = [randint(1, 5000) for el in range(1, 100000)]

print(timeit("func_1(nums)", globals=globals(), number=100))
print(timeit("func_2(nums)", globals=globals(), number=100))
print(timeit("func_3(nums)", globals=globals(), number=100))


setup = """
from random import randint
nums = [randint(1, 5000) for el in range(1, 100000)]
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
def func_2(nums):
    new_arr = [number for number, el in enumerate(nums) if el % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = list(filter(lambda x: x if x[1] % 2 == 0 else None,  enumerate(nums)))
    return new_arr
"""

statements = ['func_1(nums)', 'func_2(nums)', 'func_3(nums)']

for st in statements:
    print(repeat(st, setup, default_timer, 3, 100))
