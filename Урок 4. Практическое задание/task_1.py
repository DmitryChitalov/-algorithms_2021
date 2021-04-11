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
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [idx for idx, el in enumerate(nums) if el % 2 == 0]


nums = [randint(-100, 100) for _ in range(10)]
print(f'{timeit("func_1(nums)", globals=globals(), number=1000)} func_1')
print(f'{timeit("func_2(nums)", globals=globals(), number=1000)} func_2')
# 0.0036790999999999976 func_1
# 0.001935100000000002 func_2
# func_2 быстрее так как отсутствует операция append
