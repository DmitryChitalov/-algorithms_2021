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
import random

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [x for x in nums if x % 2 == 0]


random_list = random.sample(range(0, 100), 15)
my_list = (2, 5, 7, 18, 27, 346, 547, 1434, 5649)
print(my_list)

print(
    timeit(
        "func_1(my_list)",
        setup='from __main__ import func_1, my_list',
        number=10000))

print(
    timeit(
        "func_2(my_list)",
        setup='from __main__ import func_2, my_list',
        number=10000))

print("#############################")

print(
    timeit(
        "func_1(random_list)",
        setup='from __main__ import func_1, random_list',
        number=10000))

print(
    timeit(
        "func_2(random_list)",
        setup='from __main__ import func_2, random_list',
        number=10000))
""" 
Вторая функция оптимизированна. Она выполняется быстрее т.к. она не создает 
новый список и не добавляет в него подхдящие элементы. Вторая функция работает  
как генератор. 
"""
