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

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [el for el in nums if el % 2 == 0]
    return new_arr


print(timeit("func_1(list1)", globals=globals(), number=1000000))
print(timeit("func_2(list1)", globals=globals(), number=1000000))

'''Функция через генератор списка более быстрая
func_1: 2.3622489
func_2: 1.6321436000000005
'''
