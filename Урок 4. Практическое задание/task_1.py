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
    return [i for i, num in enumerate(nums) if num % 2 == 0]


def func_4(nums):
    return [i for i, num in enumerate(nums) if not num % 2]


numbers = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

print('func_1:', timeit('func_1(numbers)', globals=globals()))
print('func_2:', timeit('func_2(numbers)', globals=globals()))
print('func_3:', timeit('func_3(numbers)', globals=globals()))
print('func_4:', timeit('func_4(numbers)', globals=globals()))

"""
Результаты:
func_1: 1.3823189
func_2: 1.2108370000000002
func_3: 1.1069215000000003
func_4: 1.0592429
Между первыми двумя функциями незначительная разница в скорости работы.
Третья выполняется чуть быстрее.
Быстрее всего выполняется четвёртый вариант.
"""
