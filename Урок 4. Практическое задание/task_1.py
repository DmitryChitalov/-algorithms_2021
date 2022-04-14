#!/usr/bin/env python3


from timeit import timeit


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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in nums if i % 2 == 0]


array = list(range(1000))

print (timeit("func_1(array)", globals=globals(), number=10000))
print (timeit("func_2(array)", globals=globals(), number=10000))

'''Заменил цикл на list comprehension тем самым увеличив скорость выполнение т.к lc исполняется быстрее'''
