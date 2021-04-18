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


nums = list(range(10000))

print(f"Не оптимизированная: {timeit.timeit('func_1(nums)', globals=globals(), number=10000)}")


def func_1_modified(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr

print(f"Оптимизированная: {timeit.timeit('func_1_modified(nums)', globals=globals(), number=10000)}")

# Функция func_1_modified выполняется быстрее примерно в два раза. Это происходит из-за того, что нет функции append,
# а использован list comprehension, что оптимальнее.