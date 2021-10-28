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

from timeit import timeit
import random

list_for_test = [random.randint(1, 100) for i in range(10)]

print(list_for_test)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2_lc(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

def func_3_lc_enum(nums):
    new_arr = [ind for ind, num in enumerate(nums) if num % 2 == 0]
    return new_arr


print(timeit('func_1(list_for_test)', globals=globals( )))
print(timeit('func_2_lc(list_for_test)', globals=globals( )))
print(timeit('func_3_lc_enum(list_for_test)', globals=globals( )))

""" Лучший результат у функции c lc и enumirate, т. к. результат генерируется налету без добавления значений в массив
  отсутствия необходимости обращаться к элементам 
по индексам"""