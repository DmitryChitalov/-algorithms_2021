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
    yield [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    """
     list comprehension
    """
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]  # list comprehension


numbers_10 = [i for i in range(10)]
print('*' * 15, '10', '*' * 15)
print('Цикл', timeit('func_1(numbers_10)', globals=globals(), number=100000))
print('Генератор', timeit('func_2(numbers_10)', globals=globals(), number=100000))
print('list comprehension', timeit('func_3(numbers_10)', globals=globals(), number=100000))

numbers_100 = [i for i in range(100)]
print('*' * 15, '100', '*' * 15)
print('Цикл', timeit('func_1(numbers_100)', globals=globals(), number=100000))
print('Генератор', timeit('func_2(numbers_100)', globals=globals(), number=100000))
print('list comprehension', timeit('func_3(numbers_100)', globals=globals(), number=100000))

numbers_1000 = [i for i in range(1000)]
print('*' * 15, '1000', '*' * 15)
print('Цикл', timeit('func_1(numbers_1000)', globals=globals(), number=100000))
print('Генератор', timeit('func_2(numbers_1000)', globals=globals(), number=100000))
print('list comprehension', timeit('func_3(numbers_1000)', globals=globals(), number=100000))

# *************** 10 ***************
# Цикл 0.14025590000000002
# Генератор 0.024571200000000015
# list comprehension 0.1445115
# *************** 100 ***************
# Цикл 1.066071
# Генератор 0.02440449999999994
# list comprehension 0.7710453999999998
# *************** 1000 ***************
# Цикл 11.4665025
# Генератор 0.021203800000000328
# list comprehension 9.841173999999999


# ВЫВОД: List comprehension позволяет оптимизировать  время, а генератор делает это еще быстрее поскольку
# он не хранит значения в памяти но его можно использовать лишь раз.
