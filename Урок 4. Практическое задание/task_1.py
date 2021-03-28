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
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def fill_list(number_of_items):
    test_list = list(range(number_of_items))
    return test_list


numbers = fill_list(100000)
print(func_1(numbers))
print(func_2(numbers))

print(timeit.timeit("func_1(numbers)", globals=globals(), number=1000))  # 19.684575000000002
print(timeit.timeit("func_2(numbers)", globals=globals(), number=1000))  # 15.374730999999997

"""
Снизил время выполнения функции за счет использования list comprehension.
list comprehension работают эффективней простого цикла в связи с отсутсвием цикла и постоянных вызовов append.
list comprehension изначально создана для построения списков из итерируемых объектов.
"""

