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


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i, j in enumerate(nums) if j % 2 == 0]


numbers = [i for i in range(300)]
print(f'Время выполнения 1 функции: {timeit.repeat("func_1(numbers)", globals=globals(), repeat=3, number=20000)}')
print(f'Время выполнения 2 функции: {timeit.repeat("func_2(numbers)", globals=globals(), repeat=3, number=20000)}')
print(f'Время выполнения 3 функции: {timeit.repeat("func_3(numbers)", globals=globals(), repeat=3, number=20000)}')

# Разница в вычислении двух функции func_1 и func_2 составила примерно 17% процентов (func_2 - лучше).
# В функции func_1 был цикл, внутри которого вычисление операнда append. В функции func_2 вообще используется выражение
# в одну строку и используется списковое включения и функции range. Но лучшим похожим решением на func_2
# стало решение func_3 с использованием enumerate в моем случае.
