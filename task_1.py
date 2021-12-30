# 123
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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    # написал итератор в одну строку (ls)
    return [v for v, k in enumerate(nums) if k % 2 == 0]


nums = [l for l in range(1000)]

print(timeit.timeit('func_1(nums[:])', globals=globals(), number=1000))

print(timeit.timeit('func_2(nums[:])', globals=globals(), number=1000))

# LC работают быстрее чем обычные итераторы, примерно на 20-25%









