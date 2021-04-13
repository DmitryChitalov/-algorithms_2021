"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
import timeit
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return [i for i, el in enumerate(nums) if not el % 2]


arr = [randint(1, 10000) for _ in range(3000)]
print('nums:', arr)
print('func_1', func_1(arr))
print('func_2', func_2(arr))
print('func_3', func_3(arr))

print('\n**********************************\n')

print('func_1', timeit.repeat(stmt="func_1(arr)", setup="from __main__ import func_1, arr", number=10000))
print('func_2', timeit.repeat(stmt="func_2(arr)", setup="from __main__ import func_2, arr", number=10000))
print('func_3', timeit.repeat(stmt="func_3(arr)", setup="from __main__ import func_3, arr", number=10000))


# 1. Для оптимизации испозован генератор списка, он работает быстрее обычного перебора for in
# 2. Используется функция enumerate вместо range() и len() - меньше вызовов функций
# 3. Вместо сравнения результата деления по модулю с нулем используется логический оператор НЕ,
# что уменьшает количество операций
