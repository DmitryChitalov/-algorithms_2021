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

def func_2(nums):
    new_arr = [num for num , val in enumerate(nums, 0) if val % 2 == 0]
    return new_arr

nums = [2,3,4,5,6,7,8,9,9, 8, 5, 5, 10, 10, 11, 21, 22]
print(timeit("func_1(nums)", globals=globals(), number=10000000))
print(timeit("func_2(nums)", globals=globals(), number=10000000))

"""
14.610225253000001
12.887586676999998

Как выяснили на уроке списковое создание массива работает чуть быстрее, чем добавление элементов в цикле