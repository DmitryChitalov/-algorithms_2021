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
from random import choice


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [id_el for id_el, val in enumerate(nums) if val % 2 == 0]
    return new_arr


n = [choice([x for x in range(1000)]) for el in range(1000)]
print(f'Время первоначальной функции: {timeit("func_1(n)", globals=globals(), number=100000)}')
print(f'Время измененной функции: {timeit("func_2(n)", globals=globals(), number=100000)}')

'''
Измерения:
Время первоначальной функции: 22.308479400000003
Время измененной функции: 15.684319600000002
Мы ушли от работы с перебором индексов списка и их значением к работе только с самими значениями.
'''
