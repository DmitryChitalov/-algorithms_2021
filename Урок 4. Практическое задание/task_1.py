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


from timeit import timeit


nums = [i for i in range(9999)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit(stmt="func_1(nums)",
             setup="from __main__ import func_1, nums",
             number=1000))


# list comprehension
def func_2(nums):
    return [i for i in nums if i % 2 == 0]


print(timeit(stmt="func_2(nums)",
             setup="from __main__ import func_2, nums",
             number=1000))


'''
Списковое включение работает быстрее, чем итератор с методом append
func_1 - 0.85
func_2 - 0.40
'''
