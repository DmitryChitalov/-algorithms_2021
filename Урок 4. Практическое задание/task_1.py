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
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = filter(lambda i: nums[i] % 2 == 0, range(len(nums)))
    return new_arr


nums = list(range(1000))

print(timeit("func_1(nums)", globals=globals(), number=10000))
print(timeit("func_2(nums)", globals=globals(), number=10000))
print(timeit("func_3(nums)", globals=globals(), number=10000))

# Итератор заменен на list comprehension, за счет этого удалось увеличить скорость работы почти в два раза
# Но с использованием функции фильтр и лямбды скорость возрастает десятки раз
