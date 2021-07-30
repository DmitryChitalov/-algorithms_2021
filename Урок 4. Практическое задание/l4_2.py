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

from time import time as time
from random import randint as rand


def timer(func):
    def temporary(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        delta_time = time() - start_time
        print(f'Время выполнения функции {func.__name__} = {delta_time}')
        return result

    return temporary


@timer
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@timer
def optimize(nums):
    return [num for num, el in enumerate(nums) if num % 2 == 0]


@timer
def optimize_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


num_array = [rand(0, 100) for i in range(100000)]
num_array_1 = [rand(0, 100) for el in range(1000000)]
num_array_2 = [rand(0, 100) for z in range(10000000)]

for arr in [num_array_2, num_array_1, num_array]:
    func_1(arr)  # 2.0499491691589355, 0.19768786430358887, 0.016515493392944336
    # Самый медленный в силу последовательности действий.
    optimize(arr)  # 1.459388256072998, 0.13763213157653809, 0.010510683059692383
    # Самый быстрый в силу одновременности действий и замену обращения к индексам встроенной функцией enumerate.
    optimize_2(arr)  # 1.7861981391906738, 0.17016148567199707, 0.014013051986694336
    # Чуть более быстрый, чем первый способ в силу одноврменности действий.
