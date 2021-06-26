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
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


"""
используем List Comprehension, так как это встроенный механизм 
построения списков, и он будет работать быстрее
"""


def func_2(nums):
    return [i for i, num in enumerate(nums) if num % 2 == 0]


numbers = [randint(0, 100) for i in range(1000)]

print(timeit('func_1(numbers)', globals=globals(), number=10000))
print(timeit('func_2(numbers)', globals=globals(), number=10000))
