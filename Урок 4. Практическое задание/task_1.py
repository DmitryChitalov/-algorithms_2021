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
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i, val in enumerate(nums) if val % 2 == 0]


nums_lst = random.sample(range(100000), 10000)

print(f'func_1: {timeit("func_1(nums_lst)", globals=globals(), number=1000)}')  # 2.204342643
print(f'func_2: {timeit("func_1(nums_lst)", globals=globals(), number=1000)}')  # 2.140081592
print(f'func_3: {timeit("func_1(nums_lst)", globals=globals(), number=1000)}')  # 2.157549899

"""
2 и 3 варианты быстрее первого, т.к. в них используется list comprehension.
При этом второй вариант быстрее третьего, вероятно из-за генерации кортежей в 3 варианте, 
вместо использования существующего индекса элементов списка во втором варианте.
"""