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
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


n = [randint(0, 1000) for i in range(500)]

print('Выполнение первой функции составило', timeit.repeat("func_1(n)", globals=globals(), repeat=3, number=1000))
print('Выполнение второй функции составило', timeit.repeat("func_2(n)", globals=globals(), repeat=3, number=1000))


# Я использовала для второго варианта LC, замеры показали, что он быстрее, что логично, т.к. не нужно создавать
# промежуточный список и нет метода append()
