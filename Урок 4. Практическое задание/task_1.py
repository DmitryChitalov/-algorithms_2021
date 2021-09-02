"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

import random
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    '''
    убрал доступ к элементу по индексу, вместо этого и индекс, и значение
    извлекаются за один проход
    '''
    new_arr = []
    for item, val in enumerate(nums):
        if val % 2 == 0:
            new_arr.append(item)
    return new_arr


def func_3(nums):
    '''
    логика такая же как и в func_2, но реализация через списковое включение
    дает самую быструю скорость
    '''
    new_arr = [item for item, val in enumerate(nums) if val % 2 == 0]
    return new_arr


lst = [random.randrange(1, 50, 1) for i in range(1000)]
print(timeit("func_1(lst)", globals=globals(), number=10000))
print(timeit("func_2(lst)", globals=globals(), number=10000))
print(timeit("func_3(lst)", globals=globals(), number=10000))
