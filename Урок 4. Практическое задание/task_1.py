"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
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
    return [i for i, value in enumerate(nums) if value % 2 == 0]


def func_4(nums):
    return filter(lambda i: nums[i] % 2 == 0, range(len(nums)))


n = [i for i in range(1000)]

print(f'func_1(n): {timeit("func_1(n)", globals=globals(), number=1000)}')
print(f'func_2(n): {timeit("func_2(n)", globals=globals(), number=1000)}')
print(f'func_3(n): {timeit("func_3(n)", globals=globals(), number=1000)}')
print(f'func_4(n): {timeit("func_4(n)", globals=globals(), number=1000)}')

"""
func_1(n): 0.0817406 - самый медленный способ. Классический цикл for
func_2(n): 0.06696840000000001 - list comprehension работает быстрее append, испульзует другой механизм
func_3(n): 0.06728319999999999 - list comprehension + enumerate работает медленне просто list comprehension
func_4(n): 0.0004704999999999848 - самое быстрое решение при помощи встроенной функции
"""
