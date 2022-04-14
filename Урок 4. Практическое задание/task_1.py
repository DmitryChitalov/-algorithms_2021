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


def insert_in_list(n):      # вспомогательная функция для заполнения списка, который нужен для теста функции func_1
    new_lst = []
    for i in range(1, n):
        new_lst.append(i)
    return new_lst


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


test_lst = insert_in_list(1000)

print('Функция func_1')
print(
    timeit(
        "func_1(test_lst)",
        setup='from __main__ import func_1, test_lst',
        number=10000))

print('Функция func_2')
print(
    timeit(
        "func_2(test_lst)",
        setup='from __main__ import func_2, test_lst',
        number=10000))

"""
Функция func_1
0.7313297999999999
Функция func_2
0.5751326999999999
Для сокращения времени работы функции применил списковое включение, так как list comprehension быстрее for-циклов, 
которые он и заменяет. Некоторые источники прямо указывают, что замена for-циклов на списковые включения - один из 
первых пунктов при рефакторинге Python-кода.
"""