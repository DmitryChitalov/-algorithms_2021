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

random_list = [randint(0, 100) for i in range(10)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print('Время до оптимицации:', timeit("func_1(random_list)", globals=globals(), number=100000))


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


print('Время после оптимицации:', timeit("func_2(random_list)", globals=globals(), number=100000))

""" 
Списковое включение отрабатывает бестрее, чем добавление индексов с помощью 
append в цикле. Еще один плюс - компактность кода.

Время до оптимицации: 0.24483026599999996
Время после оптимицации: 0.194721078
"""