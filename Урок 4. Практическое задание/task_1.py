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

nums = [i * i for i in range(100)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit("func_1(nums)", number=1500000, globals=globals()))


def func_1_mod(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


print(timeit("func_1_mod(nums)", number=1500000, globals=globals()))

# 11.742759642000001
# 9.680958492999999
# Вывод: В исходном коде используется итерация с методом append (большая сложность), а в моей версии
# я использовал list comprehension, что дало прибавку в скорости, так же код стал более красивым и стильным.
