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

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def my_func_1(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


nums = [i for i in range(1000)]

# T1 = timeit.Timer("func_1(nums)", "from __main__ import func_1, nums")
# print(T1.timeit(number=100), " seconds")
print("First function time: ", timeit.timeit("func_1(nums)", globals=globals()), "secs")
print("My function time: ", timeit.timeit("my_func_1(nums)", globals=globals()), "secs")


# Программа работает на +-10 сек быстрее, добились оптимизировать работу программы. Я использовал list comprehension
# вместо функции .append, так как для создании список list comprehension самый оптимальный вариант