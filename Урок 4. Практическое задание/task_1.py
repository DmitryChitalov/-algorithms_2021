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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [idx for idx in range(len(nums)) if nums[idx] % 2 == 0]


def func_3(nums):
    new_list = list(filter(lambda idx: nums[idx] % 2 == 0, range(len(nums))))
    return new_list


old_list = [1, 2, 2, 3, 4, 5, 6, 8, 5, 4, 5, 5, 4]
print(func_1(old_list))
print(func_2(old_list))
print(func_3(old_list))

print(f'Time for func_1: {timeit("func_1(old_list)", globals=globals(), number=10000)}')
print(f'Time for func_2: {timeit("func_2(old_list)", globals=globals(), number=10000)}')
print(f'Time for func_3: {timeit("func_3(old_list)", globals=globals(), number=10000)}')

"""
Резльтуты: 
    func_1 - [1, 2, 4, 6, 7, 9, 12]
    func_2 - [1, 2, 4, 6, 7, 9, 12]
    func_3 - [1, 2, 4, 6, 7, 9, 12]
    Time for func_1: 0.011375439000403276
    Time for func_2: 0.009525399000267498
    Time for func_3: 0.015828613000849145
    Самое долгое решение через лямбда-функцию, т.к перегружена методом list и функцией filter, 
    без чего лямбда не работает по ТЗ.
    Решение в исходном примере (func_1) на втором месте, и самое быстрое через импользование list comprehension.
"""