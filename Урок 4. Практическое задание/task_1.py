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

"""
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
   """

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Measurements of code execution time*Замеры времени выполнения кода
elements = [i for i in range(200)]
print(timeit("func_1(elements)", globals=globals()))  # 13.3329138


# Algorithm optimization using list comprehension*Оптимизация алгоритма, используя list comprehension
def func_2(nums):
    new_arr = [el for el in nums if el % 2 == 0]
    return new_arr


# Runtime measurements after optimization*Замеры времени выполнения после оптимизации
print(timeit("func_2(elements)", globals=globals()))  # 8.2158034


"""
Using a list comprehension is faster than an iterator with an append method.
After optimization, the function works 1.62 times faster.
Использование list comprehension работает быстрее, чем итератор с методом append.
После оптимизации  функция работает быстрее в 1,62 раза.
"""
