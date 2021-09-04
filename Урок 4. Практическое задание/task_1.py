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


nums = [i for i in range(10000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit.timeit('func_1(nums)', globals=globals(), number=1000))


def mod_func_1(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(timeit.timeit('mod_func_1(nums)', globals=globals(), number=1000))

"""
Вывод: Для оптимизации кода стоит использовать list comprehension, согласно замерам это снизит время его выполнения 
приблизительно на 20 %.
"""
